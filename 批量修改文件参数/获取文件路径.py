import os

sign = 'c2=0.5'

def func(fileDir):
    for root, dirs, files in os.walk(fileDir):
        if sign in dirs:
            for dir in dirs:
                # print(dir)
                temp = os.path.join(root, dir)
                temp = eval(repr(temp).replace('\\', '\\'))
                temp = eval(repr(temp).replace('\\', '/'))
                temp = eval(repr(temp).replace('//', '/'))
                temp = eval(repr(temp).replace('//', '/'))
                print(temp)
                with open('file_path_PSO.txt', mode='a') as filename:
                    filename.write(temp)
                    filename.write('\n')  # 换行

if __name__ == "__main__":
    fileDir = "C:\\Users\\王家桢\\Desktop\\lab\\PSO"
    func(fileDir)
