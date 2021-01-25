# Unpacking

# Unpack first element, ignore other
a, _ = (1, 2)
print(a)

# b, c, *d = (1, 2, 3, 4, 5)
b, c, *_ = (1, 2, 3, 4, 5)
print(b)
print(c)

# e, f, *e, h = (1, 2, 3, 4, 5, 6)
e, f, *_, h = (1, 2, 3, 4, 5, 6)