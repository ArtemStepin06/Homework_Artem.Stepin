import matplotlib.pyplot as plt


amount = [15, 17, 30, 24, 14]
groups = ["понедельник", "вторник", "среда", "четверг", "пятница"]
color_ = ["green", "pink", "red", "grey", "purple"]

plt.pie(amount, colors=color_, labels=groups, autopct="%1.f%%")
plt.title("Процент загруженности в день")
plt.show()