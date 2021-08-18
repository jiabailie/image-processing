from summer.tools.utils import Utils


class BmpStructHeader:
    def __init__(self):
        self.biSize = Utils.i_to_bytes(0, 4)  # bmp header size
        self.biWidth = Utils.i_to_bytes(0, 4)
        self.biHeight = Utils.i_to_bytes(0, 4)
        self.biPlanes = Utils.i_to_bytes(0, 2)  # default 1
        self.biBitCount = Utils.i_to_bytes(0, 2)  # one pixel occupy how many bits
        self.biCompression = Utils.i_to_bytes(0, 4)
        self.biSizeImage = Utils.i_to_bytes(0, 4)
        self.biXPelsPerMeter = Utils.i_to_bytes(0, 4)
        self.biYPelsPerMeter = Utils.i_to_bytes(0, 4)
        self.biClrUsed = Utils.i_to_bytes(0, 4)
        self.biClrImportant = Utils.i_to_bytes(0, 4)