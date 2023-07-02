import shutil
import os

def copy_files(src_dir, dest_dir):
    # 创建目标文件夹
    os.makedirs(dest_dir, exist_ok=True)
    # 复制所有文件
    for file_name in os.listdir(src_dir):
        src_file = os.path.join(src_dir, file_name)
        dest_file = os.path.join(dest_dir, file_name)
        shutil.copy(src_file, dest_file)

# 示例用法
with open('file_path_DE.txt', 'r') as file:
    for line in file:
        line = line.rstrip()
        print(line)
        copy_files(r"C:\Users\王家桢\Desktop\test", line)
