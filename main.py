import os

download_folder_direction = f"../../../{os.getlogin()}/Downloads"

list_with_files = os.listdir(download_folder_direction)

list_with_file_type = []
list_with_files_to_move = []

for fname in os.listdir(download_folder_direction):
    path = os.path.join(download_folder_direction, fname)

    if os.path.isdir(path):
        continue
    else:
        split_file = fname.rsplit(".", 1)
        list_with_file_type.append(split_file[1])
        list_with_files_to_move.append(fname)


list_with_file_type_no_duplicates = list(dict.fromkeys(list_with_file_type))

if os.path.isdir(f"../../../{os.getlogin()}/Desktop/Segregated Files"):
    print(True)
else:
    os.mkdir(os.path.join(f"../../../{os.getlogin()}/Desktop", "Segregated Files"))


for file_type in list_with_file_type_no_duplicates:
    if not os.path.isdir(f"../../../{os.getlogin()}/Desktop/Segregated Files/{file_type}"):
        os.mkdir(os.path.join(f"../../../{os.getlogin()}/Desktop/Segregated Files", file_type))

print(list_with_files_to_move)
print(list_with_file_type_no_duplicates)

for file_ending in list_with_file_type_no_duplicates:
    for file in list_with_files_to_move:
        split_file = file.rsplit(".", 1)
        print(file)
        print(split_file[1])
        if file_ending == split_file[1]:
            print('test')
            src_path = os.path.join(download_folder_direction, file)
            dst_path = os.path.join(f"../../../{os.getlogin()}/Desktop/Segregated Files/{file_ending}", file)
            os.rename(src_path, dst_path)
