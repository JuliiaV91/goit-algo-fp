
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm (items, budget):
    # співвідношення калорій до вартості 
    ratios = [(item, info['calories'] / info['cost']) for item, info in items.items()]
    
    ratios.sort(key=lambda x: x[1], reverse=True)
    
    selected_items = []
    total_cost = 0
    
    for item, ratio in ratios:
        item_cost = items[item]['cost']
        if total_cost + item_cost <= budget:
            selected_items.append(item)
            total_cost += item_cost
    if not selected_items:
        print("У вас недостатньо коштів.")   

    return selected_items

budget = 100
selected_items = greedy_algorithm(items, budget)
print("Вибрані страви:", selected_items)

def dynamic_programming (items, budget):
    # список для зберігання максимальної кількості калорій для кожного бюджету
    max_calories = [0] * (budget + 1)

    for i in range(1, budget + 1):
        for item, info in items.items():
            item_cost = info['cost']
            item_calories = info['calories']
            if item_cost <= i:
                max_calories[i] = max(max_calories[i], max_calories[i - item_cost] + item_calories)

    selected_items = []
    remaining_budget = budget
    for i in range(budget, 0, -1):
        if max_calories[i] != max_calories[i - 1]:
            for item, info in items.items():
                if info['cost'] <= remaining_budget and max_calories[i] - info['calories'] == max_calories[i - info['cost']]:
                    selected_items.append(item)
                    remaining_budget -= info['cost']
                    break
    if not selected_items:
        print("У вас недостатньо коштів.")
    return selected_items

budget = 1
selected_items = dynamic_programming(items, budget)
print("Вибрані страви:", selected_items)
