import numpy as np
import matplotlib.pyplot as plt


mu = 0       
sigma = 1    


sample_sizes = [100, 1000, 10000, 100000]


fig, axs = plt.subplots(len(sample_sizes), 1, figsize=(10, 12))

for i, size in enumerate(sample_sizes):
    data = np.random.normal(mu, sigma, size)
    # Строим cтолбчатый график
    axs[i].hist(data, bins=30, density=True, alpha=0.6, color='g')
    # Настройки подграфика
    axs[i].set_title(f'Столбчатый график для {size} точек')
    axs[i].set_xlabel('Значение')
    axs[i].set_ylabel('Плотность вероятности')
    axs[i].grid()

plt.tight_layout()
plt.show()