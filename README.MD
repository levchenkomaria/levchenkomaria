# Приближённые и эвристические алгоритмы
## Левченко Мария УИБО-09-24
### Вариант 13.
#### Алгоритм жадного распределения ресурсов

ШАГ 1: Инициализация и вычисление эффективности

for project in projects:

    project['efficiency'] = project['profit'] / project['resource']

Назначение: Для каждого проекта вычисляется показатель efficiency, который представляет собой отношение прибыли к требуемому ресурсу. Это позволяет оценить, насколько эффективно каждый проект использует ограниченные ресурсы.

ШАГ 2: Сортировка проектов по эффективности

projects_sorted = sorted(projects, key=lambda x: x['efficiency'], reverse=True)

Назначение: Проекты упорядочиваются по убыванию значения efficiency. Параметр reverse=True обеспечивает сортировку от наибольшего к наименьшему. Это гарантирует, что наиболее "рентабельные" проекты будут рассматриваться первыми.

ШАГ 3: Жадный выбор проектов

selected_projects = []

used_resource = 0

total_profit = 0

for project in projects_sorted:

    if used_resource + project['resource'] <= total_resource:

        selected_projects.append(project)

        used_resource += project['resource']

        total_profit += project['profit']

Назначение:

· selected_projects = [] - инициализация пустого списка для выбранных проектов

· used_resource = 0 - отслеживание суммарного использованного ресурса

· total_profit = 0 - накопление общей прибыли

· Условие if used_resource + project['resource'] <= total_resource проверяет, не превысит ли добавление текущего проекта доступный лимит ресурсов

· Если условие выполняется, проект добавляется в selected_projects, а значения used_resource и total_profit обновляются
