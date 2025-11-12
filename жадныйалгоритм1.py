def greedy_resource_allocation(projects, total_resource):
  
    # Сортируем проекты по убыванию прибыли на единицу ресурса
    projects_sorted = sorted(projects, 
                           key=lambda x: x['profit'] / x['resource'], 
                           reverse=True)
    
    selected_projects = []
    used_resource = 0
    total_profit = 0
    
    # Выбираем проекты в порядке убывания эффективности
    for project in projects_sorted:
        if used_resource + project['resource'] <= total_resource:
            selected_projects.append(project)
            used_resource += project['resource']
            total_profit += project['profit']
    
    return selected_projects, total_profit, used_resource

# Входные данные
projects = [
    {'resource': 10, 'profit': 50},
    {'resource': 15, 'profit': 80},
    {'resource': 20, 'profit': 90},
    {'resource': 8, 'profit': 40}
]
total_resource = 40

# Выполнение алгоритма
selected, total_profit, used_resource = greedy_resource_allocation(projects, total_resource)

# Вывод результатов
print("Все проекты:")
for i, project in enumerate(projects, 1):
    efficiency = project['profit'] / project['resource']
    print(f"Проект {i}: ресурс={project['resource']}, прибыль={project['profit']}, эффективность={efficiency:.2f}")

print(f"\nОбщий доступный ресурс: {total_resource}")
print("\nВыбранные проекты:")
for i, project in enumerate(selected, 1):
    print(f"Проект: ресурс={project['resource']}, прибыль={project['profit']}")

print(f"\nИтоговые показатели:")
print(f"Общая прибыль: {total_profit}")
print(f"Использованный ресурс: {used_resource}")
print(f"Остаток ресурса: {total_resource - used_resource}")