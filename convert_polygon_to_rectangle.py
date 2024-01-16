import os
import glob

# 基于 convert_coco_to_yolo.py 中的返回路径
# 设置原始标签文件夹和保存修改后的标签的文件夹
original_labels_folder = 'path_to_source_annotations_folder'  # 用户提供的原始标签文件夹路径
save_folder = 'path_to_save_annotation_folder'  # 用户应该替换为自己的保存文件夹路径

# 确保保存文件夹存在
os.makedirs(save_folder, exist_ok=True)

# 读取原始标签文件夹中的所有txt文件
label_files = glob.glob(os.path.join(original_labels_folder, '*.txt'))


# 定义计算矩形边界框的函数
def calculate_bounding_box(polygon):
    min_x = min([point[0] for point in polygon])
    max_x = max([point[0] for point in polygon])
    min_y = min([point[1] for point in polygon])
    max_y = max([point[1] for point in polygon])

    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2
    width = max_x - min_x
    height = max_y - min_y

    return center_x, center_y, width, height


# 遍历每个文件，进行转换，并保存
for label_file in label_files:
    with open(label_file, 'r') as file:
        yolo_polygon_labels = file.readlines()

    yolo_rectangular_labels = []

    for label in yolo_polygon_labels:
        label_parts = label.strip().split(' ')
        category, points = label_parts[0], label_parts[1:]
        polygon_points = [(float(points[i]), float(points[i + 1])) for i in range(0, len(points), 2)]

        # 计算矩形边界框
        center_x, center_y, width, height = calculate_bounding_box(polygon_points)

        # 创建新的YOLO格式标签
        yolo_rectangular_labels.append(f"{category} {center_x} {center_y} {width} {height}")

    # 构建保存路径，并保存修改后的文件
    save_path = os.path.join(save_folder, os.path.basename(label_file))
    with open(save_path, 'w') as file:
        for label in yolo_rectangular_labels:
            file.write(label + '\n')

# 执行完成后的提示
print("所有标签文件已转换并保存到指定文件夹。")
