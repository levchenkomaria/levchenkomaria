
# Входные данные
projects = [
    {"resource": 10, "profit": 50},
    {"resource": 15, "profit": 80},
    {"resource": 20, "profit": 90},
    {"resource": 8,  "profit": 40}
]

total_resource = 40  # общий объем ресурсов

# Вычисляем прибыль на единицу ресурса
for p in projects:
    p["ratio"] = p["profit"] / p["resource"]

# Сортируем проекты по убыванию прибыльности
projects.sort(key=lambda x: x["ratio"], reverse=True)

used_resource = 0
total_profit = 0
chosen = []

# Жадный выбор проектов
for p in projects:
    if used_resource + p["resource"] <= total_resource:
        # Берем проект полностью
        used_resource += p["resource"]
        total_profit += p["profit"]
        chosen.append((p["resource"], p["profit"]))
    else:
        # Если не хватает ресурсов — берем частично (дробный вариант)
        remain = total_resource - used_resource
        if remain > 0:
            part = remain / p["resource"]
            total_profit += p["profit"] * part
            chosen.append((remain, p["profit"] * part))
            used_resource += remain
        break

# Вывод результата
print("Выбранные проекты:")
for r, pr in chosen:
    print(f"  - Ресурс = {r}, Прибыль = {pr:.2f}")

print(f"\nОбщий использованный ресурс: {used_resource}")
print(f"Общая прибыль: {total_profit:.2f}")
