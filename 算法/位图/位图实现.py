# coding:utf-8


class Bitmap:
    def __init__(self, num_bits):
        self._num_bits = num_bits
        self._bytes = bytearray(num_bits // 8 + 1)  # 开辟字节数组空间

    def setbit(self, k):
        if k > self._num_bits or k < 1: return
        self._bytes[k // 8] |= (1 << k % 8)

    def getbit(self, k):
        if k > self._num_bits or k < 1: return
        return self._bytes[k // 8] & (1 << k % 8) != 0

    def sorted(self, k):
        if k > self._num_bits or k < 1: return
        if self._bytes[k // 8] & (1 << k % 8):
            return k


if __name__ == '__main__':
    bitmap = Bitmap(22222222222)
    bitmap.setbit(13683553547)
    bitmap.setbit(13683553446)
    bitmap.setbit(13683553245)
    bitmap.setbit(13683553243)
    bitmap.setbit(13683553544)

    for k in range(13683553000, 13683553999):
        # print(bitmap.getbit(k))
        e = bitmap.sorted(k)
        if e:
            print(e)
    print(bitmap.getbit(13683553544))
