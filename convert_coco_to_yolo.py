from ultralytics.data.converter import convert_coco

path = 'path_to_coco_annoatations/annotations' #  coco标签的路径

convert_coco(labels_dir=path,
             save_dir='video_79_coco_converted/',
             use_segments=True)

