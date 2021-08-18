from bmp.tools.utils import Utils
from bmp.base.bmp import Bmp


class BmpDisplay(Bmp):
    def __init__(self):
        super().__init__()

    def display_rgb(self):
        out_file_path = "/Users/yangruiguo/Documents/image-lab/script/part3/1_process/pirate.txt"
        with open(out_file_path, "w") as out:
            for i in range(0, self.height):
                for j in range(0, self.width):
                    s_index = i * self.width_step + j * self.bit_count
                    r = int.from_bytes(self.bits[s_index + 2], 'little')
                    g = int.from_bytes(self.bits[s_index + 1], 'little')
                    b = int.from_bytes(self.bits[s_index], 'little')

                    cell = '({r},{g},{b})'.format(r=r,g=g,b=b)
                    out.write("{c}\t".format(c=cell))
                out.write("\n")