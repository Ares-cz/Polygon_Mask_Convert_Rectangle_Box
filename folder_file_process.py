import shutil
import os

# 用于移动文件
def move_file_to_folder (source_folder, destination_folder):
    """
    Move every file from source folder to destination folder

    :param source_folder: The path of folder contains files need to be moved.
    :param destination_folder: The path of folder where will accept moved files.
    :return: None. However, a confirmation message is printed after all files have been moved.

    Note:
    This function does not return a value. It prints a confirmation message to the console.
    The function assumes that the provided paths are valid and the program has the necessary permissions.
    """

    os.makedirs(destination_folder, exist_ok=True)

    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)

        if os.path.isfile(file_path):
            shutil.move(file_path, destination_folder)

    print(f"Files in folder '{source_folder}' have been moved to folder '{destination_folder}'.")

# 用于找到coco转yolo后的yolo标签所在路径
def find_folder(root_folder, sub_folder):
    """
    Searches for a specific sub-folder within a given root folder and its sub folder.
    :param root_folder: The path of the root folder where the search will begin.
    :param sub_folder: The name of the sub-folder to search for.
    :return: The full path to the found sub-folder. Returns None if the sub-folder is not found.

    This function traverses all sub folder of the specified root folder using os.walk.
    It checks each directory to see if it contains a sub folder with the specified name.
    If such a sub-folder is found, the function returns its full path. If the sub-folder
    cannot be found in any of the sub folder, the function returns None.
    """

    for dirpath, dirnames, filename in os.walk(root_folder):
        if sub_folder in dirnames:
            return os.path.join(dirpath, sub_folder)

    return None


def delete_folder(folder_paths):
    """
    Deletes the specified folder(s).
    :param folder_paths: A single string representing a folder path, or a list of strings
                        representing multiple folder paths to be deleted.
    :return:  None. However, it prints a confirmation message for each folder deleted,
                or a message if a folder does not exist.

    This function takes a single folder path or a list of folder paths.
    It checks each path and, if the folder exists, deletes it along with all its contents.
    If a specified folder does not exist, a message is printed to indicate this.
    """
    # if folder_paths is not a list，will transfer it to a list
    if not isinstance(folder_paths, list):
        folder_paths = [folder_paths]

    # Traverse all provided paths
    for path in folder_paths:
        # Check if the folder exists
        if os.path.exists(path):
            # delete folder
            shutil.rmtree(path)
            print(f"Folder '{path}' has been deleted.")
        else:
            print(f"Folder '{path}' does not exist.")

    print(f"'{folder_paths}' deleted done!")
