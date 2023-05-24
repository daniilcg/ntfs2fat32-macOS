# ntfs2fat32-macOS
a Python program that on macOS detects connected NTFS hard drives, asks for permission to change the file system to FAT32 with formatting the drive, and moves files to it.
Note that you need to replace the logic for moving files to disk with your own implementation. Also make sure you have the tkinter module installed, which can be installed using the pip install tk command.

In addition, this code changes the file system by formatting the drive to the FAT32 file system. This may take some time and may not be suitable for large drives or pain.
