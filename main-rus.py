import os
import tkinter as tk
from tkinter import messagebox

def ask_permission():
    response = messagebox.askyesno("Форматирование диска", "Хотите ли вы изменить файловую систему с NTFS на FAT32 без форматирования диска?")
    return response

def show_notification():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Перенос файлов", "Перенос файлов успешно завершен!")

def detect_ntfs_disks():
    ntfs_disks = []
    output = os.popen('diskutil list').read()
    lines = output.split('\n')
    for line in lines:
        if 'Microsoft Basic Data' in line:
            parts = line.split()
            ntfs_disks.append(parts[-1])
    return ntfs_disks

def convert_filesystem(disk):
    try:
        os.system(f"diskutil eraseVolume FAT32 NewFAT32 {disk}")
        return True
    except Exception as e:
        print(f"Произошла ошибка при изменении файловой системы: {e}")
        return False

def transfer_files(disk):
    # Перенос файлов на диск
    # Замените эту часть кода на свою реализацию переноса файлов

    # Пример кода:
    files_to_transfer = ['file1.txt', 'file2.txt', 'file3.txt']
    for file in files_to_transfer:
        os.system(f"cp {file} {disk}")

def main():
    ntfs_disks = detect_ntfs_disks()
    
    if not ntfs_disks:
        print("Жесткие диски NTFS не найдены.")
        return

    for disk in ntfs_disks:
        print(f"Найден NTFS-диск: {disk}")
        response = ask_permission()
        
        if response:
            success = convert_filesystem(disk)
            if success:
                transfer_files(disk)
                show_notification()
        else:
            print("Процесс изменения файловой системы отменен пользователем.")

if __name__ == '__main__':
    main()
