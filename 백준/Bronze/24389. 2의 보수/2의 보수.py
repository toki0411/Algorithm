N = int(input())
tmp = (N ^ ((1 << 32) - 1)) + 1
print((N ^ tmp).bit_count())
