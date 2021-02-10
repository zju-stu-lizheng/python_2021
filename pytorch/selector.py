import torch
import time
from torch.autograd import Variable
import torch.nn.functional as F
import matplotlib.pyplot as plt

# 伪数据
n_data = torch.ones(100,2)
x0 = torch.normal(2*n_data,1)   # class0 x data,shape(100,2)
y0 = torch.zeros(100)           # class0 y data,shape(100,1)
x1 = torch.normal(-2*n_data,1)    # class1 x data,shape(100,2)
y1 = torch.ones(100)            # class1 y data,shape(100,1)
x = torch.cat((x0,x1), 0).type(torch.FloatTensor)   # floattensor = 32-bit floating
y = torch.cat((y0,y1),).type(torch.LongTensor)      # longtensor = 64-bit integer

x, y = Variable(x), Variable(y)

# 画图
# plt.scatter(x.data.numpy()[:,0], x.data.numpy()[:,1], c=y.data.numpy(), s=100, lw=0,cmap='RdYlGn')
# plt.show()


# method 1
class Net(torch.nn.Module):  # 继承 torch 的 Module
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()     # 继承 __init__ 功能
        # 定义每层用什么样的形式
        self.hidden = torch.nn.Linear(n_feature, n_hidden)   # 隐藏层线性输出
        self.predict = torch.nn.Linear(n_hidden, n_output)   # 输出层线性输出

    def forward(self, x):   # 这同时也是 Module 中的 forward 功能
        # 正向传播输入值, 神经网络分析出输出值
        x = F.relu(self.hidden(x))      # 激励函数(隐藏层的线性值)
        x = self.predict(x)             # 输出值
        return x


net1 = Net(n_feature=2, n_hidden=10, n_output=2)
print(net1)  # net 的结构
"""
Net (
  (hidden): Linear (2 -> 10)
  (predict): Linear (10 -> 2)
)
"""

# method 2
net2 = torch.nn.Sequential(
    torch.nn.Linear(2,10),
    torch.nn.ReLU(),    # 这是一个类
    torch.nn.Linear(10,2)
)
print(net2)

# optimizer 是训练的工具
optimizer = torch.optim.SGD(net2.parameters(), lr=0.02)  # 传入net的所有参数，学习率
loss_function = torch.nn.CrossEntropyLoss()    # 预测值和真实值的误差计算公式（概率）

plt.ion()   # 画图
plt.show()

for t in range(100):
    time.sleep(0.5)
    out = net2(x)     # 喂给 net 训练数据x，输出预测值

    loss = loss_function(out, y)     # prediction,y的顺序不能变：计算两者的误差

    optimizer.zero_grad()   # 清空上一步的残余更新参数值
    loss.backward()         # 误差反向传播，计算参数更新值
    optimizer.step()        # 将参数更新值施加到 net 的parameters上
    if t % 2 == 0:
        plt.cla()
        # 过了一道 softmax 的激励函数后的最大概率才是预测值
        prediction = torch.max(F.softmax(out), 1)[1]  # [-2,-12,20] -> [0.1,0.2,0.7]
        pred_y = prediction.data.numpy().squeeze()
        target_y = y.data.numpy()
        plt.scatter(x.data.numpy()[:, 0], x.data.numpy()[:, 1], c=pred_y, s=100, lw=0, cmap='RdYlGn')
        accuracy = sum(pred_y == target_y) / 200.  # 预测中有多少和真实值一样
        plt.text(1.5, -4, 'Accuracy=%.2f' % accuracy, fontdict={'size': 20, 'color': 'red'})
        plt.pause(0.1)
        pass


plt.ioff()   # 画图
plt.show()



