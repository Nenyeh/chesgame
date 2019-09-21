class Pawn:
    def __init__(self, name ):
        self.name = name

    def move_forward(self):
        pass

    def move_diagonally(self):
        pass

    def resurrect(self):
        pass

    def eats(self):
        pass


class King:
    def __init__(self, name):
        self.name = name

    def move_any_direction(self):
        pass

    def dead(self,):
        pass

    def eats(self):
        pass


class Queen:
    def __init__(self, name):
        self.name = name

    def move_vertically(self):
        pass

    def move_horizontally(self):
        pass

    def move_diagonally(self):
        pass

    def eats(self):
        pass



class Bishop:
    def __init__(self, name):
        self.name = name

    def move_diagonally(self):
        pass

    def eats(self):
        pass

class Rook:
    def __init__(self, name):
        self.name = name

    def vertical(self):
        pass
    def horizontal(self):
        pass

class Knight:
    def __init__(self, name):
        self.name=name

    def movement(self):
        pass

    def eats(self):
        pass
