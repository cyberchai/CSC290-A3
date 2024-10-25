class Piece:
  def __init__(self, color, piece, pattern, starting_pos):
    self.color = color
    self.piece = piece
    self.pattern = pattern
    self.starting_pos = starting_pos

  def __str__(self):
    return f"{self.color} {self.piece}"

# ex.
p1 = Piece('Black', 'r', ['f','b','l','r',1,7], '00')

print(p1)