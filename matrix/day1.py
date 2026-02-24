# Day 1：向量是箭头，空间就是舞台
"""
目标：把向量具象化为二维/三维箭头。

练习：
随机生成 2~3 维向量，用箭头画出来（Python：matplotlib 或 Java: JavaFX/Processing）。
练习向量加法、数乘，画出合成结果。

思考：向量加法 = 空间中的平移叠加；数乘 = 拉伸/压缩。
思维关键词：平移、拉伸、组合。
"""

import matplotlib.pyplot as plt
import numpy as np

# 生成随机向量
v1 = np.random.rand(2)  # 2D 向量
v1 = np.array([0.5, 0.8])  # 固定向量，便于观察变化
v2 = np.random.rand(2)  # 另一个 2D 向
v2 = np.array([0.2, 0.4])  # 固定向量，便于观察变化

# 绘制向量
plt.figure()
# 绘制 v1 和 v2
plt.quiver(
    0, 0, v1[0], v1[1], angles="xy", scale_units="xy", scale=1, color="r", label="v1"
)
plt.quiver(
    0, 0, v2[0], v2[1], angles="xy", scale_units="xy", scale=1, color="b", label="v2"
)
plt.xlim(-1, 2)  # 设置 x 轴范围
plt.ylim(-1, 2)  # 设置 y 轴范围
plt.axhline(0, color="grey", lw=0.5)  # 绘制 x 轴
plt.axvline(0, color="grey", lw=0.5)  # 绘制 y 轴
plt.grid()  # 添加网格
plt.legend()  # 添加图例
plt.title("Random 2D Vectors")
plt.show()
