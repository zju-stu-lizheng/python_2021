import torch
import numpy as np

# np_data = np.arange(6).reshape((2,3))
# torch_data = torch.from_numpy(np_data)
# tensor2array = torch_data.numpy()
# print('\n numpy',np_data,
#       '\n torch',torch_data,
#       '\n',tensor2array)

# abs
# data = [-1, -2, 1, 2]
# tensor = torch.FloatTensor(data)    # 32bit

# print('\n abs',
#       '\n numpy', np.abs(data),
#       '\n torch: ', torch.abs(tensor))
#
# print('\n sin',
#       '\n numpy', np.sin(data),
#       '\n torch: ', torch.sin(tensor))
#
# print('\n mean',
#       '\n numpy', np.mean(data),
#       '\n torch: ', torch.mean(tensor))

data = [[1, 2], [3, 4]]
tensor = torch.FloatTensor(data)    # 32bit
data = np.array(data)
print(
      '\n numpy:', data.dot(data),
      '\n torch:', torch.mm(tensor, tensor)
)
