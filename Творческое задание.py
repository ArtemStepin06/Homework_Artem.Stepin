import tkinter as tk
from tkinter import Label, PhotoImage, ttk
from PIL import Image, ImageTk



brawlers = {
    "Соло ШД": ["Шелли", "Кендзи", "Вольт"],
    "Дуо ШД": ["Брок", "Джесси", "Пайпер"],
    "Нокаут": ["Гром", "Мортис", "Леон"],
    "Броулбол": ["Гейл", "Биби", "Френк"],
    "Ограбление": ["Чак", "Джесси", "Колетт"],
}


maps = {
    "Соло ШД": ["Озеро мертвецов", "Всё или ничего", "Штольня", "Двойная проблема", "Проход"],
    "Захват кристалов": ["Полёт фантазии", "Убежище", "Потасовка в роукулле","Ветренная долина", "Красочный закат"],
    "Нокаут": ["Ущелье золотой руки ", "В чситом поле", "Живописный утёс", "Междуречье", "Пылающий феникс"],
    "Броулбол": ["Трипл-дриблинг", "Пинбол", "Супербляж", "Пенальти", "Солнечный футбол"],
    "Ограбление": ["Взятие моста", "Горячая кукуруза", "Пороховый каньон", "Загадочный секрте", "Надёжное укрытие"],
}

def get_brawlers():
    selected_mode = mode_combobox.get()
    selected_map = map_combobox.get()
    
    if selected_mode:
        brawler_list = brawlers[selected_mode]
        result_text = f" Пик персонажей для режима '{selected_mode}' на карте '{selected_map}': {', '.join(brawler_list)}"
    else:
        result_text = "Выберите режим игры."
    
    result_label.config(text=result_text)



root = tk.Tk()
root.title("Brawl Stars - Идеальный пик персонажей")


root.geometry("1920x1080")




root.image = PhotoImage(file="Brawl_image.png")  


bg_logo = Label(root, image=root.image)
bg_logo.place(relx=.5, rely=.5, anchor="center") 


mode_label = tk.Label(root, text="Выберите режим игры:",background = "pink")
mode_label.pack()


mode_combobox = ttk.Combobox(root, values=list(brawlers.keys()))
mode_combobox.pack()


map_label = tk.Label(root, text="Выберите карту:",background = "pink")
map_label.pack()


map_combobox = ttk.Combobox(root, values=[])
map_combobox.pack()


def update_maps(event):
    selected_mode = mode_combobox.get()
    map_combobox['values'] = maps.get(selected_mode, [])
    map_combobox.set('')  

mode_combobox.bind("<<ComboboxSelected>>", update_maps)


get_brawlers_button = tk.Button(root, text="Получить персонажей", command=get_brawlers,background = 'light green')
get_brawlers_button.pack()



result_label = tk.Label(root, text="", background= "light blue")
result_label.pack()


root.mainloop()
