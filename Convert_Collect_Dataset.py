import os
import convert_coco_to_yolo
import folder_file_process
import rename
import convert_polygon_to_rectangle

'''
This script aims to convert COCO format labels to YOLO format labels,
using convert_coco function provided by ultralytics.
    
This script also aims to convert polygon masks annotations to rectangle boxes annotations.
    
This script also can collect images and labels into one dataset container.
If new dataset has been converted, it can add into the container, to enrich the whole dataset.
'''

'''
You just need to provide the root path of COCO format dataset <root_path>
In order to avoid duplication and to easily distinguish data sources,
you need to provide a prefix, which will be added to the file name <prefix>
You also need to provide the data container path, which can add new dataset into it <data_container_path>
'''

if __name__ == '__main__':

    data_container_path = 'Dataset_container'
    root_path = 'video_78_coco'
    prefix = 'video_78_'

    # 转换COCO格式的标签，返回转换后YOLO标签所在的路径
    convert_root_path, convert_root_labels_path = convert_coco_to_yolo.coco_to_yolo(root_path)
    # 对YOLO标签改名
    rename.rename_files_in_folder(prefix=prefix, root_path=convert_root_labels_path)
    # YOLO多边形标签转换为矩形标签，并保存到数据容器
    convert_polygon_to_rectangle.process_label_directory(convert_root_labels_path, os.path.join(data_container_path, 'labels'))
    # 对图像改名
    rename.rename_files_in_folder(prefix=prefix, root_path=root_path, sub_path='images')
    # 移动图像到数据容器
    folder_file_process.move_file_to_folder(os.path.join(root_path, 'images'), os.path.join(data_container_path, 'images'))

    # 删除多余文件夹
    folder_file_process.delete_folder([root_path, convert_root_path])

