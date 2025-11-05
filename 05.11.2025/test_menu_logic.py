import unittest

# пример функции (как в menu_api.py), вынесём логику в тестируемую функцию:
def build_tree(items):
    refs = {it['id']: {**it, 'children': []} for it in items}
    tree = []
    for id_, node in refs.items():
        pid = node.get('parent_id')
        if pid and pid in refs:
            refs[pid]['children'].append(node)
        else:
            tree.append(node)
    return tree

def filter_items_by_role(items, allowed_ids):
    # items - плоский список dict с id..., allowed_ids - set
    return [it for it in items if it['id'] in allowed_ids]

class TestMenuLogic(unittest.TestCase):
    def setUp(self):
        self.items = [
            {'id':1,'parent_id':None,'title':'Главная','url':'/'},
            {'id':2,'parent_id':None,'title':'Услуги','url':'/services'},
            {'id':3,'parent_id':2,'title':'Веб','url':'/services/web'},
            {'id':4,'parent_id':None,'title':'Контакты','url':'/contacts'},
        ]
    def test_build_tree(self):
        tree = build_tree(self.items)
        # должны быть 3 корневых узла (1,2,4)
        ids = sorted([n['id'] for n in tree])
        self.assertEqual(ids, [1,2,4])
        # у 'Услуги' есть child id=3
        services = next(n for n in tree if n['id']==2)
        self.assertEqual(len(services['children']),1)
        self.assertEqual(services['children'][0]['id'],3)

    def test_filter_role_change(self):
        # симулируем смену роли: студент видит 1,2,3
        allowed = {1,2,3}
        filtered = filter_items_by_role(self.items, allowed)
        ids = sorted(it['id'] for it in filtered)
        self.assertEqual(ids, [1,2,3])

    def test_empty_db(self):
        tree = build_tree([])
        self.assertEqual(tree, [])

if __name__ == '__main__':
    unittest.main()
