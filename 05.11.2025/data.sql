-- data.sql
INSERT INTO menu (name) VALUES ('main');

-- роли
INSERT INTO roles (name) VALUES ('admin'), ('student'), ('guest');

-- пункты меню (menu_id = 1)
INSERT INTO menu_items (menu_id, parent_id, title, url, position) VALUES
(1, NULL, 'Главная', '/', 1),
(1, NULL, 'Услуги', '/services', 2),
(1, NULL, 'Портфолио', '/portfolio', 3),
(1, NULL, 'Контакты', '/contacts', 4),
(1, NULL, 'Панель администратора', '/admin', 5),
(1, 2, 'Веб-разработка', '/services/web', 1),       -- child of Услуги
(1, 2, 'Дизайн', '/services/design', 2),           -- child of Услуги
(1, 3, 'Игры', '/portfolio/games', 1);             -- child of Портфолио

-- назначение ролей для пунктов
-- admin видит всё:
INSERT INTO item_role (menu_item_id, role_id)
SELECT id, (SELECT id FROM roles WHERE name='admin') FROM menu_items;

-- student видит: Главная, Услуги (и вложения), Портфолио
INSERT INTO item_role (menu_item_id, role_id)
SELECT id, (SELECT id FROM roles WHERE name='student') FROM menu_items
WHERE title IN ('Главная','Услуги','Портфолио','Веб-разработка','Дизайн','Игры');

-- guest видит только: Главная, Контакты
INSERT INTO item_role (menu_item_id, role_id)
SELECT id, (SELECT id FROM roles WHERE name='guest') FROM menu_items
WHERE title IN ('Главная','Контакты');
