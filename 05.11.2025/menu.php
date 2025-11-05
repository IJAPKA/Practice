<?php
// menu.php - чистый PHP. Параметр ?role=admin|student|guest или из сессии.
$role = isset($_GET['role']) ? $_GET['role'] : 'guest';
$db = new PDO('sqlite:menu.db');
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Получаем id роли
$stmt = $db->prepare('SELECT id FROM roles WHERE name = ?');
$stmt->execute([$role]);
$role_row = $stmt->fetch(PDO::FETCH_ASSOC);
$role_id = $role_row ? (int)$role_row['id'] : null;

// Получаем все разрешённые пункты (включая вложенные) для роли
if ($role_id) {
    $sql = "
      SELECT mi.* FROM menu_items mi
      JOIN item_role ir ON ir.menu_item_id = mi.id
      WHERE ir.role_id = :role_id AND mi.visible = 1
      ORDER BY mi.position ASC
    ";
    $stmt = $db->prepare($sql);
    $stmt->execute([':role_id' => $role_id]);
    $items = $stmt->fetchAll(PDO::FETCH_ASSOC);
} else {
    $items = [];
}

// Преобразуем плоский список в дерево
$tree = [];
$refs = [];
foreach ($items as $it) {
    $it['children'] = [];
    $refs[$it['id']] = $it;
}
foreach ($refs as $id => $node) {
    if ($node['parent_id']) {
        if (isset($refs[$node['parent_id']])) {
            $refs[$node['parent_id']]['children'][] = &$refs[$id];
        }
    } else {
        $tree[] = &$refs[$id];
    }
}

// Функция вывода
function render_menu($nodes) {
    $html = '<ul class="nav">';
    foreach ($nodes as $n) {
        $hasChildren = !empty($n['children']);
        $html .= '<li class="nav-item'.($hasChildren?' has-children':'').'">';
        $html .= '<a href="'.htmlspecialchars($n['url']).'" data-item-id="'.intval($n['id']).'">'
              .htmlspecialchars($n['title']).'</a>';
        if ($hasChildren) {
            $html .= '<div class="dropdown"><ul>';
            foreach ($n['children'] as $c) {
                $html .= '<li><a href="'.htmlspecialchars($c['url']).'" data-item-id="'.intval($c['id']).'">'
                       .htmlspecialchars($c['title']).'</a></li>';
            }
            $html .= '</ul></div>';
        }
        $html .= '</li>';
    }
    $html .= '</ul>';
    return $html;
}

// Простая страница для демонстрации
?>
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Меню (role: <?php echo htmlspecialchars($role); ?>)</title>
<style>
/* адаптивный CSS (Flexbox) - подробнее ниже, но минимально для PHP вывода */
.nav { display:flex; list-style:none; padding:0; margin:0; gap:10px; flex-wrap:wrap; }
.nav-item { position:relative; }
.nav-item a { text-decoration:none; padding:8px 12px; display:block; }
.nav-item .dropdown { display:none; position:absolute; top:100%; left:0; background:#fff; border:1px solid #ddd; padding:8px; z-index:100; }
.nav-item:hover .dropdown { display:block; }
@media(max-width:720px){
  .nav { flex-direction:column; }
  .nav-item .dropdown { position:relative; border:0; }
}
</style>
</head>
<body>
<h2>Меню — роль: <?php echo htmlspecialchars($role); ?></h2>
<?php echo render_menu($tree); ?>

<script>
// При клике на пункт меню — отправляем лог на сервер
document.addEventListener('click', function(e){
  var a = e.target.closest('a[data-item-id]');
  if (!a) return;
  var itemId = a.getAttribute('data-item-id');
  var payload = {
    item_id: itemId,
    item_title: a.textContent,
    url: a.getAttribute('href'),
    username: '<?php echo addslashes($role); ?>' // для примера - в real получаем из сессии
  };
  // fire-and-forget. Сохранение логов на сервер
  navigator.sendBeacon('/log.php', JSON.stringify(payload));
});
</script>
</body>
</html>