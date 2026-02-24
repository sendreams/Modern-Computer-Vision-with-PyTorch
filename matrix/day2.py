# Day 2：矩阵 = 空间变形器
"""
目标：把矩阵运算理解为空间的旋转/拉伸/压缩/反射。

练习：
随机生成二维矩阵 A，生成一批二维向量点。
绘制原始点阵和 A·点阵后的点阵。
尝试不同矩阵（旋转、缩放、投影）理解每种变换的视觉效果。

思维关键词：变形、坐标系转换。
"""

import matplotlib.pyplot as plt
import numpy as np

num_points = 100
v = np.random.rand(num_points, 2)
points = v * 2 - 1  # 生成 [-1, 1] 范围内的随机点
A = np.array([[0.5, -0.5], [0.5, 0.5]])  # 定义一个旋转+缩放矩阵
transformed_points = points @ A.T  # 对点进行变换

plt.figure(figsize=(8, 8))
plt.scatter(points[:, 0], points[:, 1], color="blue", label="Original Points")
plt.scatter(
    transformed_points[:, 0],
    transformed_points[:, 1],
    color="red",
    label="Transformed Points",
)
plt.axhline(0, color="grey", lw=0.5)
plt.axvline(0, color="grey", lw=0.5)
plt.grid()
plt.legend()
plt.title("Original vs Transformed Points")
plt.show()
