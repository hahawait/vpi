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
    global click_counter
    global index
    global start_time

    # Замеряем время прошедшее с начала перемещения курсора
    elapsed_time = time.time() - start_time
    print(f"Time Elapsed: {elapsed_time:.2f} seconds")
    print(distances[-index-1])

    pyautogui.moveTo(window_center_x, window_center_y)

    """2 группа эксперементов"""
    # # Проверяем, было ли нажатие мимо кнопки
    # if abs(window_center_x - distances[index]) > button_size // 2 or abs(window_center_y - distances[index]) > 3 * button_size // 2:
    #     click_counter += 1  # Увеличиваем счетчик нажатий мимо кнопки
    #     print(click_counter)

    # Увеличиваем индекс текущего расстояния
    index += 1
    
    if index < len(distances):
        # Перемещаем кнопку на новое расстояние
        button.place(x=distances[index], y=distances[index])
        
        # Запоминаем новое начальное время
        start_time = time.time()
    else:
        root.quit()  # Завершаем приложениее

distances = [0, 20, 40, 60, 100, 150, 200, 250, 300, 350]

# Создаем кнопку
button_size = 10  # Размер кнопки (x, 3x)
button = tk.Button(root, width=button_size, height=3*button_size, bg="gray", fg="black")
button.configure(command=button_click)
button.place(x=distances[0], y=distances[0])

# Запоминаем время начала перемещения курсора и индекс текущего расстояния
start_time = time.time()
index = 0
click_counter = 0

# Запускаем главный цикл tkinter
root.mainloop()
