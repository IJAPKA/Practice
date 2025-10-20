import matplotlib.pyplot as plt
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