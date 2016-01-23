####**朴素贝叶斯模型预测 Titanic 遇难人员**

<font color= #778899>kaggle 数据竞赛：Titanic: Machine Learning from Disaster</font>
<a>https://www.kaggle.com/c/titanic</a>

<font color=#483D8B size = 4>背景分析</font>

沉没的泰坦尼克号是历史上最臭名昭著的沉船。1912年4月15日，泰坦尼克号撞上冰山后沉没，2224名乘客和机组人员1502人死亡。

一个海难导致生命损失的原因是没有足够的救生艇的乘客和船员。除过有一些因素的影响，在沉船事故中，一些群体的人更可能生存其他群体更容易生还，比如妇女，儿童和上层阶级等。

<font color=#483D8B size = 4>问题概述</font>

要求完成对具备什么特征的人可能生存的分析，使用机器学习算法来预测乘客是否能在悲剧中幸存下来。

<font color=#483D8B size = 4>数据处理</font>

缺失数据：平均值补全

<font color=#483D8B size = 4>基于年龄，性别，票价的贝叶斯模型</font>

- 朴素贝叶斯分类器的公式：
  假设某个体有n项特征（Feature），分别为F1、F2、...、Fn。现有m个类别（Category），分别为C1、C2、...、Cm。贝叶斯分类器就是计算出概率最大的那个分类，也就是求下面这个算式的最大值：P(C|F1F2...Fn) = P(F1F2...Fn|C)P(C) / P(F1F2...Fn)
- 朴素贝叶斯分类器：
  P(F1F2...Fn|C)P(C) = P(F1|C)P(F2|C) ... P(Fn|C)P(C),上式等号右边的每一项，都可以从统计资料中得到，由此就可以计算出每个类别对应的概率，从而找出最大概率的那个类。

- 分别计算：P(survived|age)，P(survived|sex)，P(survived|fare)，P(survived)
- P(survived|age,sex,fare)
  =P(survived|age)P(survived|sex)P(survived|fare)P(survived)








