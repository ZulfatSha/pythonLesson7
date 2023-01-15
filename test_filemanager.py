from filemanager import copy_file_or_directory, author_info, quit, filenames
import shutil
import os
import sys


# Копирование файла или директории
def test_copy_file_or_directory():
    name = 'folder'
    new_name = 'folder_copy'
    if os.path.isdir(name):
        assert shutil.copytree(name, new_name)

# Список файлов
def test_filenames():
    for i in os.listdir():
        if os.path.isfile(i):
            assert True

# Проверка автора
def test_author_info():
    assert author_info() == 'Leonid Orlov'

# Выход
def test_quit():
    if SystemExit == 0:
        assert sys.exit(0)

#Грязные функции



