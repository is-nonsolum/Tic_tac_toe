import turtle

window = turtle.Screen()
window.title('Tic-Tac-Toe')
player1 = window.textinput('Player 1', "what is the name of first player?")
player2 = window.textinput("player 2", "What is the name of second player?")
window.setup(1.0, 1.0)
window.bgcolor('black')
Board = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]


# for making lines of the board
def make_line(length=300):
    line = turtle.Turtle()
    line.speed(0)
    line.hideturtle()
    line.begin_poly()
    line.up()
    line.bk(length / 2)
    line.down()
    line.fd(length)
    line.end_poly()
    line.clear()
    line = line.get_poly()
    window.register_shape('Line', line)


# finalising the board
def create_board(length=300, hx=0, hy=0, spacing=100):
    """Indexing starts from top-left corner"""
    make_line(length=length)
    var = length / 2 - spacing
    vertices = [(hx - var, hy + var), (hx + var, hy + var), (hx + 3 * var, hy + var),
                (hx - var, hy + var - spacing), (hx + var, hy + var - spacing), (hx + 3 * var, hy + var - spacing),
                (hx - var, hy - 2 * spacing + var), (hx + var, hy - 2 * spacing + var),
                (hx + 3 * var, hy - 2 * spacing + var)]
    centres = [(cord[0] - 50, cord[1] + 50) for cord in vertices]
    board = turtle.Turtle()
    board.color('blue')
    board.shape('Line')
    board.speed(0)
    board.penup()
    board.goto(hx, hy)
    board.bk(var)
    board.stamp()
    board.fd(spacing)
    board.stamp()
    board.bk(var)
    board.seth(90)
    board.fd(var)
    board.stamp()
    board.bk(spacing)
    return vertices, centres


# returns index of the vertex
def shortest_distance(x1, y1, coords):
    distance = [((x1 - coord[0]) ** 2 + (y1 - coord[1]) ** 2) ** 0.5 for coord in coords]
    return distance.index(min(distance))


# creates a circle inside one of the boxes
def makecircle(x1, y1, spacing=100):
    diam = 0.90 * spacing
    x1 -= 0.20 * spacing
    y1 += 0.20 * spacing
    temp = turtle.Turtle()
    temp.color('green')
    temp.speed(0)
    temp.hideturtle()
    temp.seth(45)
    temp.up()
    temp.goto(x1, y1)
    temp.down()
    temp.circle(diam / 2)


# creates a cross inside one of the boxes
def makecross(x1, y1, spacing=100):
    diam = 0.90 * spacing
    x1 -= 0.20 * spacing
    y1 += 0.20 * spacing
    temp = turtle.Turtle()
    temp.color("red")
    temp.speed(0)
    temp.hideturtle()
    temp.up()
    temp.goto(x1, y1)
    temp.down()
    temp.seth(135)
    temp.fd(diam)
    temp.bk(diam / 2)
    temp.setheading(45)
    temp.bk(diam / 2)
    temp.fd(diam)


def play(x, y, coords, verts):
    global turn
    ix = shortest_distance(x, y, coords)
    x, y = verts[ix]
    if turn < 9 and not check_winner()[0]:
        if turn % 2 == 0:
            makecircle(x, y)
            turn += 1
            Board[ix] = 0
        else:
            makecross(x, y)
            turn += 1
            Board[ix] = 1
    if check_winner()[0]:
        temp = turtle.Turtle()
        temp.speed(0)
        temp.hideturtle()
        temp.color('yellow')
        if check_winner()[1] == 0:
            temp.shape('Line')
            temp.setheading(90)
            temp.penup()
            temp.goto(coords[1])
            temp.stamp()
        elif check_winner()[1] == 1:
            temp.shape('Line')
            temp.setheading(90)
            temp.penup()
            temp.goto(coords[4])
            temp.stamp()
        elif check_winner()[1] == 2:
            temp.shape('Line')
            temp.setheading(90)
            temp.penup()
            temp.goto(coords[7])
            temp.stamp()
        elif check_winner()[1] == 3:
            temp.shape('Line')
            temp.setheading(45)
            temp.penup()
            temp.goto(coords[4])
            temp.stamp()
        elif check_winner()[1] == 4:
            temp.shape('Line')
            temp.setheading(135)
            temp.penup()
            temp.goto(coords[4])
            temp.stamp()
        elif check_winner()[1] == 5:
            temp.shape('Line')
            temp.penup()
            temp.goto(coords[3])
            temp.stamp()
        elif check_winner()[1] == 6:
            temp.shape('Line')
            temp.penup()
            temp.goto(coords[4])
            temp.stamp()
        elif check_winner()[1] == 7:
            temp.shape('Line')
            temp.penup()
            temp.goto(coords[5])
            temp.stamp()


def check_winner():
    found_winner = False
    index = None
    if Board[0] == Board[1] == Board[2]:
        found_winner = True
        index = 0
    elif Board[3] == Board[4] == Board[5]:
        found_winner = True
        index = 1
    elif Board[6] == Board[7] == Board[8]:
        found_winner = True
        index = 2
    elif Board[0] == Board[4] == Board[8]:
        found_winner = True
        index = 3
    elif Board[2] == Board[4] == Board[6]:
        found_winner = True
        index = 4
    elif Board[0] == Board[3] == Board[6]:
        found_winner = True
        index = 5
    elif Board[1] == Board[4] == Board[7]:
        found_winner = True
        index = 6
    elif Board[2] == Board[5] == Board[8]:
        found_winner = True
        index = 7
    return found_winner, index


pla1 = turtle.Turtle()
pla2 = turtle.Turtle()
midname = turtle.Turtle()
midname.hideturtle()
midname.up()
pla1.hideturtle()
pla2.hideturtle()
pla1.penup()
pla2.up()
pla1.color('pink')
pla2.color("purple")
midname.color("red")
pla1.goto(-100, 300)
pla2.goto(100, 300)
midname.sety(300)
midname.write("VS", align="left", move=True, font=('italic', 20, 'normal'))
pla1.write(player1, align="left", move=True, font=('italic', 20, 'normal'))
pla2.write(player2, align='left', move=True, font=('italic', 20, 'normal'))
vertex, centers = create_board()
turn = 0
window.listen()
window.onclick(lambda x, y: play(x, y, centers, vertex))
window.mainloop()
