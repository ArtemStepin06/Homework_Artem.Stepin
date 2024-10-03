import matplotlib.pyplot as plt


mass = [1, 2, 3, 4, 5]  
acceleration = [2, 3, 4, 5, 6]  
force = [2, 6, 12, 20, 30]  

plt.figure(figsize=(10, 6))
plt.plot(acceleration, force, marker='o', linestyle='-', color='b', label='Сила (F)')
plt.title('Зависимость силы от ускорения')
plt.xlabel('Ускорение (м/с²)')
plt.ylabel('Сила (Н)')
plt.grid()
plt.legend()
plt.xlim(0, 7)
plt.ylim(0, 35)
plt.show()
