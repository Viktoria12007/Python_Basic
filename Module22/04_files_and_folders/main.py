import os


def get_info_files_folders(path, total_size=0, count_dirs=0, count_files=0):
    for element in os.listdir(path):
        next_path = os.path.join(path, element)
        if os.path.isfile(next_path):
            count_files += 1
            total_size += os.path.getsize(next_path)
        elif os.path.isdir(next_path):
            count_dirs += 1
            total_size, count_dirs, count_files = get_info_files_folders(next_path, total_size, count_dirs, count_files)
    return total_size, count_dirs, count_files


path = os.path.join('..', '..', 'Module22')
total_size, count_dirs, count_files = get_info_files_folders(path)
print('Размер каталога (в Кб):', total_size / 1024)
print('Количество подкаталогов:', count_dirs)
print('Количество файлов:', count_files)
