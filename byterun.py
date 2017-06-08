class Byterun:

    def __init__(self):
        pass

    @staticmethod
    def hex_string_decompress(hex_string):

        arr = []

        i = 0
        check = False
        last = None

        for char in hex_string:

            if check:
                check = False
                continue

            arr.append(char)

            if char == last:
                check = True
                l = ord(hex_string[i + 1])
                for j in xrange(0, l):
                    arr.append(char)

                i += 2
                continue

            last = char
            i += 1

        return arr
