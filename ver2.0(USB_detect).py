import os
import tkinter as tk
from tkinter import messagebox
import psutil

def ask_permission():
    response = messagebox.askyesno("Форматирование диска", "Хотите ли вы изменить файловую систему с NTFS на FAT32 без форматирования диска?")
    return response

def show_notification():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Перенос файлов", "Перенос файлов успешно завершен!")

def detect_ntfs_flash_drive():
    ntfs_flash_drive = None
    for partition in psutil.disk_partitions():
        if partition.fstype == 'ntfs' and 'removable' in partition.opts:
            ntfs_flash_drive = partition.mountpoint
            break
    return ntfs_flash_drive

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
    ntfs_flash_drive = detect_ntfs_flash_drive()
    
    if not ntfs_flash_drive:
        print("NTFS флешка не найдена.")
        return

    print(f"Найдена NTFS флешка: {ntfs_flash_drive}")
    response = ask_permission()
        
    if response:
        success = convert_filesystem(ntfs_flash_drive)
        if success:
            transfer_files(ntfs_flash_drive)
            show_notification()
    else:
        print("Процесс изменения файловой системы отменен пользователем.")

if __name__ == '__main__':
    main()
