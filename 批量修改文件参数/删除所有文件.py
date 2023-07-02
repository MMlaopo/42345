import os

# 指定文件夹路径
with open('file_path_DE.txt', 'r') as file:
    for line in file:
        folder_path = line.rstrip()
        print(line)
        # 遍历文件夹中的所有文件
        for filename in os.listdir(folder_path):
            # 构造文件路径
            file_path = os.path.join(folder_path, filename)
            # 判断是否是文件，是文件则删除
            if os.path.isfile(file_path):
                os.remove(file_path)

