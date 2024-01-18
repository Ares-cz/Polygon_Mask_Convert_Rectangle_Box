# Convert_COCO_to_YOLO_Convert_Polygon_to_Rectangle_Split_dataset

# 标注数据处理流程

### 简介

由于项目需要，使用CVAT进行标注，使用多边形进行标注，为了获取MOTS算法所需的标注文件。但是，仍需要使用YOLO模型进行相应目标检测。不过CVAT导出yolo格式，其标注文件夹为空。因此可以通过导出COCO格式，再根据ultralytic官方库提供的转换函数，转换为YOLO格式，此时数据集可以用于训练一个segmentation任务的YOLO模型。

但是，为了进行detection任务，可以将转换后的多边形YOLO格式（即masks）的标注文件，进一步转换问矩形YOLO格式（即boxes）的标注文件。

同时，由于数据集来源于不同的视频，因此导出、转换后，所有数据集并为进行整合，同时也存在不同视频产生的数据的文件名相同，因此需要对不同的数据进行合并，再进一步划分训练、验证、测试的数据集。

YOLO的数据集文件结构如下：

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


### 具体流程

1. 从CAVT标注后下载COCO数据集，可以得到json格式的标注信息；下载MOTS数据集，可以得到instance格式的标注信息
   - 使用`convert_coco_to_yolo.py`
   - 将coco数据集转换为yolo数据集，转换后得到`/labels`文件夹下的`.txt`文件

2. 对于YOLO检测（这里考虑矩形标注下的detection任务）

   - 使用`convert_polygon_to_rectangle.py`
   - 将多边形masks转换为矩形boxes，存放包含boxes的文件夹命在`/labels`后存在后缀，以便与masks的`/labels`文件夹区分
3. 对于文件夹的移动和重命名
   - 由于images存在于coco数据集中，labels存在于转换后的yolo数据集中，因此需要将其移动到一起，使用`move_rename_folder.py`
   - 将`/images`和`/lables`移动到一起，含有后缀的boxes的`/labels`文件夹，重命名为`/labels`
   - 移动后，需要对images和labels文件夹内的所有文件进行重命名，以便于汇总后，与其他数据集来源的数据进行区分。这里的做法是添加包含视频名称的前缀，使用`rename.py`
   - 在数据重命名后，需要将所有数据汇总到一起。这里采用的方法是新建一个根文件夹，并将需要汇总的数据添加到这里，这样做可以提高后续数据集的可扩展性，使用`add_file_to_dataset.py`
4. 对数据集进行划分
   - 这里将在step 3中最后汇总数据的文件夹内，划分数据集。
   - 其可以自行调整`train`，`valid`，`test`的比例


### 需要完善功能

1. 将数据集划分在另一个空间内，这样保持数据汇总的目录下可以扩充数据集。
2. 仍需要对整体流程进行优化，减少数据重复，以及避免多次生成文件夹。


--------------------------------------------------------------
### Brief script introduction
#### Convert_COCO_to_YOLO
   - convert_coco_to_yolo.py

#### Convert_Polygon_to_Rectangle_labels
   - convert_polygon_to_rectangle.py

#### Split_dataset
   - move_rename_folder.py
   - rename.py
   - add_file_to_dataset.py
   - split_dataset.py
