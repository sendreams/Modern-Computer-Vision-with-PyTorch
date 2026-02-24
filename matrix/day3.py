# Day 3：秩 = 自由度
"""
目标：理解秩是空间中独立方向的数量。

练习：
构造矩阵 rank=2，将二维平面压到一条线上，观察图形变化。
改变秩，观察自由方向减少的效果。
理解“低秩 = 数据有隐藏结构”

思维关键词：压缩、隐藏方向、自由度。
"""

import matplotlib.pyplot as plt
import numpy as np

num_points = 100
v = np.random.rand(num_points, 2)
points = v * 2 - 1  # 生成 [-1, 1] 范围内的随机点
A = np.array([[1, 0], [0.5, 0]])  # 定义一个秩为1的矩阵，将点压缩到一条线上
transformed_points = points @ A.T  # 对点进行变换

plt.figure(figsize=(8, 8))
plt.scatter(points[:, 0], points[:, 1], color="blue", label="Original Points")
plt.scatter(
    transformed_points[:, 0],
    transformed_points[:, 1],
    color="red",
    label="Transformed Points (Rank=1)",
)
plt.axhline(0, color="grey", lw=0.5)
plt.axvline(0, color="grey", lw=0.5)
plt.grid()
plt.legend()
plt.title("Original vs Transformed Points with Rank=1")
plt.show()
