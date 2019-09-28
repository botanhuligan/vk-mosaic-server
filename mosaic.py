import os
import uuid
from pho_mos import create_mosaic

THIS_FILE_PATH = os.path.dirname(os.path.realpath(__file__))


def create(filename):
    name = uuid.uuid1()
    path = THIS_FILE_PATH + "/results/{0}.jpg".format(name)
    # Мы 2
    create_mosaic(
        img_path=THIS_FILE_PATH + "/downloaded/" + filename,
        source_dirs=[THIS_FILE_PATH + "/imgs/"],
        target_path=path,
        resize_factor=0.1,
        cell_size=64,
        ukrup_field_max_percent=0.2,
        not_ukrup_fields=[(0.2, 0.1, 0.6, 0.9)]
    )
    return path


if __name__ == "__main__":
    print(create("1.png"))