import os
import shutil
from sklearn.model_selection import train_test_split

def ensure_folder_exists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def get_image_files(path, extensions):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.lower().endswith(extensions)]

def copy_files(files, src_path, dest_path):
    for file in files:
        # 复制图片
        shutil.copy2(os.path.join(src_path, file), os.path.join(dest_path, file))
        # 复制对应的标签文件
        label_file = os.path.splitext(file)[0] + '.txt'
        shutil.copy2(os.path.join(src_path.replace('images', 'labels'), label_file), os.path.join(dest_path.replace('images', 'labels'), label_file))

def split_dataset(root_path, save_path, train_size, valid_size, test_size):
    images_path = os.path.join(root_path, "images")

    # 确保保存路径的子文件夹存在
    for subset in ['train', 'valid', 'test']:
        ensure_folder_exists(os.path.join(save_path, "images", subset))
        ensure_folder_exists(os.path.join(save_path, "labels", subset))

    # 支持的图片文件扩展名
    extensions = ('.jpg', '.jpeg', '.png')

    # 获取所有图片文件名
    image_files = get_image_files(images_path, extensions)

    # 首先，从总体数据集中划分出测试集
    train_valid_files, test_files = train_test_split(image_files, test_size=test_size)
    print(len(train_valid_files))
    print(len(test_files))
    print('---------')
    # 接着，从剩余的数据集中划分出验证集
    train_files, valid_files = train_test_split(train_valid_files, test_size=valid_size / (1 - test_size))
    print(len(train_files))
    print(len(valid_files))
    print(len(test_files))
    # 复制文件到对应的文件夹
    copy_files(train_files, images_path, os.path.join(save_path, "images", 'train'))
    copy_files(valid_files, images_path, os.path.join(save_path, "images", 'valid'))
    copy_files(test_files, images_path, os.path.join(save_path, "images", 'test'))




if __name__ == '__main__':

    # 定义数据集根目录路径和保存路径
    root_path = "Dataset_container"  # 替换为你的实际源路径
    save_path = "Grape_bunch_yolo_detection_dataset"  # 替换为你的实际保存路径

    # 定义数据集划分的比例
    train_size = 0.7
    valid_size = 0.2
    test_size = 0.1

    # 执行数据集划分
    split_dataset(root_path, save_path, train_size, valid_size, test_size)
