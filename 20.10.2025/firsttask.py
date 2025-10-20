import matplotlib.pyplot as plt
import matplotlib.patches as patches
import networkx as nx

def create_idea_cloud():
    fig, ax = plt.subplots(figsize=(12, 8))

    G = nx.DiGraph()

    concepts = [
        "Заявка", "Клиент", "Статус заявки", 
        "Услуга", "Сотрудник", "База данных",
        "Обработка", "Учет", "Отчет"
    ]

    for concept in concepts:
        G.add_node(concept)

    edges = [
        ("Клиент", "Заявка"), ("Заявка", "Статус заявки"),
        ("Заявка", "Услуга"), ("Сотрудник", "Обработка"),
        ("Обработка", "Заявка"), ("База данных", "Учет"),
        ("Заявка", "База данных"), ("Учет", "Отчет"),
        ("Статус заявки", "База данных")
    ]
    
    for edge in edges:
        G.add_edge(edge[0], edge[1])
    
    pos = {
        "Заявка": (0, 0),
        "Клиент": (-2, 1),
        "Статус заявки": (1, 1),
        "Услуга": (-1, -1),
        "Сотрудник": (2, 1),
        "Обработка": (1, -1),
        "База данных": (0, 2),
        "Учет": (-1, 2),
        "Отчет": (1, 2)
    }
    
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', 
            node_size=3000, arrowsize=20, font_size=10, 
            font_weight='bold', ax=ax)
    
    ax.set_title("Облако идей: Учет заявок", size=16)
    plt.tight_layout()
    plt.show()

create_idea_cloud()

def create_participants_diagram():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    G = nx.DiGraph()
    
    participants = {
        "Клиент": "Создает заявки,\nпросматривает статус",
        "Администратор": "Обрабатывает заявки,\nуправляет системой", 
        "База данных": "Хранит информацию\nо заявках и клиентах",
        "Программа": "Обеспечивает\nвзаимодействие\nвсех компонентов"
    }
    
    for participant in participants:
        G.add_node(participant)
    
    edges = [
        ("Клиент", "Программа"),
        ("Администратор", "Программа"), 
        ("Программа", "База данных"),
        ("База данных", "Программа"),
        ("Программа", "Клиент"),
        ("Программа", "Администратор")
    ]
    
    for edge in edges:
        G.add_edge(edge[0], edge[1])
    
    pos = {
        "Клиент": (0, 0),
        "Администратор": (2, 0),
        "База данных": (1, 2),
        "Программа": (1, 1)
    }
    
    nx.draw_networkx_nodes(G, pos, node_color='lightgreen', 
                          node_size=4000)
    nx.draw_networkx_edges(G, pos, arrowstyle='->', 
                          arrowsize=20)
    
    labels = {node: f"{node}\n({desc})" for node, desc in participants.items()}
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=8)
    
    ax.set_title("Участники процесса учета заявок", size=14)
    ax.axis('off')
    plt.tight_layout()
    plt.show()

create_participants_diagram()

def create_dfd_diagram():
    fig, ax = plt.subplots(figsize=(12, 8))
    
    G = nx.DiGraph()

    elements = {
        "Клиент": "Внешняя сущность",
        "Форма заявки": "Процесс",
        "Проверка данных": "Процесс", 
        "Обработка заявки": "Процесс",
        "База данных": "Хранилище",
        "Администратор": "Внешняя сущность",
        "Отчет": "Выходные данные"
    }
    
    for element in elements:
        G.add_node(element)

    data_flows = [
        ("Клиент", "Форма заявки", "Данные клиента"),
        ("Форма заявки", "Проверка данных", "Заявка"),
        ("Проверка данных", "Обработка заявки", "Проверенная заявка"),
        ("Обработка заявки", "База данных", "Сохранить данные"),
        ("База данных", "Обработка заявки", "Получить данные"),
        ("Обработка заявки", "Администратор", "Уведомление"),
        ("Обработка заявки", "Отчет", "Статистика"),
        ("Администратор", "Обработка заявки", "Действия")
    ]
    
    for flow in data_flows:
        G.add_edge(flow[0], flow[1])
    
    pos = {
        "Клиент": (0, 0),
        "Форма заявки": (1, 0),
        "Проверка данных": (2, 1),
        "Обработка заявки": (3, 0),
        "База данных": (2, -1),
        "Администратор": (4, 1),
        "Отчет": (4, -1)
    }

    node_colors = []
    for node in G.nodes():
        if "сущность" in elements[node]:
            node_colors.append('lightcoral')
        elif "Процесс" in elements[node]:
            node_colors.append('lightyellow')
        elif "Хранилище" in elements[node]:
            node_colors.append('lightblue')
        else:
            node_colors.append('lightgreen')
    
    nx.draw(G, pos, with_labels=True, node_color=node_colors,
            node_size=3000, arrowsize=20, font_size=9,
            edge_color='black')
    
    edge_labels = {(flow[0], flow[1]): flow[2] for flow in data_flows}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, 
                               font_size=7)
    
    ax.set_title("DFD диаграмма потоков данных", size=14)
    plt.tight_layout()
    plt.show()

