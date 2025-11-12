def greedy_resource_allocation(projects, total_resource):
    projects_with_eff = []
    for i, (resource, profit) in enumerate(projects):
        efficiency = profit / resource
        projects_with_eff.append((i, resource, profit, efficiency))
    
    projects_sorted = sorted(projects_with_eff, key=lambda x: x[3], reverse=True)
    
    selected = []
    total_profit = 0
    used_resource = 0
    
    for idx, resource, profit, eff in projects_sorted:
        if used_resource + resource <= total_resource:
            selected.append(idx)
            total_profit += profit
            used_resource += resource
    
    return selected, total_profit, used_resource

projects = [(10, 50), (15, 80), (20, 90), (8, 40)]
total_resource = 40

selected, profit, used = greedy_resource_allocation(projects, total_resource)

print("Проекты:", projects)
print("Общий ресурс:", total_resource)
print("Выбранные проекты:", selected)
print("Общая прибыль:", profit)
print("Использовано ресурсов:", used)
print("Остаток ресурсов:", total_resource - used)

print("\nДетализация:")
for i, (r, p) in enumerate(projects):
    eff = p / r
    status = "✓" if i in selected else "✗"
    print(f"Проект {i}: ресурс={r}, прибыль={p}, эффективность={eff:.2f} {status}")
