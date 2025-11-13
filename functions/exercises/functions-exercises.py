# Part 1 A -- Make a Line
def make_line(size):
        return ('#' * size)

print(make_line(5))
# Part 1 B -- Make a Square
# create a function using your make_line function to code a square
def make_square(size): 
    square = ''
    for i in range(size):
        square += '\n' + make_line(size)
    return (square)

print(make_square(5))

# Part 1 C -- Make a Rectangle

def make_rectangle(width, height): 
    rectangle = ''
    for i in range(height):
        rectangle += '\n' + make_line(width)
    return (rectangle)

print(make_rectangle(5, 3))

# Part 1.4  -- Rewrite make_square to use make_rectangle.

def make_square_2(size): 
    square_2 = make_rectangle(size, size)
    return (square_2)

print(make_square_2(5))

# Part 2 A -- Make a Stairs

def make_downward_stairs(height):
    stairs = ''
    for i in range(1, height+1):
        stairs += make_line(i) + '\n'
    return stairs

print(make_downward_stairs(5))

# Part 2 B -- Make Space-Line 

def make_space_line(numSpaces, numChars):
    return (' ' * numSpaces) + make_line(numChars) + (' ' * numSpaces)

print(make_space_line(3, 5))


# Part 2 C -- Make Isosceles Triangle

def make_isosceles_triangle(height):
    triangle = ''
    for i in range(height):
        numSpaces = height - i - 1
        num_hashes = 2 * i + 1
        triangle += make_space_line(numSpaces, num_hashes) + '\n'
    return triangle

print(make_isosceles_triangle(5))


# Part 3 -- Make a Diamond

def make_diamond(height):
    diamond = ''
    for i in range(height):
        num_spaces = height - i - 1
        num_hashes = 2 * i + 1
        diamond += ' ' * num_spaces + '#' * num_hashes + '\n'
    for i in range(height - 2, -1, -1):
        num_spaces = height - i - 1
        num_hashes = 2 * i + 1
        diamond += ' ' * num_spaces + '#' * num_hashes + '\n'
    return diamond

print(make_diamond(5))