create_dfd_diagram()

def create_goals_tree():
    fig, ax = plt.subplots(figsize=(10, 8))
    
    G = nx.DiGraph()

    goals = {
        "Цель системы": "Эффективный учет заявок",
        "Сбор данных": "Сбор информации о заявках",
        "Хранение": "Надежное хранение данных", 
        "Обработка": "Автоматическая обработка заявок",
        "Поиск": "Быстрый поиск информации",
        "Анализ": "Анализ эффективности",
        "Регистрация": "Регистрация новых заявок",
        "Валидация": "Проверка корректности данных",
        "Резервное копирование": "Обеспечение сохранности",
        "Фильтрация": "Фильтрация по критериям",
        "Статистика": "Статистический анализ"
    }

    edges = [
        ("Цель системы", "Сбор данных"),
        ("Цель системы", "Хранение"),
        ("Цель системы", "Обработка"), 
        ("Цель системы", "Поиск"),
        ("Цель системы", "Анализ"),
        ("Сбор данных", "Регистрация"),
        ("Сбор данных", "Валидация"),
        ("Хранение", "Резервное копирование"),
        ("Поиск", "Фильтрация"),
        ("Анализ", "Статистика")
    ]
    
    for goal in goals:
        G.add_node(goal)
    
    for edge in edges:
        G.add_edge(edge[0], edge[1])

    pos = {
        "Цель системы": (0, 3),
        "Сбор данных": (-2, 2), "Хранение": (-1, 2), 
        "Обработка": (0, 2), "Поиск": (1, 2), "Анализ": (2, 2),
        "Регистрация": (-2.5, 1), "Валидация": (-1.5, 1),
        "Резервное копирование": (-1, 1),
        "Фильтрация": (1, 1), "Статистика": (2, 1)
    }
    
    nx.draw(G, pos, with_labels=True, node_color='lightgreen',
            node_size=2500, arrowsize=15, font_size=8,
            font_weight='bold')
    
    ax.set_title("Дерево целей системы учета заявок", size=14)
    ax.axis('off')
    plt.tight_layout()
    plt.show()

create_goals_tree()

def create_processing_flowchart():
    fig, ax = plt.subplots(figsize=(12, 10))
    
    G = nx.DiGraph()

    steps = [
        "Начало",
        "Ввод данных заявки", 
        "Проверка обязательных полей",
        "Валидация данных",
        "Сохранение в БД",
        "Уведомление администратора",
        "Обновление статуса",
        "Формирование ответа",
        "Вывод результата",
        "Конец"
    ]
    
    for step in steps:
        G.add_node(step)

    sequence = [
        ("Начало", "Ввод данных заявки"),
        ("Ввод данных заявки", "Проверка обязательных полей"),
        ("Проверка обязательных полей", "Валидация данных"),
        ("Валидация данных", "Сохранение в БД"),
        ("Сохранение в БД", "Уведомление администратора"), 
        ("Уведомление администратора", "Обновление статуса"),
        ("Обновление статуса", "Формирование ответа"),
        ("Формирование ответа", "Вывод результата"),
        ("Вывод результата", "Конец")
    ]
    
    for seq in sequence:
        G.add_edge(seq[0], seq[1])

    pos = {}
    for i, step in enumerate(steps):
        pos[step] = (0, -i)

    node_colors = ['lightgreen' if step in ['Начало', 'Конец'] else 
                  'lightblue' if 'Ввод' in step or 'Вывод' in step else
                  'lightyellow' for step in steps]
    
    nx.draw(G, pos, with_labels=True, node_color=node_colors,
            node_size=3000, arrowsize=20, font_size=9,
            font_weight='bold', node_shape='s')
    
    ax.set_title("Блок-схема обработки информации: Ввод → Обработка → Вывод", size=14)
    ax.axis('off')
    plt.tight_layout()
    plt.show()

create_processing_flowchart()

