import tkinter as tk
import pyautogui
import time

# Создаем графическое окно
root = tk.Tk()
root.geometry("1000x1000")

# Устанавливаем цвет фона окна на черный
root.configure(bg="black")

# Вычисляем центр окна
window_center_x = root.winfo_screenwidth() // 2
window_center_y = root.winfo_screenheight() // 2

# Создаем функцию, вызываемую при нажатии кнопки
def button_click():
    global index
    global start_time

    # Замеряем время прошедшее с начала перемещения курсора
    elapsed_time = time.time() - start_time
    # print(f"{sizes[index]}")
    print(distances[-index-1])
    print(f"Time Elapsed: {elapsed_time:.2f} seconds")

    pyautogui.moveTo(window_center_x, window_center_y)

    # Увеличиваем индекс текущего расстояния
    index += 1
    
    # if index < len(sizes):
    if index < len(distances):
        # new_size = sizes[index]
        # button.config(width=new_size, height=new_size)
        button.place(x=distances[index], y=distances[index])

        # Запоминаем новое начальное время
        start_time = time.time()
    else:
        root.quit()  # Завершаем приложение

sizes = [8, 10, 12, 15, 20, 30, 50, 70, 100]
distances = [0, 20, 40, 60, 100, 150, 200, 250, 300, 350]

# Создаем кнопку
initial_size = sizes[8]  # Начальный размер кнопки
button = tk.Button(root, width=initial_size, height=initial_size, bg="gray", fg="black")
button.configure(command=button_click)
button.place(x=window_center_x - initial_size // 2, y=window_center_y - 3*initial_size // 2)

# Запоминаем время начала перемещения курсора и индекс текущего размера
start_time = time.time()
index = 0

# Запускаем главный цикл tkinter
root.mainloop()
