# 1 FLOWER RECOGNITION 花卉识别

> 注：本作品是OpenMMLab2023实战营的实验一**基础**作品

![dataset-cover](https://i.imgur.com/VhlkOrW.jpg)

## INTRODUCTION 介绍

- 使用简单：只需任意摄像头获取图片，就可以得到花卉的「分类标识」
- 类名序列：
  - daisy
  - dandelion
  - rose
  - sunflower
  - tulip

- 模型文件（"accuracy_top-1": 97.02797）：https://github.com/TianWen580/mmcls-exp1/releases/download/homework/epoch_43.pth

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

  [下载模型](https://download.openmmlab.com/mmclassification/v0/resnet/resnet18_batch256_imagenet_20200708-34ab8f90.pth)并存放在 *mmclassification/pth/* 中

- 启动训练

  ```shell
  python tools/train.py \
     configs/resnet/resnet18_b16_flower.py \
      --work-dir work_dirs/flower
  ```

  启动后训练log、配置文件以及所得模型将保存在 *mmclassification/work_dirs/flower/* 中

# 2 GARBAGE RECOGNITION 迅捷垃圾识别

> 注：本作品是OpenMMLab2023实战营的实验一**进阶**作品

![dataset-cover.jpg](https://i.imgur.com/RDVyxz0.jpg)

## INTRODUCTION 介绍

- 使用简单：只需任意摄像头获取图片，就可以得到垃圾的「分类标识」
- 类名序列：
  - paper
  - green-glass
  - clothes
  - metal
  - cardboard
  - trash
  - biological
  - white-glass
  - battery
  - brown-glass
  - plastic
  - shoes

- 模型文件（"accuracy_top-1": 95.58918）：https://github.com/TianWen580/mmcls-exp1/releases/download/homework-advanced/latest.pth

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

  - **Resize** ：多尺度增强，比例范围0.75-1.25
  - **RandomCrop**：随机裁剪图像，范围最小为全图75%
  - **RandomFlip**：水平翻转，由于数据普遍以水平视角拍摄，不适合采用垂直翻转

- 测试时增强：

  - **MultiScaleFlipFile**：多尺度增强，比例范围0.75, 1.0, 1.25
  - **RandomFlip**：水平翻转

- 学习率策略

  - 线性热身

    ![SCR-20230207-jpq](https://i.imgur.com/KQ3Jls6.jpg)

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

  [下载模型](https://download.openmmlab.com/mmclassification/v0/resnet/resnet18_batch256_imagenet_20200708-34ab8f90.pth)并存放在 *mmclassification/pth/* 中

- 启动训练

  ```shell
  python tools/train.py \
     configs/resnet/resnet18_b16_garbage.py \
      --work-dir work_dirs/garbage
  ```

  启动后训练log、配置文件以及所得模型将保存在 *mmclassification/work_dirs/garbage/* 中