def create_data_structure():
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Настраиваем область рисования
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    
    # Данные от пользователя (слева)
    user_data = {
        "ФИО клиента": "Текст",
        "Email": "Email",
        "Телефон": "Номер", 
        "Тип услуги": "Выбор из списка",
        "Описание проблемы": "Текст",
        "Дата обращения": "Дата"
    }
    
    # Данные, формируемые системой (справа)
    system_data = {
        "ID заявки": "Автономер",
        "Дата создания": "Автодата",
        "Статус заявки": "Системный статус",
        "Приоритет": "Автоназначение",
        "Исполнитель": "Назначение системой",
        "Время обработки": "Расчетное время"
    }
    
    # Рисуем блок пользовательских данных
    ax.add_patch(patches.Rectangle((1, 1), 3.5, 6, 
                                  fill=True, color='lightblue', 
                                  alpha=0.7, label='Данные от пользователя'))
    
    # Рисуем блок системных данных  
    ax.add_patch(patches.Rectangle((5.5, 1), 3.5, 6,
                                  fill=True, color='lightgreen',
                                  alpha=0.7, label='Данные от системы'))
    
    # Добавляем заголовки
    ax.text(2.75, 6.8, 'Данные от ПОЛЬЗОВАТЕЛЯ', 
            ha='center', va='center', fontsize=12, fontweight='bold')
    ax.text(7.25, 6.8, 'Данные от СИСТЕМЫ', 
            ha='center', va='center', fontsize=12, fontweight='bold')
    
    # Добавляем пользовательские данные
    y_pos = 6.2
    for field, data_type in user_data.items():
        y_pos -= 0.7
        ax.text(1.2, y_pos, f"• {field}", fontsize=10, ha='left')
        ax.text(3.8, y_pos, f"({data_type})", fontsize=9, 
                ha='right', style='italic', color='darkblue')
    
    # Добавляем системные данные
    y_pos = 6.2
    for field, data_type in system_data.items():
        y_pos -= 0.7
        ax.text(5.7, y_pos, f"• {field}", fontsize=10, ha='left')
        ax.text(8.8, y_pos, f"({data_type})", fontsize=9,
                ha='right', style='italic', color='darkgreen')
    
    # Добавляем стрелку ввода данных
    ax.arrow(4.5, 3.5, 0.8, 0, head_width=0.2, 
             head_length=0.2, fc='red', ec='red')
    ax.text(4.8, 3.8, 'Ввод данных', fontsize=10, color='red')
    
    ax.set_title("Структура исходных данных системы учета заявок", 
                 fontsize=14, fontweight='bold')
    ax.axis('off')
    plt.tight_layout()
    plt.show()

create_data_structure()

def create_er_diagram():
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Создаем граф для ER-диаграммы
    G = nx.DiGraph()
    
    # Сущности (объекты) системы
    entities = {
        "Клиент": "ID, ФИО, телефон, email",
        "Заявка": "ID, дата_создания, статус, описание", 
        "Услуга": "ID, название, категория, стоимость",
        "Сотрудник": "ID, ФИО, должность, отдел",
        "Статус": "ID, название, описание",
        "Отчет": "ID, период, тип_отчета"
    }
    
    for entity in entities:
        G.add_node(entity)
    
    # Связи между сущностями
    relationships = [
        ("Клиент", "Заявка", "оформляет"),
        ("Заявка", "Услуга", "содержит"),
        ("Сотрудник", "Заявка", "обрабатывает"),
        ("Заявка", "Статус", "имеет"),
        ("Заявка", "Отчет", "включается_в"),
        ("Сотрудник", "Услуга", "предоставляет")
    ]
    
    for rel in relationships:
        G.add_edge(rel[0], rel[1])
    
    # Позиционируем сущности
    pos = {
        "Клиент": (1, 5),
        "Заявка": (3, 5),
        "Услуга": (5, 3),
        "Сотрудник": (3, 7), 
        "Статус": (5, 5),
        "Отчет": (5, 7)
    }
    
    # Рисуем сущности как прямоугольники с атрибутами
    for entity, attributes in entities.items():
        x, y = pos[entity]
        # Рисуем прямоугольник для сущности
        ax.add_patch(patches.Rectangle((x-0.8, y-0.3), 1.6, 0.6, 
                                      fill=True, color='lightblue',
                                      alpha=0.8))
        ax.text(x, y, entity, ha='center', va='center', 
                fontweight='bold', fontsize=10)
        
        # Добавляем атрибуты под сущностью
        ax.text(x, y-0.5, attributes, ha='center', va='top',
                fontsize=8, style='italic')
    
    # Рисуем связи с подписями
    for rel in relationships:
        start, end, label = rel
        x1, y1 = pos[start]
        x2, y2 = pos[end]
        
        # Рисуем стрелку
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='->', 
                                   color='red', lw=1.5))
        
        # Добавляем подпись связи
        mid_x, mid_y = (x1+x2)/2, (y1+y2)/2
        ax.text(mid_x, mid_y, label, ha='center', va='center',
                fontsize=9, backgroundcolor='white',
                bbox=dict(boxstyle="round,pad=0.3", 
                         facecolor='white', alpha=0.8))
    
    ax.set_title("ER-диаграмма: Сущности и связи системы учета заявок", 
                 fontsize=14, fontweight='bold')
    ax.set_xlim(0, 6)
    ax.set_ylim(2, 8)
    ax.axis('off')
    plt.tight_layout()
    plt.show()

