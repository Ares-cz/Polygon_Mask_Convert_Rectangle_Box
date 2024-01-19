import os
import glob

# 定义计算矩形边界框的函数
def calculate_bounding_box(polygon):
    """
    Calculate the bounding box for a given polygon.

    This function takes a polygon, represented as a list of (x, y) tuples, and calculates the bounding box that
    completely encloses the polygon. The bounding box is represented by the center coordinates (x, y), the width,
    and the height.

    :param polygon: A list of (x, y) tuples representing the vertices of the polygon.
    :return: A tuple (center_x, center_y, width, height), where:
             - center_x is the x-coordinate of the bounding box center.
             - center_y is the y-coordinate of the bounding box center.
             - width is the width of the bounding box.
             - height is the height of the bounding box.
    """

    # Find the minimum and maximum x-coordinate and y-coordinate
    min_x = min([point[0] for point in polygon])
    max_x = max([point[0] for point in polygon])
    min_y = min([point[1] for point in polygon])
    max_y = max([point[1] for point in polygon])

    # Calculate the center coordinates of the bounding box
    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2
    # Calculate the width and height of the bounding box
    width = max_x - min_x
    height = max_y - min_y

    return center_x, center_y, width, height

# 定义处理单个标签文件的函数
def process_label_file(label_file, save_folder):
    """
    Process a single label file by converting polygon annotations to YOLO-compatible rectangular bounding box format.

    This function reads a label file where each line represents an object's annotation in a polygon format.
    It converts these annotations to a rectangular bounding box format that is compatible with YOLO object detection models.
    The converted labels are then saved in a specified folder.

    :param label_file: String representing the path to the label file that needs to be processed.
    :param save_folder: String representing the path to the folder where the processed label file will be saved.
    :return: None. The converted label file is saved in the specified folder.
    """

    # Read the original label file with polygon annotations
    with open(label_file, 'r') as file:
        yolo_polygon_labels = file.readlines()

    # Initialize a list to store the converted rectangular bounding box labels
    yolo_rectangular_labels = []

    # Process each label in the file
    for label in yolo_polygon_labels:
        label_parts = label.strip().split(' ')
        category, points = label_parts[0], label_parts[1:]
        polygon_points = [(float(points[i]), float(points[i + 1])) for i in range(0, len(points), 2)]

        # Calculate the bounding of boxes
        center_x, center_y, width, height = calculate_bounding_box(polygon_points)

        # Create new YOLO rectangular labels
        yolo_rectangular_labels.append(f"{category} {center_x} {center_y} {width} {height}")

    # Create save path, and save the file
    save_path = os.path.join(save_folder, os.path.basename(label_file))
    with open(save_path, 'w') as file:
        for label in yolo_rectangular_labels:
            file.write(label + '\n')

# Process the whole directory
def process_label_directory(original_labels_folder, save_folder):
    """
    Process and convert all label files in a specified directory from polygon
    to rectangular bounding box format.

    This function iterates over all label files in a given directory, each of
    which contains annotations in a polygon format.
    It converts these polygon annotations to a YOLO-compatible rectangular
    bounding box format and saves the converted labels to a new specified directory.

    :param original_labels_folder: String representing the path to the directory containing the original label files.
                                   Each label file is expected to contain polygon annotations for an image.
    :param save_folder: String representing the path to the directory where the converted label files will be saved.
                        This directory will be created if it does not already exist.
    :return: None. The function prints a confirmation message upon successfully processing all files.
    """
    # Ensure the folder exist
    os.makedirs(save_folder, exist_ok=True)

    # Read all txt files in the original label folder
    label_files = glob.glob(os.path.join(original_labels_folder, '*.txt'))

    for label_file in label_files:
        process_label_file(label_file, save_folder)

    print(f"All label files have been converted and saved to the specified folder '{save_folder}'.")

if __name__ == '__main__':
    # 使用示例
    original_labels_folder = 'video_78_coco_converted/labels/default'  # 用户提供的原始标签文件夹路径
    save_folder = 'video_78_coco_converted/labels_rectangle'  # 用户应该替换为自己的保存文件夹路径

    process_label_directory(original_labels_folder, save_folder)
