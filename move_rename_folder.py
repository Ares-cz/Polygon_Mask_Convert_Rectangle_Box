import os
import shutil

def move_folder(src, dest):
    """移动文件夹 src 到 dest 目录下，并返回新的文件夹路径"""
    try:
        # 计算新的文件夹路径
        dest_path = os.path.join(dest, os.path.basename(src))

        # 移动文件夹
        shutil.move(src, dest_path)
        print(f"文件夹 {src} 已移动到 {dest_path}")

        return dest_path
    except Exception as e:
        print(f"移动文件夹时出错: {e}")
        return None

def rename_folder(folder_path, new_name):
    """重命名 folder_path 到新名称 new_name"""
    try:
        new_path = os.path.join(os.path.dirname(folder_path), new_name)
        os.rename(folder_path, new_path)
        print(f"文件夹 {folder_path} 已重命名为 {new_name}")
    except Exception as e:
        print(f"重命名文件夹时出错: {e}")

# 需要找到原始图像的路径和需要制作数据集的标签路径

source_folder_image = "path_to_image_folder"  # 图像文件夹的路径
source_folder_label_rectangle = "path_to_label_folder"  # 标签文件夹的路径
destination_root = "path_to_direction_folder"  # 目标根目录的路径

new_folder_name = "labels"  # 新的文件夹名称，这里是'labels'

# 移动文件夹
move_folder(source_folder_image, destination_root)
folder_to_rename = move_folder(source_folder_label_rectangle, destination_root)  # 需要重命名的文件夹路径
# 重命名文件夹
rename_folder(folder_to_rename, new_folder_name)
