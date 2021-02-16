import numpy as np
result = np.empty((2,2),order = 'C')  # shape为（2，2），内存未初始化
print(type(result))