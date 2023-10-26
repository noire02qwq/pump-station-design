import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sympy import Eq, symbols, solve

# 读取表格
data = pd.read_csv('pumps.csv')
a, b, c, q, h = symbols('a b c q h')

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

# 配色
col = ['#211A3E', '#453370', '#A597B6', '#FEF3E8', '#D06C9D']

for index, rowa in data.iterrows():
    for index, rowb in data.iterrows():
        i, namea, q1a, q2a, q3a, h1a, h2a, h3a = rowa
        j, nameb, q1b, q2b, q3b, h1b, h2b, h3b = rowb
        if i != 4 or j != 8:
            continue
        equations = [Eq(a * q1a ** 2 + b * q1a + c, h1a),
                 Eq(a * q2a ** 2 + b * q2a + c, h2a),
                 Eq(a * q3a ** 2 + b * q3a + c, h3a)]
        solutions = solve(equations, (a, b, c))
        aa, ba, ca = solutions[a], solutions[b], solutions[c]
        equations = [Eq(a * q1b ** 2 + b * q1b + c, h1b),
                 Eq(a * q2b ** 2 + b * q2b + c, h2b),
                 Eq(a * q3b ** 2 + b * q3b + c, h3b)]
        solutions = solve(equations, (a, b, c))
        ab, bb, cb = solutions[a], solutions[b], solutions[c]
        q_cur1 = np.linspace(0, 2500, 1000)
        h_cur_t = 44 + 5.78e-6 * q_cur1 ** 2
        h_cur_1 = aa * q_cur1 ** 2 + ba * q_cur1 + ca
        plt.plot(q_cur1, h_cur_t, label = r"管路特性曲线", color = col[0])
        plt.plot(q_cur1, h_cur_1, label = r"水泵1特性曲线", color = col[2])
        h_min = max(aa * q3a ** 2 + ba * q3a + ca, ab * q3b ** 2 + bb * q3b + cb)
        h_max = min(aa * q1a ** 2 + ba * q1a + ca, ab * q1b ** 2 + bb * q1b + cb)
        h_cur_ab = np.arange(h_min, h_max, 0.2)
        q_cur_ab = q_now = (h_cur_ab / aa - (4 * aa * ca - ba ** 2) / (4 * (aa ** 2))) ** 0.5 - (ba / (2 * aa)) + (h_cur_ab / ab - (4 * ab * cb - bb ** 2) / (4 * (ab ** 2))) ** 0.5 - (bb / (2 * ab))
        plt.plot(q_cur_ab, h_cur_ab, label = "并联特性曲线", color = col[4])

# 设置图表标题和坐标轴标签
plt.scatter([1191.2], [53.0], label = r'二级工况点$M_2$', color = col[1], marker = '^')
plt.scatter([2248.9], [72.7], label = r'一级工况点$M_1$', color = col[1], marker = 's')
plt.scatter([2323.9], [57.7], label = r'消防工况点$M_p$', color = 'red', marker = 'x')
plt.title('水泵与管路特性曲线')
plt.ylim(0, 90)
plt.xlabel('流量Q(L/s)')
plt.ylabel('扬程H(m)')

# 显示图例
plt.legend()

# 显示图表
plt.show()