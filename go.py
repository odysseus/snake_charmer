class BoardError(Exception):
    pass


class GoVertex(object):
    def __init__(self):
        self.x_position = None
        self.y_position = None
        self.contents = None

    def __str__(self):
        if self.contents is not None:
            if self.contents == "white":
                return "* "
            else:
                return "o "
        else:
            return ". "


class Goban(object):
    def __init__(self, size):
        if size % 2 == 0:
            raise BoardError("Board sizes must be odd numbers")
        elif size > 35:
            raise BoardError("Board sizes greater than 35 are not supported")
        else:
            vals = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            self.base_values = list(vals[:size])
            self.size = size
            self.board = [GoVertex() for _ in range(size * size)]
            # Using the array approach:
            # East Stone: index + 1
            # West Stone: index - 1
            # North Stone: index - size
            # South Stone: index + size

    def position_tuple_for_index(self, index):
        x = self.base_values[index % self.size]
        y = self.base_values[index // self.size]
        return x, y

    def index_from_position_tuple(self, position):
        x = self.base_values.index(position[0])
        y = self.base_values.index(position[1])
        return y * self.size + x

    def __str__(self):
        s = ""
        for i in range(len(self.board)):
            if i % self.size == 0:
                s += "\n"
            s += str(self.board[i])
        s += "\n"
        return s


def go_main():
    size = 9
    b = Goban(size)
    print(b)