create_er_diagram()

def create_context_diagram():
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Рисуем центральную систему
    system_circle = plt.Circle((5, 5), 1.5, color='lightblue', 
                              alpha=0.8, fill=True)
    ax.add_patch(system_circle)
    ax.text(5, 5, 'Система\nучета\nзаявок', ha='center', 
            va='center', fontsize=12, fontweight='bold')
    
    # Внешние участники
    external_entities = {
        "Клиенты": (1, 3),
        "Администраторы": (1, 7), 
        "Менеджеры": (9, 7),
        "Бухгалтерия": (9, 3),
        "Техническая\nподдержка": (5, 1),
        "Система\nотчетности": (5, 9)
    }
    
    # Потоки данных к системе
    data_flows = [
        ("Клиенты", "Заявки, запросы"),
        ("Администраторы", "Управление, настройки"),
        ("Менеджеры", "Запросы, отчеты"), 
        ("Бухгалтерия", "Финансовые данные"),
        ("Техническая\nподдержка", "Тех. запросы"),
        ("Система\nотчетности", "Данные для отчетов")
    ]
    
    # Рисуем внешние сущности
    for entity, pos in external_entities.items():
        ax.add_patch(patches.Rectangle((pos[0]-1.2, pos[1]-0.4), 
                                      2.4, 0.8, fill=True, 
                                      color='lightcoral', alpha=0.7))
        ax.text(pos[0], pos[1], entity, ha='center', va='center',
                fontsize=9, fontweight='bold')
        
        # Рисуем связи с системой
        ax.plot([pos[0], 5], [pos[1], 5], 'k-', alpha=0.5)
        
        # Добавляем подписи потоков данных
        flow_label = next(flow[1] for flow in data_flows if flow[0] == entity)
        mid_x, mid_y = (pos[0] + 5) / 2, (pos[1] + 5) / 2
        ax.text(mid_x, mid_y, flow_label, ha='center', va='center',
                fontsize=8, rotation=15, 
                bbox=dict(boxstyle="round,pad=0.2", facecolor='white'))
    
    ax.set_title("Контекстная диаграмма системы\n(Границы и внешние взаимодействия)", 
                 fontsize=14, fontweight='bold')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    plt.tight_layout()
    plt.show()

create_context_diagram()

def create_problems_solutions():
    fig, ax = plt.subplots(figsize=(16, 10))
    
    # Проблемы (левая колонка)
    problems = [
        "Потеря заявок при ручной обработке",
        "Дублирование данных клиентов", 
        "Долгая обработка заявок",
        "Отсутствие уведомлений клиентов",
        "Сложность формирования отчетов",
        "Ошибки при вводе данных"
    ]
    
    # Решения (правая колонка)  
    solutions = [
        "Автоматизированная система учета",
        "Единая база данных клиентов",
        "Автоматическое назначение исполнителей",
        "Система email/SMS уведомлений", 
        "Автоматические отчеты по шаблонам",
        "Валидация данных при вводе"
    ]
    
    # Рисуем проблемы слева
    ax.text(2, 9.5, 'ПРОБЛЕМЫ', ha='center', va='center',
            fontsize=14, fontweight='bold', color='red')
    
    for i, problem in enumerate(problems):
        y_pos = 8 - i * 1.2
        ax.add_patch(patches.Rectangle((0.5, y_pos-0.4), 3, 0.8,
                                      fill=True, color='lightcoral'))
        ax.text(2, y_pos, problem, ha='center', va='center',
                fontsize=10, fontweight='bold')
    
    # Рисуем решения справа
    ax.text(8, 9.5, 'РЕШЕНИЯ', ha='center', va='center',
            fontsize=14, fontweight='bold', color='green')
    
    for i, solution in enumerate(solutions):
        y_pos = 8 - i * 1.2
        ax.add_patch(patches.Rectangle((5.5, y_pos-0.4), 3, 0.8,
                                      fill=True, color='lightgreen'))
        ax.text(7, y_pos, solution, ha='center', va='center',
                fontsize=10, fontweight='bold')
    
    # Рисуем стрелки от проблем к решениям
    for i in range(len(problems)):
        y_pos = 8 - i * 1.2
        ax.annotate("", xy=(5.5, y_pos), xytext=(3.5, y_pos),
                   arrowprops=dict(arrowstyle='->', 
                                   color='blue', lw=2,
                                   connectionstyle="arc3,rad=0"))
    
    # Добавляем заголовок
    ax.text(4, 10.2, 'АНАЛИЗ ПРОБЛЕМ И ПУТИ РЕШЕНИЯ', 
            ha='center', va='center', fontsize=16, fontweight='bold')
    
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10.5)
    ax.axis('off')
    plt.tight_layout()
    plt.show()

