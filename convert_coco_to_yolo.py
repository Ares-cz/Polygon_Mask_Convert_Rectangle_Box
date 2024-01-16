from ultralytics.data.converter import convert_coco

path = 'video_79_coco/annotations' #  coco标签的路径

convert_coco(labels_dir=path,
             save_dir='video_79_coco_converted/',
             use_segments=True)

