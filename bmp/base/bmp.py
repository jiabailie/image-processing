from bmp.tools.utils import Utils
from bmp.base.bmp_file_header import BmpFileHeader
from bmp.base.bmp_struct_header import BmpStructHeader


class Bmp(BmpFileHeader, BmpStructHeader):
    def __init__(self):
        BmpFileHeader.__init__(self)
        BmpStructHeader.__init__(self)
        self.__bitSize = 0  # pixels size
        self.bits = []  # pixel array

    @property
    def width(self):
        return Utils.bytes_to_i(self.biWidth)

    @property
    def height(self):
        return Utils.bytes_to_i(self.biHeight)

    # unit is byte
    @property
    def bit_count(self):
        return Utils.bytes_to_i(self.biBitCount) // 8

    @property
    def width_step(self):
        return self.bit_count * self.width

    # resolve a bmp file
    def parse(self, file_name):
        file = open(file_name, 'rb')

        # BmpFileHeader
        self.bfType = file.read(2)
        self.bfSize = file.read(4)
        self.bfReserved1 = file.read(2)
        self.bfReserved2 = file.read(2)
        self.bfOffBits = file.read(4)

        # BmpStructHeader
        self.biSize = file.read(4)
        self.biWidth = file.read(4)
        self.biHeight = file.read(4)
        self.biPlanes = file.read(2)
        self.biBitCount = file.read(2)

        # pixel size
        self.__bitSize = self.width * self.height * self.bit_count
        self.biCompression = file.read(4)
        self.biSizeImage = file.read(4)
        self.biXPelsPerMeter = file.read(4)
        self.biYPelsPerMeter = file.read(4)
        self.biClrUsed = file.read(4)
        self.biClrImportant = file.read(4)

        #  load pixel info
        count = 0
        while count < self.__bitSize:
            bit_count = 0
            while bit_count < (int.from_bytes(self.biBitCount, 'little') // 8):
                self.bits.append(file.read(1))
                bit_count += 1
            count += 1
        file.close()

    def generate(self, file_name):
        file = open(file_name, 'wb+')
        # reconstruct File Header
        file.write(self.bfType)
        file.write(self.bfSize)
        file.write(self.bfReserved1)
        file.write(self.bfReserved2)
        file.write(self.bfOffBits)

        # reconstruct bmp header
        file.write(self.biSize)
        file.write(self.biWidth)
        file.write(self.biHeight)
        file.write(self.biPlanes)
        file.write(self.biBitCount)
        file.write(self.biCompression)
        file.write(self.biSizeImage)
        file.write(self.biXPelsPerMeter)
        file.write(self.biYPelsPerMeter)
        file.write(self.biClrUsed)
        file.write(self.biClrImportant)

        # reconstruct pixels
        for bit in self.bits:
            file.write(bit)
        file.close()

