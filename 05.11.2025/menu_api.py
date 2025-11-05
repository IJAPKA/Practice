#!/usr/bin/env python3
# menu_api.py - minimal REST API. Запуск: python3 menu_api.py
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse as up
import json
import sqlite3
import datetime

DB = 'menu.db'

def get_role_id(conn, role_name):
    cur = conn.execute("SELECT id FROM roles WHERE name=?", (role_name,))
    r = cur.fetchone()
    return r[0] if r else None

def fetch_items_for_role(conn, role_id):
    # берём видимые элементы для роли
    cur = conn.execute("""
      SELECT mi.id, mi.parent_id, mi.title, mi.url, mi.position
      FROM menu_items mi
      JOIN item_role ir ON ir.menu_item_id = mi.id
      WHERE ir.role_id = ? AND mi.visible = 1
      ORDER BY mi.position ASC
    """, (role_id,))
    rows = cur.fetchall()
    items = [dict(id=r[0], parent_id=r[1], title=r[2], url=r[3], position=r[4]) for r in rows]
    return items

def build_tree(items):
    refs = {it['id']: {**it, 'children': []} for it in items}
    tree = []
    for id_, node in refs.items():
        pid = node['parent_id']
        if pid and pid in refs:
            refs[pid]['children'].append(node)
        else:
            tree.append(node)
    return tree

class Handler(BaseHTTPRequestHandler):
    def _send_json(self, obj, code=200):
        data = json.dumps(obj, ensure_ascii=False).encode('utf-8')
        self.send_response(code)
        self.send_header("Content-Type","application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        parsed = up.urlparse(self.path)
        if parsed.path == '/api/menu':
            q = up.parse_qs(parsed.query)
            role = q.get('role', ['guest'])[0]
            conn = sqlite3.connect(DB)
            role_id = get_role_id(conn, role)
            if not role_id:
                self._send_json({'error':'role not found'}, 404); return
            items = fetch_items_for_role(conn, role_id)
            tree = build_tree(items)
            self._send_json({'role': role, 'menu': tree})
            return
        else:
            self.send_response(404); self.end_headers()

    def do_POST(self):
        parsed = up.urlparse(self.path)
        if parsed.path == '/api/log':
            length = int(self.headers.get('Content-Length', 0))
            raw = self.rfile.read(length).decode('utf-8')
            try:
                data = json.loads(raw)
            except:
                self._send_json({'error':'bad json'}, 400); return
            # Ожидаем: username, item_id, item_title, url
            username = data.get('username')
            item_id = data.get('item_id')
            item_title = data.get('item_title')
            url = data.get('url')
            ip = self.client_address[0]
            conn = sqlite3.connect(DB)
            conn.execute("INSERT INTO menu_logs (username, item_id, item_title, url, user_ip, action_time) VALUES (?,?,?,?,?,?)",
                         (username, item_id, item_title, url, ip, datetime.datetime.utcnow().isoformat()))
            conn.commit()
            self._send_json({'status':'ok'})
            return
        self.send_response(404); self.end_headers()

if __name__ == '__main__':
    print("Starting server on http://127.0.0.1:8000")
    HTTPServer(('0.0.0.0', 8000), Handler).serve_forever()