from bmp.base.bmp import Bmp


class BmpGraying(Bmp):
    def __init__(self):
        super().__init__()

    def graying(self):
        new_bits = [b''] * self.width * self.height * self.bit_count
        for i in range(0, self.height):
            for j in range(0, self.width):
                s_index = i * self.width_step + j * self.bit_count
                target_index = i * self.width_step + j * self.bit_count
                r = int.from_bytes(self.bits[s_index + 2], 'little')
                g = int.from_bytes(self.bits[s_index + 1], 'little')
                b = int.from_bytes(self.bits[s_index], 'little')
                gray = (r * 30 + g * 59 + b * 11) / 100
                new_bits[target_index] = int(gray).to_bytes(1, 'little')
                new_bits[target_index + 1] = int(gray).to_bytes(1, 'little')
                new_bits[target_index + 2] = int(gray).to_bytes(1, 'little')
        self.bits = new_bits