import xlwt  # 写入excel文件的库
import numpy as np
hr_book = xlwt.Workbook(encoding='ascii')
hr_sheet = hr_book.add_sheet('HR_title', cell_overwrite_ok=True)  # 创建表格

data = np.loadtxt('C:\\Users\\王家桢\\Desktop\\data.txt')
final_index = int(len(data)/29)
final_data = []
for i in range(0, final_index):
    start = i*29 
    end = (i+1)*29
    final_data.append(data[start:end])
for i in range(0, len(final_data)):
    print(final_data[i])

i = 0
j = 0
for j in range(0, len(final_data)):
    for i in range(0, 29):
        hr_sheet.write(i, j, final_data[j][i])  # i，j控制表格坐标，左定格为（0，0）
hr_book.save('C:\\Users\\王家桢\\Desktop\\计算智能\\HMPSO\\对比算法\\AMSEPSO\\dim=100.xls')  # 保存文件，这里默认保存到你的相对路径，也可以设置绝对路径，与上面打开
# txt文件是一样的