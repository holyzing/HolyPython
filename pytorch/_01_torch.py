# -*- encoding: utf-8 -*-

import torch
import numpy as np
from torch import nn, optim
from torchvision.datasets import ImageFolder, folder
from torch.utils.data import Dataset, DataLoader, dataloader

class EntryLevel(object):
    @staticmethod
    def say_hello():
        f = torch.Tensor([[1, 2], [3, 4], [5, 6], [7, 8]])
        i = torch.IntTensor([1, 2, 3, 4])  # default type is float
        # print(f, "{}".format(f.size()), f.numpy(), torch.from_numpy(np.arange(1, 5)))
        # print(torch.Tensor(np.zeros((4, 2))), torch.zeros((4, 2)))

        # if requires_grad=False return a Tensor
        var = torch.autograd.Variable(i, requires_grad=True)
        print(var.data, var.grad, var.grad_fn)

        # TODO gradient | Backpropagation gradient
        code = '{}=torch.autograd.Variable(torch.Tensor([{}]), requires_grad=True)'
        w = x = b = None  # To prevent warnings from appearing in the IDE
        for i, j in {'x': 1, 'w': 2, 'b': 3}.items():
            exec(code.format(i, j), globals())
        y = w * x + b
        y.backward()
        print(x.grad, w.grad, b.grad)

        x = torch.autograd.Variable(torch.randn(3), requires_grad=True)
        y = x*2
        # The gradient of each component
        y.backward(torch.FloatTensor([1, 0.1, 0.01]))
        print(x.grad)

        if torch.cuda.is_available():
            print(torch.cuda)

    class CustomDataSet(Dataset):
        def __init__(self, csv_file, text_file, root_dir, other_file):
            pass

        def __len__(self):
            pass

        def __getitem__(self, idx):
            pass

        dataiter = DataLoader(EntryLevel.CsvDataSet, batch_size=32,
                              shuffle=True, collate_fn=dataloader.default_collate)

        image_dataset = ImageFolder(
            roor='root_path', transform=None, loader=folder.default_loader)

    class NNModule(nn.Module):
        """ 模组  层结构  损失函数 模型构建 """

        def __init__(self, *args):
            super(NNModule, self).__init__()
            # self.convl = nn.Conv2d(in_channels, out_channels, kernel_size)

        def forward(self, x):
            """
                每次调用就相当于用该计算图定义的相同参数做一次前向传播，这得益于
                PyTorch的自动求导功能，所以我们不需要自己编写反向传播
            """
            x = self.convl(x)
            return x

        @staticmethod
        def loss_func():
            # 均方误差、多分类的交叉熵，以及二分类的交叉熵
            # criterion = nn.CrossEntropyLoss()
            # loss = criterion(output, target)
            pass

        @staticmethod
        def optimize():
            # 使得损失的数最小化或最大化,化算法就是一种调整模型参数更新的策略

            # 一阶优化算法：使用各个参数的梯度值来更新参数，最常用的是梯度下降。
            # 梯度下降的功能是通过寻找最小值，控制方差，更新模型参数，最终使模型收敛。
            # 网络的参数更新公式：θ = θ-η*∂J(θ)/∂θ  【η:学习率  ∂J(θ)/∂θ:梯度】

            # 二阶优化算法：基于牛顿法，使用二阶导数进行优化，但是计算成本高 。

            # 其它优化算法：随机梯度下降，以及添加动量的随机棉度下降，自适应学习率

            # 1:需要被更新的模型参数  lr: 学习率  momentum：动量是0.9的随机梯度下降
            # optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
            # optimizer.zeros() # 优化器梯度归零
            # loss.backward()   # 损失函数反向传播
            # optimizer.step()  # 优化器通过梯度做一步参数更新
            pass

        @staticmethod
        def save_model():
            # torch.save(model, 'path/model.pth')
            # torch.save(model.state_dict(), 'path/model_state.pth')
            # torch.load('model.pth')
            # model.load_state_dic(torch.load('model state.pth'))
            pass
