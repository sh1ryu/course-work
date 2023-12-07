import tkinter as tk
from tkinter import filedialog
import os

def convert_to_all():
    try:
        file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title='Выберите файл', filetypes=(('Текстовые файлы', '*.txt'),))
        if file_path:
            from_system = from_var.get()
            to_system = to_var.get()
            output_file_path = os.path.join(os.path.dirname(file_path), 'output.txt')

            with open(file_path, 'r') as file:
                numbers = file.read().split()

                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    for number in numbers:
                        try:
                            decimal = int(number, int(from_system))

                            converted_number = ""

                            if int(to_system) < 1 or int(to_system) > 50:
                                print("Система счисления должна быть от 1 до 50")
                            else:
                                converted_number = format(decimal, f"0{to_system}d")

                            output_file.write(f'Число {number} из системы счисления {from_system} в систему счисления {to_system}: {converted_number}\n')

                        except ValueError:
                            print(f"Ошибка преобразования числа: {number}")

            result_label.config(text='Конвертация завершена. Результаты сохранены в файл.')

            os.startfile(output_file_path)
    
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

root = tk.Tk()
root.title('Конвертер систем счисления')
root.geometry('400x123')

from_label = tk.Label(root, text='Выберите систему счисления (из):')
from_label.pack()

from_var = tk.StringVar(root)
from_entry = tk.Entry(root, textvariable=from_var)
from_entry.pack()

to_label = tk.Label(root, text='Выберите систему счисления (в):')
to_label.pack()

to_var = tk.StringVar(root)
to_entry = tk.Entry(root, textvariable=to_var)
to_entry.pack()

button = tk.Button(root, text='Выбрать файл и конвертировать', command=convert_to_all)
button.pack()

result_label = tk.Label(root, text='')
result_label.pack()

root.mainloop()