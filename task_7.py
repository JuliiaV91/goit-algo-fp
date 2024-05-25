
import matplotlib.pyplot as plt
import numpy as np

# Кількість симуляцій
num_simulations = 100000

# Ініціалізуємо масив для підрахунку результатів
results = np.zeros(11)  # Можливі суми від 2 до 12

# Проведемо симуляції
for _ in range(num_simulations):
    dice1 = np.random.randint(1, 7)  # Кубик 1
    dice2 = np.random.randint(1, 7)  # Кубик 2
    throw_sum = dice1 + dice2
    results[throw_sum - 2] += 1  # Підрахунок суми

# Обчислимо ймовірності
probabilities = results / num_simulations

# Виведемо результати
for sum_value in range(2, 13):
    print(f"Сума {sum_value}: {results[sum_value - 2]} разів, Ймовірність: {probabilities[sum_value - 2]* 100:.2f}%")


# Значення сум випадкових кидків
sum_values = list(range(2, 13))

# Побудова графіку
plt.bar(sum_values, probabilities * 100, color='skyblue')

# Налаштування заголовка та міток осей
plt.title('Ймовірності сум випадкових кидків двох кубиків')
plt.xlabel('Сума')
plt.ylabel('Ймовірність, %')

# Встановлення обмежень для осі Y
plt.ylim(0, max(probabilities * 100) + 2)
plt.xticks(range(2, 13, 1))
# Відображення графіку
plt.show()



