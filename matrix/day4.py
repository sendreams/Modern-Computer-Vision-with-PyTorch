# Day 4：特征向量和特征值 = 空间主拉伸方向
"""
目标：把特征向量理解为“空间变形最明显方向”，特征值 = 拉伸倍数。

练习：
构造对称矩阵，绘制单位圆变形后的椭圆。
找出主轴方向（特征向量），测量伸长倍数（特征值）。
观察拉伸大方向 vs 小方向，理解“重要性”。

思维关键词：主方向、拉伸、重要程度。
"""

import matplotlib.pyplot as plt
import numpy as np

A = np.array([[2, 1], [1, 2]])  # 定义一个对称矩阵
eigenvalues, eigenvectors = np.linalg.eig(A)  # 计算特征值和特征向量
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
# 绘制单位圆和变形后的椭圆
theta = np.linspace(0, 2 * np.pi, 100)
circle = np.array([np.cos(theta), np.sin(theta)])  # 单位圆上的点
ellipse = A @ circle  # 对单位圆进行变换得到椭圆

plt.figure(figsize=(8, 8))
plt.plot(circle[0], circle[1], label="Unit Circle", color="blue")
plt.plot(ellipse[0], ellipse[1], label="Transformed Ellipse", color="red")
# 绘制特征向量
for i in range(len(eigenvalues)):
    vec = eigenvectors[:, i] * eigenvalues[i]  # 特征向量乘以特征值表示拉伸后的方向
    plt.arrow(
        0, 0, vec[0], vec[1], head_width=0.1, head_length=0.1, fc="green", ec="green"
    )
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.axhline(0, color="grey", lw=0.5)
plt.axvline(0, color="grey", lw=0.5)
plt.grid()
plt.legend()
plt.title("Unit Circle and Transformed Ellipse with Eigenvectors")
plt.show()
