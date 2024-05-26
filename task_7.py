
import matplotlib.pyplot as plt
import numpy as np

num_simulations = 100000

# масив для підрахунку результатів
results = np.zeros(11)  # Можливі суми від 2 до 12

# симуляції
for _ in range(num_simulations):
    dice1 = np.random.randint(1, 7)  
    dice2 = np.random.randint(1, 7)  
    throw_sum = dice1 + dice2
    results[throw_sum - 2] += 1  # Кількість разів, скільки випадає кожна сума для запису в масив

# Обчислимо ймовірності
probabilities = results / num_simulations

# результати у відсотках
for sum_value in range(2, 13):
    print(f"Сума {sum_value}: {results[sum_value - 2]} разів, Ймовірність: {probabilities[sum_value - 2]* 100:.2f}%")

# Значення сум випадкових кидків
sum_values = list(range(2, 13))

# графік
plt.bar(sum_values, probabilities * 100, color='skyblue')
plt.title('Ймовірності сум випадкових кидків двох кубиків')
plt.xlabel('Сума')
plt.ylabel('Ймовірність, %')
plt.ylim(0, max(probabilities * 100) + 2)
plt.xticks(range(2, 13, 1))
plt.show()



