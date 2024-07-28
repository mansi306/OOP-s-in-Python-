class Decoder(object):
    def __init__(self, func):  # constructor
        self.function = func

    def __call__(self, *args):  # call magic method
        try:
            if any([isinstance(i, str) for i in args]):
                raise TypeError("cannot pass string as arguments")
            else:
                return self.function(*args)  # added this line
        except Exception as obj:
            print(obj)

@Decoder
def add(*args):
    sum1 = 0
    for num in args:
        sum1 = sum1 + num
    return sum1

print(add(10, 20, 45))
print(add(10, '20', 78))
