import tkinter as tk
from tkinter import filedialog
import os

def convert_to_all():
    try:
        file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title='Выберите файл', filetypes=(('Текстовые файлы', '*.txt'),))
        if file_path:
            system = system_var.get()
            output_file_path = os.path.join(os.path.dirname(file_path), 'output.txt')

            with open(file_path, 'r') as file:
                numbers = file.read().split()

                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    for number in numbers:
                        try:
                            decimal = int(number)

                            if system == 'Двоичная':
                                converted_number = bin(decimal)[2:]
                            elif system == 'Восьмеричная':
                                converted_number = oct(decimal)[2:]
                            elif system == 'Шестнадцатеричная':
                                converted_number = hex(decimal)[2:].upper()
                            elif system == 'Десятичная':
                                converted_number = str(decimal)

                            output_file.write(f'Число {number} в {system.lower()} системе: {converted_number}\n')
                        
                        except ValueError:
                            print(f"Ошибка преобразования числа: {number}")

            result_label.config(text='Конвертация завершена. Результаты сохранены в файл.')
    
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

root = tk.Tk()
root.title('Конвертер систем счисления')
root.geometry('400x100')


label = tk.Label(root, text='Выберите систему счисления:')
label.pack()

system_var = tk.StringVar(root)
system_var.set('Двоичная')

system_menu = tk.OptionMenu(root, system_var, 'Двоичная', 'Восьмеричная', 'Шестнадцатеричная', 'Десятичная')
system_menu.pack()

button = tk.Button(root, text='Выбрать файл и конвертировать', command=convert_to_all)
button.pack()

result_label = tk.Label(root, text='')
result_label.pack()

root.mainloop()