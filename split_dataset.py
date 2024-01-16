import os
import shutil
from sklearn.model_selection import train_test_split

def ensure_folder_exists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def get_image_files(path, extensions):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.lower().endswith(extensions)]

def move_files(files, src_path, dest_path):
    for file in files:
        # 移动图片
        shutil.move(os.path.join(src_path, file), os.path.join(dest_path, file))
        # 移动对应的标签文件
        label_file = os.path.splitext(file)[0] + '.txt'
        shutil.move(os.path.join(src_path.replace('images', 'labels'), label_file), os.path.join(dest_path.replace('images', 'labels'), label_file))

def split_dataset(root_path, train_size, valid_size, test_size):
    images_path = os.path.join(root_path, "images")
    labels_path = os.path.join(root_path, "labels")

    # 确保子文件夹存在
    for subset in ['train', 'valid', 'test']:
        ensure_folder_exists(os.path.join(images_path, subset))
        ensure_folder_exists(os.path.join(labels_path, subset))

    # 支持的图片文件扩展名
    extensions = ('.jpg', '.jpeg', '.png')

    # 获取所有图片文件名
    image_files = get_image_files(images_path, extensions)

    # 划分数据集
    train_files, test_files = train_test_split(image_files, train_size=train_size + valid_size)
    valid_files, test_files = train_test_split(test_files, train_size=valid_size / (valid_size + test_size))

    # 移动文件到对应的文件夹
    move_files(train_files, images_path, os.path.join(images_path, 'train'))
    move_files(valid_files, images_path, os.path.join(images_path, 'valid'))
    move_files(test_files, images_path, os.path.join(images_path, 'test'))

# 定义数据集根目录路径
root_path = "Grape_bunch_yolo_dataset"  # 替换为你的实际路径

# 定义数据集划分的比例
train_size = 0.7
valid_size = 0.2
test_size = 0.1

# 执行数据集划分
split_dataset(root_path, train_size, valid_size, test_size)
