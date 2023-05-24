# ntfs2fat32-macOS
A Python program that on macOS detects connected NTFS hard drives, asks for permission to change the file system to FAT32 with formatting the drive, and moves files to it.


Note that you need to replace the logic for moving files to disk with your own implementation. Also make sure you have the tkinter module installed, which can be installed using the pip install tk command.

In addition, this code changes the file system by formatting the drive to the FAT32 file system. This may take some time and may not be suitable for large drives or pain.


Для автоматического запуска программы при подключении NTFS флешки в macOS вам потребуется использовать функциональность автозапуска системы. Вот как можно настроить автозапуск программы при подключении флешки:

Создайте файл AppleScript, который будет запускать вашу программу. Откройте "Script Editor" (Редактор сценариев) на вашем Mac (можно найти в папке "Утилиты").
Вставьте следующий скрипт в редактор сценариев:
do shell script "python /путь_к_вашей_программе.py" with administrator privileges
Замените "/путь_к_вашей_программе.py" на фактический путь к вашей программе Python.

Сохраните файл AppleScript с расширением ".scpt" в удобном для вас месте.
Откройте "Automator" (Автоматизатор) на вашем Mac (можно найти в папке "Утилиты").
Создайте новую рабочую область, выбрав "Application" (Приложение) в диалоговом окне "Choose a type for your document" (Выберите тип документа).
В правой части окна Automator найдите "Run AppleScript" (Выполнить AppleScript) и перетащите его в рабочую область слева.
Вставьте следующий скрипт в блок "Run AppleScript":
on run {input, parameters}
    set diskPath to POSIX path of (item 1 of input)
    do shell script "osascript /путь_к_вашему_AppleScript.scpt" with administrator privileges
end run

Замените "/путь_к_вашему_AppleScript.scpt" на фактический путь к сохраненному файлу AppleScript.

Сохраните рабочую область Automator как приложение с расширением ".app" в удобном для вас месте.
Откройте "System Preferences" (Настройки системы) на вашем Mac.
Выберите "Users & Groups" (Пользователи и группы), затем вкладку "Login Items" (Элементы входа).
Нажмите на "+" внизу списка элементов входа.
Навигируйтесь к вашему сохраненному приложению Automator и добавьте его в список.
Теперь, когда вы подключите NTFS флешку к вашему Mac, ваша программа Python будет автоматически запускаться.

Пожалуйста, обратите внимание, что для успешного запуска программы Python по автозапуску, вам необходимо предоставить соответствующие разрешения и прав
