class Cell:

    def __init__(self, value, row, column, size, editable = True):
        self.value = value
        self.row = row
        self.col = column
        self.size = size
        self.edit = editable
        self.selected = False

    def draw(self, surface, font):
        """
        Draw cells of the sudoku board.
        """
        x = self.col * self.size
        y = self.row * self.size


