import os
from ultralytics.data.converter import convert_coco
from folder_file_process import find_folder

def coco_to_yolo (root_path):
    """
    Convert annotation files from COCO format to YOLO format.
    :param root_path: A string representing the path to the directory containing the original COCO annotations.
    :return: A tuple containing two elements:
        1. The path to the directory where converted annotations are saved.
        2. The path to the 'default' folder within the converted annotations directory,
        which is found using the `find_folder` function.

    This function assumes a directory structure where the COCO annotations
    are located in a subdirectory named 'annotations' within the provided root path.
    The converted annotations are saved in a new directory, which is named
    after the root path with '_converted' appended.
    """
    label_path = os.path.join(root_path, 'annotations')
    save_path = root_path + '_converted'
    convert_coco(labels_dir=label_path,
                 save_dir=save_path,
                 use_segments=True)
    return save_path, find_folder(save_path, 'default')

if __name__ == '__main__':
    root_path = 'video_04_COCO'
    save_path = root_path + '_converted'
    coco_to_yolo(root_path)

