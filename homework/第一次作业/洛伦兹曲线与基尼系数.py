import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker


current_path = os.path.dirname(__file__)
with open(current_path+'./data_pums_2000.csv', 'r') as f:
    info = f.readlines()
    info.pop(0)

    # 处理收入数据
    tot_income = 0.
    for i in range(len(info)):
        _, info[i] = info[i].split(',')
        info[i] = int(info[i])
        tot_income += info[i]
    info.sort()

    # 计算累积收入份额和累积人口数量百分比
    tot_tmp = 0
    x_axis = list(range(1, len(info)+1))
    for i in range(len(info)):
        tot_tmp += info[i]
        info[i] = tot_tmp/tot_income
        x_axis[i] /= len(info)

    # 由于统计人数较多，可以求和近似计算洛伦兹曲线下方面积,可以同时计算洛伦兹系数的上下界
    upper_bound = 1.
    lower_bound = 1.
    dx = x_axis[1]-x_axis[0]
    for i in range(len(info)-1):
        upper_bound -= 2*info[i]*dx
    for i in range(1, len(info)):
        lower_bound -= 2*info[i]*dx
    print('%.6f' % lower_bound, '<= Gini Index <=', '%.6f' % upper_bound)

    # 将横纵坐标格式化为百分比格式
    plt.gca().xaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))
    plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))

    # 使用matplot绘图
    plt.title('Lorenz Curve')
    plt.ylabel('Cumulative Share of Income')
    plt.xlabel('Cumulative Share of Population')
    plt.plot(x_axis, info)
    plt.show()
