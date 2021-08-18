class Utils:
    @staticmethod
    def i_to_bytes(number, length, byteorder='little'):
        return number.to_bytes(length, byteorder)

    @staticmethod
    def bytes_to_i(mbytes, byteorder='little'):
        return int.from_bytes(mbytes, byteorder)