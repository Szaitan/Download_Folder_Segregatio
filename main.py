import os
from pathlib import Path

downloads_path = Path.home() / "Downloads"

list_with_files = os.listdir(downloads_path)

list_with_file_type = []
list_with_files_to_move = []

for fname in os.listdir(downloads_path):
    path = os.path.join(downloads_path, fname)

    if os.path.isdir(path):
        pass
    else:
        split_file = fname.rsplit(".", 1)
        if split_file[1] in list_with_file_type:
            pass
        else:
            list_with_file_type.append(split_file[1])
        list_with_files_to_move.append(fname)

if os.path.isdir(f"{downloads_path}/Segregated Files"):
    print(True)
else:
    os.mkdir(os.path.join(f"{downloads_path}", "Segregated Files"))

for file_type in list_with_file_type:
    if not os.path.isdir(f"{downloads_path}/Segregated Files/{file_type}"):
        os.mkdir(os.path.join(f"{downloads_path}/Segregated Files", file_type))

for file_ending in list_with_file_type:
    for file in list_with_files_to_move:
        split_file = file.rsplit(".", 1)

        if file_ending == split_file[1]:

            src_path = os.path.join(downloads_path, file)
            dst_path = os.path.join(f"{downloads_path}/Segregated Files/{file_ending}", file)
            os.rename(src_path, dst_path)
