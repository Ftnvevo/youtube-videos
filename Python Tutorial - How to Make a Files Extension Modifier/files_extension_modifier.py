import os

path_folder = r'' # e.g. C:\Users\Fabio-Work\Desktop\python_project

print()
print('Path: {}'.format(path_folder))
print()
old_extension = '.' + input('Enter the old extension (e.g. txt, mp3) --> ')
new_extension = '.' + input('Enter the new extension (e.g. txt, mp3) --> ')
print()

files_counter = 0

with os.scandir(path_folder) as files_and_folders:
    for element in files_and_folders:
        if element.is_file():
            # tuple_root_ext = os.path.splitext(element.path)
            # root = tuple_root_ext[0]
            # ext = tuple_root_ext[1]

            root, ext = os.path.splitext(element.path)
            if ext == old_extension:
                new_path = root + new_extension
                os.rename(element.path, new_path)
                files_counter += 1

print('** RECAP **')
print()
print('Number of files processed: {}'.format(files_counter))
print('Extension: from {} to {}'.format(old_extension, new_extension))
