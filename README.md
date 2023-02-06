# FLOWER RECOGNITION 花卉识别

> 注：本作品是OpenMMLab2023实战营的实验一基础作品

## INTRODUCTION 介绍

- 使用简单：只需任意摄像头获取图片，就可以得到花卉的「分类标识」
- 模型文件：

## 环境配置

```shell
python 3.8
pytorch 1.10.1
cuda 11.1
mmcv-full 1.7.0
mmcls 0.25.0
```

按照[MMClassification官方文档](https://mmclassification.readthedocs.io/en/master/install.html)的要求配置环境

## SOLUTION 算法方案

- Baseline：ResNet18
- 类别均衡：以数据量最少的类为标准，手动去除了其余类别的部份数据使类别间数据量差异减少
- 数据增广：
  - **Resize** ：多尺度增强，范围224
  - **RandomCrop**：随机裁剪图像，范围最小为全图75%
  - **RandomFlip**：水平翻转，由于数据普遍以水平视角拍摄，不适合采用垂直翻转

## 模型训练与测试

- 数据集组织

  可以利用脚本 *mmclassification/mytools/dataset_divide.py* 自动划分数据集为如下格式

  ```
  |--data
     |--train
     |  |--class1
     |  |--class2
     |  |--...
     |--val
     |  |--class1
     |  |--class2
     |  |--...
     |--train.txt
     |--val.txt
     |--classes.txt
  ```

  

- 加载预训练模型

  [下载模型](https://download.openmmlab.com/mmclassification/v0/resnet/resnet18_batch256_imag enet_20200708-34ab8f90.pth)并存放在 *mmclassification/pth/* 中

- 启动训练

  ```shell
  python tools/train.py \
     configs/resnet/resnet18_b16_flower.py \
      --work-dir work_dirs/flower
  ```

  启动后训练log、配置文件以及所得模型将保存在 *mmclassification/work_dirs/flower/* 中