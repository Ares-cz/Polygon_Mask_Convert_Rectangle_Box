import os


def rename_files_in_folder(folder_path, prefix):
    for filename in os.listdir(folder_path):
        # 构建完整的文件路径
        old_file = os.path.join(folder_path, filename)

        # 只有在文件路径确实是文件的情况下才进行操作
        if os.path.isfile(old_file):
            # 构建新的文件名
            new_file = os.path.join(folder_path, prefix + filename)

            # 重命名文件
            os.rename(old_file, new_file)


# 定义你想要的前缀
prefix = "video_0079_"

# 假设脚本与这些文件夹在同一根目录下
root_path = "video_79_yolo_detection"  # 这里替换为你的根目录路径

# 分别重命名 images 和 labels 文件夹中的文件
rename_files_in_folder(os.path.join(root_path, "images"), prefix)
rename_files_in_folder(os.path.join(root_path, "labels"), prefix)