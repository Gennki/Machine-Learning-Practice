import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(-2, 2, 100)
y = 3 * x + 2

# 创建图像
plt.plot(x, y)
# 显示图像
plt.show()
