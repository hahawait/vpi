import tkinter as tk
import pyautogui
import time

# Создаем графическое окно
root = tk.Tk()
root.geometry("1000x1000")

# Устанавливаем цвет фона окна на черный
root.configure(bg="gray")

# Вычисляем центр окна
window_center_x = root.winfo_screenwidth() // 2
window_center_y = root.winfo_screenheight() // 2

# Создаем функцию, вызываемую при нажатии кнопки
def button_click():
    global index
    global start_time
    global background_colors

    # Замеряем время прошедшее с начала перемещения курсора
    elapsed_time = (time.time() - start_time) * 1000
    print(f"{int(elapsed_time)}")

    pyautogui.moveTo(window_center_x, window_center_y)

    # Увеличиваем индекс текущего расстояния
    index += 1
    
    if index < len(background_colors):
        root.configure(bg=background_colors[index])
        # Запоминаем новое начальное время
        start_time = time.time()
    else:
        root.quit()  # Завершаем приложение

sizes = 3
distances = 600
background_colors = [
    "Aqua", "Gray", "Navy", "Silver", "Black", "Green", "Olive",
    "Teal", "Lime", "Purple", "White", "Fuchsia", "Maroon", "Red", "Yellow"
]

# Создаем кнопку
initial_size = sizes  # Начальный размер кнопки
button = tk.Button(root, width=initial_size, height=initial_size, bg="red", fg="red")
button.configure(command=button_click)
button.place(x=window_center_x - initial_size // 2, y=window_center_y - 3*initial_size // 2)

# Запоминаем время начала перемещения курсора и индекс текущего размера
start_time = time.time()
index = 0

# Запускаем главный цикл tkinter
root.mainloop()
