import arithmetic
import geometry


def test():
	print('Square')
	print(Square.area(4))
	print(Square.side(4))
	print(Square.diagonal(4))
	print(Square.perimeter(4), '\n')
	
	print('Rectangle')
	print(Rectangle.area(4, 7))
	print(Rectangle.length(4, 7))
	print(Rectangle.width(4, 7))
	print(Rectangle.diagonal(4, 7))
	print(Rectangle.perimeter(4, 7))
