# -*- encoding: utf-8 -*-

"""
    环境---数据---算法

    鸢尾花案例：
        未知数据    训练数据(监督学习)

    收集数据 --> 准备输入数据（数据类型确定等）--> 分析输入数据（数据清洗，查缺补漏，标准化）--> 特征工程(降维)
    --> 训练算法（监督学习）--> 测试算法 --> 使用算法

    supervised learning
        输入样本集  推演(预测合适的模型)  指定目标变量（标称型【有限集，分类】，数值型【无限集，回归分析】）的可能结果。
        知道预测什么，即目标变量的分类信息。

    分类算法：
        将实例数据划分到合适的分类中。
        特征 (数值型，二值型，枚举型)（样本集的列）
            （离散型，连续性，缺失值，异常值  ...）
        目标变量（标称型）（有限个数）（标记 ）
        训练集: 已分类的大量数据（特征和目标变量）

    回归算法：
        预测数值型数据
        目标变量（连续型的）

    知识表示：
        机器已经学会了如何区分，有的容易理解有的只有机器所能理解。
        表示形式：规则集 概率分布 训练样本集的一个实例

    unsupervised learning
        训练集没有类别信息，也不会给定目标值，需要对数据集做聚类操作。也可以减少数据特征的维度。
        聚类：将数据集分成由类似的对象组成的多个类的过程，也就是相似性学习！
        密度估计：将寻找描述数据统计值的过程，数据与每个分组的相识程度

        k-均值          最大期望算法
        DBSCAN          Parzen窗设计

    semi-supervised learning
    Reinforcement Learning
        数    据↘
            ↓     ↘
        模    型 ← 算法 ← 模型原型
            ↓    ↗
        预测结果↗  奖励
"""

import numpy  as np
import pandas as pd


from sklearn.metrics import accuracy_score  # 精确度
from sklearn import tree, naive_bayes, svm  # 树, 贝叶斯, 支持向量机
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import KFold

df = pd.read_csv('iris.data')
df.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
# 数据质量较好，省去数据清醒环节

print(df.head())

x = df.iloc[:, 0:4]
y = df.iloc[:, 4]

kf = KFold(n_splits=10, shuffle=True)

def eval_model(model_name, model):
    i = 0
    accuracies = []
    for train_index, test_index in kf.split(df):
        x_train, x_test = x.loc[train_index], x.loc[test_index]
        y_train, y_test = y.loc[train_index], y.loc[test_index]
        model.fit(x_train, y_train)
        y_predic = model.y_predic(x_test)
        accuracy = accuracy_score(y_pred=y_predic, y_true=y_test)
        accuracies.append(accuracy)
        i+=1
        print('decision tress 第 {} 轮：{}'.format(i, accuracy))

    print(model_name, np.mean(accuracies))

models = {
    "decision tree": lambda: tree.DecisionTreeClassifier(),   # 决策树
    "random forest": lambda: RandomForestClassifier(),        # 随机森林
    "svm": lambda: svm.SVC(),                                 # 支持向量机
    "GBDT": lambda: GradientBoostingClassifier(),             # 梯度提升
    "MLP": lambda: MLPClassifier(max_iter=1000)               # 多层感知器 perception
}

if __name__ == "__main__":
    for mname, m in models.items():
        eval_model(mname, m())