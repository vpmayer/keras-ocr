
import os
from dotenv import load_dotenv
load_dotenv()

pasta = os.getenv("IMG_TRAIN")
gt_file_path = os.getenv("GT_FILE_TRAIN")


def read_labels_file(labels_filepath, image_folder):
    """Read a labels file and return (filepath, label) tuples.

    Args:
        labels_filepath: Path to labels file
        image_folder: Path to folder containing images
    """
    with open(labels_filepath, encoding='utf-8-sig') as f:
        labels = [l.strip().split(',') for l in f.readlines()]
        labels = [(os.path.join(image_folder,
                                segments[0]), None, ','.join(segments[1:]).strip()[1:-1])
                  for segments in labels]
    return labels

print(pasta, gt_file_path)

data = []

data.extend(
	read_labels_file(labels_filepath=gt_file_path,image_folder=pasta))

# print(data)

# train_labels = get_traim_recognizer_dataset(split='train', cache_dir='.'):

train_labels = [(filepath, box, word.lower()) for filepath, box, word in data]

print(train_labels)