create_problems_solutions()

def create_final_diagram():
    fig, ax = plt.subplots(figsize=(16, 12))
    
    # Разделяем диаграмму на секции
    sections = {
        "Цели": (1, 9, 3, 2),
        "Участники": (5, 9, 3, 2), 
        "Данные": (9, 9, 3, 2),
        "Процессы": (1, 6, 3, 2),
        "Ограничения": (5, 6, 3, 2),
        "Результаты": (9, 6, 3, 2),
        "Проблемы": (1, 3, 5, 2),
        "Решения": (7, 3, 5, 2)
    }
    
    # Заполняем каждую секцию
    section_content = {
        "Цели": ["• Автоматизация учета", "• Ускорение обработки", 
                "• Улучшение качества", "• Снижение ошибок"],
        "Участники": ["Клиенты", "Администраторы", "Менеджеры", "Система"],
        "Данные": ["Заявки", "Клиенты", "Услуги", "Отчеты"],
        "Процессы": ["Ввод → Проверка → Обработка → Сохранение → Отчет"],
        "Ограничения": ["Бюджет", "Сроки", "Технологии", "Персонал"],
        "Результаты": ["Эффективность +50%", "Ошибки -80%", "Скорость +60%"],
        "Проблемы": ["Ручная обработка", "Потери данных", "Задержки"],
        "Решения": ["Автоматизация", "Единая БД", "Уведомления"]
    }
    
    # Рисуем все секции
    colors = ['lightblue', 'lightgreen', 'lightyellow', 
              'lightcoral', 'lavender', 'wheat', 'mistyrose', 'honeydew']
    
    for i, (section, coords) in enumerate(sections.items()):
        x, y, w, h = coords
        color = colors[i % len(colors)]
        
        # Рисуем рамку секции
        ax.add_patch(patches.Rectangle((x, y), w, h, 
                                      fill=True, color=color, alpha=0.7))
        ax.add_patch(patches.Rectangle((x, y), w, h, 
                                      fill=False, edgecolor='black', lw=2))
        
        # Заголовок секции
        ax.text(x + w/2, y + h - 0.2, section, 
                ha='center', va='top', fontsize=11, fontweight='bold')
        
        # Содержимое секции
        content = section_content[section]
        for j, item in enumerate(content):
            ax.text(x + 0.1, y + h - 0.5 - j*0.3, item, 
                    ha='left', va='top', fontsize=9)
    
    # Центральный заголовок
    ax.text(8, 11.5, 'ПОСТАНОВКА ЗАДАЧИ\n"СИСТЕМА УЧЕТА ЗАЯВОК"', 
            ha='center', va='center', fontsize=18, fontweight='bold')
    
    # Добавляем соединительные линии между ключевыми секциями
    connections = [
        ("Цели", "Процессы"), ("Участники", "Процессы"),
        ("Данные", "Процессы"), ("Процессы", "Результаты"),
        ("Проблемы", "Решения"), ("Ограничения", "Решения")
    ]
    
    for start, end in connections:
        x1, y1, w1, h1 = sections[start]
        x2, y2, w2, h2 = sections[end]
        
        # Соединяем центры секций
        start_x, start_y = x1 + w1/2, y1 + h1/2
        end_x, end_y = x2 + w2/2, y2 + h2/2
        
        ax.plot([start_x, end_x], [start_y, end_y], 'k-', alpha=0.5, lw=1)
    
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
    ax.axis('off')
    plt.tight_layout()
    plt.show()

create_final_diagram()