from bmp.tools.utils import Utils
from bmp.base.bmp import Bmp


class BmpResizing(Bmp):
    def __init__(self):
        super().__init__()

    # nearest_neighbor Interpolation
    def resize(self, width, height):
        # width must be Multiple of four
        if width % 4 != 0:
            width -= width % 4
        h_ratio = (self.height / height)
        w_ratio = (self.width / width)

        # new pixels array
        new_bits = [b''] * height * width * self.bit_count
        for row in range(0, height):
            for col in range(0, width):
                for channel in range(0, self.bit_count):
                    old_r = round((row + 0.5) * h_ratio - 0.5)
                    old_c = round((col + 0.5) * w_ratio - 0.5)
                    new_index = row * width * self.bit_count + col * self.bit_count + channel
                    old_index = old_r * self.width_step + old_c * self.bit_count + channel
                    new_bits[new_index] = self.bits[old_index]
        self.bits = new_bits

        # reset header info
        self.bfSize = Utils.i_to_bytes(height * width * self.bit_count + 54, 4)
        self.biSizeImage = Utils.i_to_bytes(len(new_bits), 4)
        self.biWidth = Utils.i_to_bytes(width, 4)
        self.biHeight = Utils.i_to_bytes(height, 4)