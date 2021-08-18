import logging

from bmp.tools.utils import Utils
from bmp.operations.bmp_graying import BmpGraying
from bmp.operations.bmp_resize import BmpResizing
from bmp.operations.bmp_rotating import BmpRotating
from bmp.operations.bmp_display import BmpDisplay
from bmp.operations.bmp_transform import BmpTransform
from bmp.tools.data import LAPLAS_1,LAPLAS_2,LAPLAS_3,LAPLAS_4,LAPLAS_5,LAPLAS_6


def run_bmp_transform():
    source_path = '/Users/yangruiguo/Documents/image-lab/script/part3/0_source/pirate_gray.jpeg.bmp'
    bmp = BmpTransform()
    logging.info("1. start to transform bmp file...")

    # logging.info("2. start to transform bmp file using Laplas1...")
    # bmp.parse(source_path)
    # bmp.transform(LAPLAS_1)
    # logging.info("3. start to write bmp file through Laplas1...")
    # bmp.generate('/Users/yangruiguo/Documents/image-lab/script/part3/1_process/pirate_gray_laplas1.jpeg.bmp')
    #
    # logging.info("4. start to transform bmp file using Laplas2...")
    # bmp.parse(source_path)
    # bmp.transform(LAPLAS_2)
    # logging.info("5. start to write bmp file through Laplas2...")
    # bmp.generate('/Users/yangruiguo/Documents/image-lab/script/part3/1_process/pirate_gray_laplas2.jpeg.bmp')
    #
    # logging.info("6. start to transform bmp file using Laplas3...")
    # bmp.parse(source_path)
    # bmp.transform(LAPLAS_3)
    # logging.info("7. start to write bmp file through Laplas3...")
    # bmp.generate('/Users/yangruiguo/Documents/image-lab/script/part3/1_process/pirate_gray_laplas3.jpeg.bmp')
    #
    # logging.info("8. start to transform bmp file using Laplas4...")
    # bmp.parse(source_path)
    # bmp.transform(LAPLAS_4)
    # logging.info("9. start to write bmp file through Laplas4...")
    # bmp.generate('/Users/yangruiguo/Documents/image-lab/script/part3/1_process/pirate_gray_laplas4.jpeg.bmp')

    logging.info("10. start to transform bmp file using Laplas5...")
    bmp.parse(source_path)
    bmp.transform(LAPLAS_5)
    logging.info("11. start to write bmp file through Laplas5...")
    bmp.generate('/Users/yangruiguo/Documents/image-lab/script/part3/1_process/pirate_gray_laplas5.jpeg.bmp')

    logging.info("12. start to transform bmp file using Laplas6...")
    bmp.parse(source_path)
    bmp.transform(LAPLAS_6)
    logging.info("13. start to write bmp file through Laplas6...")
    bmp.generate('/Users/yangruiguo/Documents/image-lab/script/part3/1_process/pirate_gray_laplas6.jpeg.bmp')


def run_bmp_graying():
    bmp = BmpGraying()
    logging.info("1. start to parse bmp file...")
    bmp.parse('/Users/yangruiguo/Documents/image-lab/script/part3/0_source/pirate_gray.jpeg.bmp')
    logging.info("2. start to process bmp file...")
    bmp.graying()
    logging.info("3. start to write bmp file...")
    bmp.generate('/Users/yangruiguo/Documents/image-lab/script/part3/1_process/pirate_gray.jpeg.bmp')


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s][%(filename)s][%(levelname)s]%(message)s',
        datefmt='%Y-%m-%d %A %H:%M:%S',
        filename="/Users/yangruiguo/Documents/image-lab/script/part3/log/log.txt",
        filemode='a')

    run_bmp_transform()
