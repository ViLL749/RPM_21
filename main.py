import tkinter as tk
from tkinter import messagebox
import vectors as ve


def calculate():
    result_text.delete(1.0, tk.END)  # Очищаем текстовое поле перед расчетом
    try:
        # Получаем входные данные
        vector1_input = vector1_entry.get().strip().split()
        vector2_input = vector2_entry.get().strip().split()

        # Преобразование строк в числа с помощью обычных циклов
        vector1 = []
        for x in vector1_input:
            vector1.append(float(x))

        vector2 = []
        for x in vector2_input:
            vector2.append(float(x))

        scalar = float(scalar_entry.get().strip())

        # Здесь будут выполнены проверки из вашей библиотеки
        dot_result = ve.myltiply_vectors(vector1, vector2)  # Скалярное произведение
        scalar_result = ve.multiply_by_scalar(vector1, scalar)  # Умножение вектора на скаляр

        # Отображение результатов
        result_dot_text = f"Скалярное произведение: {dot_result}\n"
        result_scalar_text = f"Результат умножения вектора на скаляр: {scalar_result}\n"
        result_text.insert(tk.END, result_dot_text + result_scalar_text)

    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))  # Отображение ошибки в случае неверного ввода


# Создание основного окна приложения
root = tk.Tk()
root.title("Операции с векторами")

# Ввод данных
tk.Label(root, text="Вектор 1 (разделите пробелом):").pack()
vector1_entry = tk.Entry(root)
vector1_entry.pack()

tk.Label(root, text="Вектор 2 (разделите пробелом):").pack()
vector2_entry = tk.Entry(root)
vector2_entry.pack()

tk.Label(root, text="Скаляр:").pack()
scalar_entry = tk.Entry(root)
scalar_entry.pack()

# Кнопка для выполнения расчетов
calculate_button = tk.Button(root, text="Вычислить", command=calculate)
calculate_button.pack()

# Поле для отображения результатов
result_text = tk.Text(root, height=5, width=60)
result_text.pack()

# Запуск основного цикла приложения
root.mainloop()
