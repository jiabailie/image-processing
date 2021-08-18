import logging

from summer.tools.utils import Utils
from summer.operations.graying import Graying
from summer.operations.resize import Resizing
from summer.operations.rotating import Rotating
from summer.operations.display import Display
from summer.operations.transform import Transform
from summer.tools.data import LAPLAS_1,LAPLAS_2,LAPLAS_3,LAPLAS_4,LAPLAS_5,LAPLAS_6


def run_transform():
    source_path = '0_source/pirate_gray.jpeg.bmp'
    oper = Transform()
    logging.info("1. start to transform bmp file...")

    logging.info("2. start to transform bmp file using Laplas1...")
    oper.parse(source_path)
    oper.transform(LAPLAS_1)
    logging.info("3. start to write bmp file through Laplas1...")
    oper.generate('1_process/pirate_gray_laplas1.jpeg.bmp')

    logging.info("4. start to transform bmp file using Laplas2...")
    oper.parse(source_path)
    oper.transform(LAPLAS_2)
    logging.info("5. start to write bmp file through Laplas2...")
    oper.generate('1_process/pirate_gray_laplas2.jpeg.bmp')

    logging.info("6. start to transform bmp file using Laplas3...")
    oper.parse(source_path)
    oper.transform(LAPLAS_3)
    logging.info("7. start to write bmp file through Laplas3...")
    oper.generate('1_process/pirate_gray_laplas3.jpeg.bmp')

    logging.info("8. start to transform bmp file using Laplas4...")
    oper.parse(source_path)
    oper.transform(LAPLAS_4)
    logging.info("9. start to write bmp file through Laplas4...")
    oper.generate('1_process/pirate_gray_laplas4.jpeg.bmp')

    logging.info("10. start to transform bmp file using Laplas5...")
    oper.parse(source_path)
    oper.transform(LAPLAS_5)
    logging.info("11. start to write bmp file through Laplas5...")
    oper.generate('1_process/pirate_gray_laplas5.jpeg.bmp')

    logging.info("12. start to transform bmp file using Laplas6...")
    oper.parse(source_path)
    oper.transform(LAPLAS_6)
    logging.info("13. start to write bmp file through Laplas6...")
    oper.generate('1_process/pirate_gray_laplas6.jpeg.bmp')


def run_graying():
    oper = Graying()
    logging.info("1. start to parse bmp file...")
    oper.parse('0_source/pirate_gray.jpeg.bmp')
    logging.info("2. start to process bmp file...")
    oper.graying()
    logging.info("3. start to write bmp file...")
    oper.generate('1_process/pirate_gray.jpeg.bmp')


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s][%(filename)s][%(levelname)s]%(message)s',
        datefmt='%Y-%m-%d %A %H:%M:%S',
        filename="log/log.txt",
        filemode='a')

    run_graying()
