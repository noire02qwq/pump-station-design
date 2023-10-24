import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import scipy.interpolate as spi

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
data = pd.read_csv('data.csv')

# 从表格中提取两列数据
# x = np.array(data.iloc[:, 0])
# y = np.array(data.iloc[:, 1])

# 配色
# col = ['#211A3E', '#453370', '#A597B6', '#FEF3E8', '#D06C9D']
# col = ['#3A1B19', '#7B595E', '#C7A085', '#FCF0E1', '#C94737']
# col = ['#33395B', '#5D74A2', '#C4D8F2', '#F2E8E3', '#7C282B']

# 绘制散点图
# plt.scatter(x, y)

# 插值函数拟合平滑曲线
# f = spi.interp1d(x, y, kind='quadratic')
# x_new = np.linspace(x.min(), x.max(), 300)
# y_new = f(x_new)

# 绘制平滑曲线
# plt.plot(x_new, y_new)

# 设置图表标题和坐标轴标签
# plt.title('name')
# plt.xlabel(data.columns[0])
# plt.ylabel(data.columns[1])

# 进行线性回归
# coefficients = np.polyfit(x, y, 1)
# slope, intercept = coefficients

# 绘制线性回归线
# y_fit = slope * x + intercept
# plt.plot(x, y_fit, label=f"y = {slope:.2f}x + {intercept:.2f}")

# 设置图表标题和坐标轴标签
# plt.title('name')
# plt.xlabel(data.columns[0])
# plt.ylabel(data.columns[1])

# 显示图例
plt.legend()

# 显示图表
plt.show()

# 计算R平方
# y_mean = np.mean(y)
# SS_tot = np.sum((y - y_mean)**2)
# SS_res = np.sum((y - y_fit)**2)
# R2 = 1 - SS_res / SS_tot

# 输出斜率、截距、R Square
# print('slope = %.2f, intercept = %.2f, R Square = %.2f' % (slope, intercept, R2))

