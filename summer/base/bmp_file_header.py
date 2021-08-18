from summer.tools.utils import Utils


class BmpFileHeader:
    def __init__(self):
        self.bfType = Utils.i_to_bytes(0, 2)  # BM
        self.bfSize = Utils.i_to_bytes(0, 4)  # file size
        self.bfReserved1 = Utils.i_to_bytes(0, 2)
        self.bfReserved2 = Utils.i_to_bytes(0, 2)
        self.bfOffBits = Utils.i_to_bytes(0, 4)  # header info offset
