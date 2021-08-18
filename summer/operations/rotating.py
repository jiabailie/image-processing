import math

from summer.tools.utils import Utils
from summer.base.bmp import Bmp


class Rotating(Bmp):
    def __init__(self):
        super().__init__()

    def rotate(self):
        self.rotate_with_degree(90)

    """
    reference: http://blog.csdn.net/liyuan02/article/details/6750828
    attention: in the loop, the x in real bmp is represent y, the y same too.
    """

    def rotate_with_degree(self, degree):
        cos_degree = math.cos(math.radians(degree))
        sin_degree = math.sin(math.radians(degree))
        h = math.ceil(self.height * cos_degree
                      + self.width * sin_degree)
        w = math.ceil(self.height * sin_degree
                      + self.width * cos_degree)
        h = abs(h)
        w = abs(w)
        if w % 4 != 0:
            w -= w % 4
        dx = -0.5 * w * cos_degree - 0.5 * h * sin_degree + 0.5 * self.width
        dy = 0.5 * w * sin_degree - 0.5 * h * cos_degree + 0.5 * self.height
        new_bits = [b''] * w * h * 3
        for x in range(0, h):
            for y in range(0, w):
                x0 = y * cos_degree + x * sin_degree + dx
                y0 = -y * sin_degree + x * cos_degree + dy
                src_index = round(y0) * self.width_step + round(x0) * self.bit_count
                dst_index = x * w * self.bit_count + y * self.bit_count
                if len(self.bits) - self.bit_count > src_index >= 0:
                    new_bits[dst_index + 2] = self.bits[src_index + 2]
                    new_bits[dst_index + 1] = self.bits[src_index + 1]
                    new_bits[dst_index] = self.bits[src_index]
                else:
                    new_bits[dst_index + 2] = Utils.i_to_bytes(255, 1)
                    new_bits[dst_index + 1] = Utils.i_to_bytes(255, 1)
                    new_bits[dst_index] = Utils.i_to_bytes(255, 1)
        self.bits = new_bits
        self.biWidth = Utils.i_to_bytes(w, 4)
        self.biHeight = Utils.i_to_bytes(h, 4)
