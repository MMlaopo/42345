import numpy as np
import math
from matplotlib import pyplot as plt # 导入matplotlib
from matplotlib import font_manager # 导入字体管理模块
import random # 导入随机生成模块
my_font = font_manager.FontProperties(fname="C:/WINDOWS/Fonts/STSONG.TTF")
# 定义中文字体属性，文字储存路径可以在C:/WINDOWS/Fonts/找到，这里我设置的宋体
plt.xlabel("时间",fontproperties = my_font,fontsize = 18)
# 在设置x坐标中文标注，令fontproperties = my_font，fontsize令字体为18号
# plt.title，plt.ylabel，plt.xticks，plt.yticks设置中文标注类似

my_font = font_manager.FontProperties(fname="C:/WINDOWS/Fonts/STSONG.TTF")
avepbest = \mu_pbest
print(avepbest)
#定义中文字体属性，文字储存路径可以在C:/WINDOWS/Fonts/找到，这里我设置的宋体
y = [random.randint(20,35) for i in range(120)]#y值为120个在20-35之间随机数
x = range(0,120)#x值为0-120
plt.figure(figsize=(15,10),dpi=90)#图片大小为15*10，每英寸90个像素点
_x_labels = ["10点{}分".format(i) for i in range(60)]
_x_labels += ["11点{}分".format(i) for i in range(60)]#设置x坐标轴中文刻度
plt.xticks(list(x[::3]),_x_labels[::3],rotation=45,fontproperties=my_font,fontsize = 12)#坐标轴刻度显示步长为3，为了避免坐标轴字体重叠，旋转45度，fontproperties设置字体
plt.plot(x,y)
plt.xlabel("x",fontproperties = my_font,fontsize = 18)#设置x坐标标注，字体为18号
plt.ylabel("f(x)",fontproperties = my_font,fontsize = 18)#设置y坐标标注
plt.title("根据",fontproperties = my_font,fontsize = 24)#设置标题
plt.plot(x,y)#绘图
plt.show()#显示
def gd(x, mu=0, sigma=1):
    """根据公式，由自变量x计算因变量的值
    Argument:
      x: array
        输入数据（自变量）
      mu: float
        均值
      sigma: float
        方差
    """
    left = 1 / (np.sqrt(2 * math.pi) * np.sqrt(sigma))
    right = np.exp(-(x - mu) ** 2 / (2 * sigma))
    return left * right


if __name__ == '__main__':
    # 自变量
    x = np.arange(-4, 5, 0.1)
    # 因变量（不同均值或方差）
    y_1 = gd(x, 1.77, 0.44)


    # 绘图
    plt.plot(x, y_1, color='green')

    # 设置坐标系
    plt.xlim(-5.0, 5.0)
    plt.ylim(-0.2, 1)

    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))

    plt.legend(labels=['$\mu = , \sigma^2=b$'])
    plt.show()