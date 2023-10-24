import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sympy import Eq, symbols, solve

# 读取表格
data = pd.read_csv('pumps.csv')
a, b, c, q, h = symbols('a b c q h')

for index, row in data.iterrows():
    i, name, q1, q2, q3, h1, h2, h3 = row
    # 求二次函数参数 a, b, c
    equations = [Eq(a * q1 ** 2 + b * q1 + c, h1),
                 Eq(a * q2 ** 2 + b * q2 + c, h2),
                 Eq(a * q3 ** 2 + b * q3 + c, h3)]
    solutions = solve(equations, (a, b, c))
    a_val, b_val, c_val = solutions[a], solutions[b], solutions[c]

    # 计算新的二次函数参数
    a_new = 0.25 * a_val
    b_new = 0.5 * b_val

    # 定义 h_0 函数
    h0 = 44 + 5.78e-6 * q ** 2

    # 定义 h_1 和 h_2 函数
    h1_expr = a_val * q ** 2 + b_val * q + c_val
    h2_expr = a_new * q ** 2 + b_new * q + c_val

    # 枚举q值，找到h最接近的时刻
    q_values = np.arange(0, 2501, 1)
    closest_h1, closest_q1 = None, None
    closest_h2, closest_q2 = None, None
    closest_dif1 = 100.0
    closest_dif2 = 100.0

    for q_val in q_values:
        # h0_val = h0.subs(q, q_val)
        # h1_val = h1_expr.subs(q, q_val)
        # h2_val = h2_expr.subs(q, q_val)
        h0_val = 44.0 + 5.78e-6 * q_val ** 2
        h1_val = a_val * q_val ** 2 + b_val * q_val + c_val
        h2_val = a_new * q_val ** 2 + b_new * q_val + c_val

        if abs(h0_val - h1_val) <= closest_dif1:
            closest_h1, closest_q1 = h1_val, q_val
            closest_dif1 = abs(h0_val - h1_val)

        if abs(h0_val - h2_val) <= closest_dif2:
            closest_h2, closest_q2 = h2_val, q_val
            closest_dif2 = abs(h0_val - h2_val)

    # 输出最接近的交点坐标
    h_se, q_se = closest_h1, closest_q1
    h_fi, q_fi = closest_h2, closest_q2
    print(f"ID: {i}, Name: {name}, Intersection 1: (h_se, q_se) = ({h_se}, {q_se}), Intersection 2: (h_fi, q_fi) = ({h_fi}, {q_fi})")

    # 绘制曲线
    q_values = np.linspace(0, 2500, 200)
    h0_values = [h0.subs(q, val) for val in q_values]
    h1_values = [h1_expr.subs(q, val) for val in q_values]
    h2_values = [h2_expr.subs(q, val) for val in q_values]

    plt.figure()
    plt.plot(q_values, h0_values, label='h_0')
    plt.plot(q_values, h1_values, label='h_1')
    plt.plot(q_values, h2_values, label='h_2')
    plt.xlabel('q')
    plt.ylabel('h')
    plt.legend()
    plt.title(f'ID: {i} - {name}')
    plt.show()



    # 判断条件并输出结果
    # if q_se >= 1191.2 and q_fi >= 2278.9 and h_fi >= 73:
    # if 1 :
    #     
