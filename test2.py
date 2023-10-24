import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from sympy import Eq, symbols, solve

sys.stdout = open('res.txt', 'w')

# 读取表格
data = pd.read_csv('pumps.csv')
a, b, c, q, h = symbols('a b c q h')

for index, rowa in data.iterrows():
    for index, rowb in data.iterrows():
        i, namea, q1a, q2a, q3a, h1a, h2a, h3a = rowa
        j, nameb, q1b, q2b, q3b, h1b, h2b, h3b = rowb
        print("id:", i, j)
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
        # h0 = 44 + 5.78e-6 * q ** 2
        # qinva = (h / aa - (4 * aa * ca - ba ** 2) / (4 * (aa ** 2))) - (ba / (2 * aa)) ** 0.5
        # qinvb = (h / ab - (4 * ab * cb - bb ** 2) / (4 * (ab ** 2))) - (bb / (2 * ab)) ** 0.5
        # qt = qinva + qinvb
        q_values_a = np.arange(q1a - 500, q3a, 0.2)
        h_resa, q_resa = 0.0, 0.0
        h_mdif = 100.0
        for q_now in q_values_a:
            h_a = aa * q_now ** 2 + ba * q_now + ca
            h_t = 44 + 5.78e-6 * q_now ** 2
            if abs(h_a - h_t) <= h_mdif:
                h_mdif = abs(h_a - h_t)
                h_resa, q_resa = h_a, q_now
        print("hresa = %.2f, qresa = %.1f" % (h_resa, q_resa))
        h_min = max(aa * q3a ** 2 + ba * q3a + ca, ab * q3b ** 2 + bb * q3b + cb)
        h_max = min(aa * q1a ** 2 + ba * q1a + ca, ab * q1b ** 2 + bb * q1b + cb)
        print("hmm:", h_min, h_max)
        h_values_t = np.arange(h_min, h_max, 0.02)
        h_rest, q_rest = 0.0, 0.0
        q_mdif = 10000.0
        for h_now in h_values_t:
            q_now = (h_now / aa - (4 * aa * ca - ba ** 2) / (4 * (aa ** 2))) ** 0.5 - (ba / (2 * aa)) + (h_now / ab - (4 * ab * cb - bb ** 2) / (4 * (ab ** 2))) ** 0.5 - (bb / (2 * ab))
            q_t = ((h_now - 44.0) / 5.78e-6) ** 0.5
            if abs(q_t - q_now) <= q_mdif:
                q_mdif = abs(q_t - q_now)
                h_rest, q_rest = h_now, q_now
        print("hrest = %.2f, qrest = %.1f" % (h_rest, q_rest))

