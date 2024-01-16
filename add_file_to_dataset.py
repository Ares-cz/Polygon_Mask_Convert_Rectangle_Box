import os
import shutil

def copy_subfolder_contents(root_path, dest_root_path):
    """
    从每个子目录下的 images/ 和 labels/ 中复制文件到指定的目标根目录下的 images/ 和 labels/
    """
    # 确保目标根目录的 images/ 和 labels/ 文件夹存在
    os.makedirs(os.path.join(dest_root_path, 'images'), exist_ok=True)
    os.makedirs(os.path.join(dest_root_path, 'labels'), exist_ok=True)
    print(os.listdir(dest_root_path))
    # 遍历根目录下的每个子目录

    for subdir in os.listdir(root_path):
        subdir_path = os.path.join(root_path, subdir)
        print(subdir_path)
        if not os.path.isdir(subdir_path):
            continue
        # 复制 images 子目录中的文件
        if os.path.exists(subdir_path):
            for file in os.listdir(subdir_path):
                shutil.copy2(os.path.join(subdir_path, file), os.path.join(dest_root_path, subdir, file))


    print(f"文件已从 {root_path} 复制到 {dest_root_path} 的 images/ 和 labels/ 中")

# 示例使用
source_root_folder = "video_79_yolo_detection"  # 源根目录路径
destination_root_folder = "Grape_bunch_yolo_dataset"  # 目标根目录路径

copy_subfolder_contents(source_root_folder, destination_root_folder)
