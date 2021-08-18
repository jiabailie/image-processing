import logging


class Utils:
    @staticmethod
    def i_to_bytes(number, length, byteorder='little'):
        return number.to_bytes(length, byteorder)

    @staticmethod
    def bytes_to_i(mbytes, byteorder='little'):
        return int.from_bytes(mbytes, byteorder)

    @staticmethod
    def config_log():
        logger = logging.getLogger();
        logger.setLevel('DEBUG');
        formatter = logging.Formatter(
            fmt='[%(asctime)s][%(filename)s][%(levelname)s]%(message)s',
            datefmt='%Y-%m-%d %A %H:%M:%S')

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel("INFO")
        logger.addHandler(console_handler)

        file_handler = logging.FileHandler(filename='log/log.txt', mode='a')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)