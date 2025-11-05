<?php
// log.php - принимает POST (raw JSON) через sendBeacon или fetch
$db = new PDO('sqlite:menu.db');
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$raw = file_get_contents('php://input');
if (!$raw) { http_response_code(400); echo "no data"; exit; }
$data = json_decode($raw, true);
if (!$data) { http_response_code(400); echo "json error"; exit; }

$user = isset($data['username']) ? $data['username'] : null;
$item_id = isset($data['item_id']) ? (int)$data['item_id'] : null;
$item_title = isset($data['item_title']) ? $data['item_title'] : null;
$url = isset($data['url']) ? $data['url'] : null;
$ip = $_SERVER['REMOTE_ADDR'] ?? null;

$stmt = $db->prepare("INSERT INTO menu_logs (username, item_id, item_title, url, user_ip, extra) VALUES (?,?,?,?,?,?)");
$stmt->execute([$user, $item_id, $item_title, $url, $ip, null]);

echo json_encode(['status'=>'ok']);
