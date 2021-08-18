from bmp.tools.utils import Utils
from bmp.tools.data import MAX_PIXEL_VALUE
from bmp.base.bmp import Bmp


class BmpTransform(Bmp):
    def __init__(self):
        super().__init__()

    def calculate_pixel(self, height_index, width_index, order, operator):
        total = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_height_index = height_index + i
                new_width_index = width_index + j
                if new_height_index < 0 or new_height_index >= self.height:
                    continue
                if new_width_index < 0 or new_width_index >= self.width:
                    continue
                s_index = new_height_index * self.width_step + new_width_index
                total += int.from_bytes(self.bits[s_index + order], 'little') * operator[i + 1][j + 1]

        if total < 0:
            return 0
        if total > MAX_PIXEL_VALUE:
            return MAX_PIXEL_VALUE
        return total

    def transform(self, operator):
        if len(operator) != 3 or len(operator[0]) != 3:
            raise Exception("Please back to check operator!")

        # new pixels array
        new_bits = [b''] * self.height * self.width * self.bit_count
        for i in range(0, self.height):
            for j in range(0, self.width):
                s_index = i * self.width_step + j * self.bit_count
                b = self.calculate_pixel(i, j, 0, operator)
                g = self.calculate_pixel(i, j, 1, operator)
                r = self.calculate_pixel(i, j, 2, operator)
                new_bits[s_index] = int(b).to_bytes(1, 'little')
                new_bits[s_index + 1] = int(g).to_bytes(1, 'little')
                new_bits[s_index + 2] = int(r).to_bytes(1, 'little')
        self.bits = new_bits
