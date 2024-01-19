import os

def rename_files_in_folder(prefix, root_path, sub_path=None):
    """
    Rename all files in a specified directory by adding a prefix to their names.

    This function iterates over all files in a given directory (and optionally a subdirectory) and renames them by
    prefixing their current names with a specified string. This is useful for batch renaming of files for organization
    or clarity.

    :param prefix: String to be added as a prefix to each file name in the directory.
    :param root_path: String representing the path to the root directory containing the files to be renamed.
    :param sub_path: Optional string representing the path to a subdirectory within the root directory. If provided,
                     only files within this subdirectory will be renamed. If None, files directly in the root directory
                     will be renamed.
    :return: None. The function prints a confirmation message upon successfully renaming all files.
    """
    folder_path = root_path if sub_path is None else os.path.join(root_path, sub_path)

    for filename in os.listdir(folder_path):
        # Create a completed path to access the file
        old_file = os.path.join(folder_path, filename)

        if os.path.isfile(old_file):
            # Create new file name
            new_file = os.path.join(folder_path, prefix + filename)

            # Rename the file
            os.rename(old_file, new_file)
    print(f"Files in the folder '{folder_path}' have been renamed by adding prefix '{prefix}'.")

if __name__ == '__main__':
    # 定义你想要的前缀
    prefix = "video_0079_"

    # 假设脚本与这些文件夹在同一根目录下
    root_path = "video_79_yolo_detection"  # 这里替换为你的根目录路径

    # 分别重命名 images 和 labels 文件夹中的文件
    rename_files_in_folder(root_path, 'images', prefix)
    rename_files_in_folder(root_path, 'labels', prefix)
