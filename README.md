# Convert_COCO_to_YOLO_Convert_Polygon_to_Rectangle_Split_dataset



### 简介

由于项目需要，使用CVAT进行标注，使用多边形进行标注，为了获取MOTS算法所需的标注文件。但是，仍需要使用YOLO模型进行相应目标检测。不过CVAT导出yolo格式，其标注文件夹为空。因此可以通过导出COCO格式，再根据ultralytic官方库提供的转换函数，转换为YOLO格式，此时数据集可以用于训练一个segmentation任务的YOLO模型。

但是，为了进行detection任务，可以将转换后的多边形YOLO格式（即masks）的标注文件，进一步转换问矩形YOLO格式（即boxes）的标注文件。

同时，由于数据集来源于不同的视频，因此导出、转换后，所有数据集并为进行整合，同时也存在不同视频产生的数据的文件名相同，因此需要对不同的数据进行合并，再进一步划分训练、验证、测试的数据集。

##### YOLO的数据集文件结构如下：

```bash
dataset/
├── images/
│   ├── train/
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   │   └── ...
│   ├── valid/
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   │   └── ...
│   └── test/
│       ├── image1.jpg
│       ├── image2.jpg
│       └── ...
└── labels/
    ├── train/
    │   ├── image1.txt
    │   ├── image2.txt
    │   └── ...
    ├── valid/
    │   ├── image1.txt
    │   ├── image2.txt
    │   └── ...
    └── test/
        ├── image1.txt
        ├── image2.txt
        └── ...
```



##### 文件结构

````bash
Conver_Collect_Dataset.py
├──	convert_coco_to_yolo.py
│   ├── folder_file_process.py
├── rename.py
├── convert_polygon_to_rectangle.py
├── folder_file_process.py

Split_Dataset.py
````



### 功能说明

功能实现，分为两个部分：

1. 转换数据集，并汇总到数据容器中

具体而言，在使用前，需要准备一个包含图像的COCO格式的标注数据集

其文件结构如下：

 ````bash
COCO/
├── images/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
├── annotations/
│   └── annotations.json
 ````



使用时，`Convert_Collect_Dataset.py `将调用`convert_coco_to_yolo.py `把coco路径下的annotations文件夹中的`.json`转换为YOLO需要的`.txt`文件

之后将由`rename.py` 对所有标签文件名进行修改，即增加前缀

随后`convert_polygon_to_rectangle.py`将会把多边形标注转换为矩形标注，并保存至指定的数据集容器

标签处理完成后，将对图像进行改名，同样使用了`rename.py`，增加前缀

然后，移动图像到指定的数据集容器



2. 从数据容器中读取数据并按比例划分train, valid, test数据集到指定路径

`Split_Dataset.py`将从数据集容器中读取相应文件，随机划分数据集

### 使用说明

- `Convert_Collect_Dataset.py`
  - 提供COCO格式标签数据集的根目录
  - 需要给文件改名所需的前缀
  - 数据容器的路径



- `Split_Dataset.py`
  - 给`root_path`提供数据容器的根路径
  - 指定一个保存划分好数据集饿路径 `save_path`

### 改进点
- 对于分割数据集可以增加检查目标路径是否为空，若不为空可以选择删除路径内文件后，再执行拷贝
