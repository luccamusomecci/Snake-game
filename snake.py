import curses
from random import randint

#Setup the window

curses.initscr()
win = curses.newwin(20, 60, 0, 0) #The 1st coord is Y, the 2nd it's X
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

#Snake and apple
snake = [(4, 10), (4,9), (4,8)]
apple = (10, 20)

win.addch(apple[0], apple[1], '#')
#Game logic

score = 0

ESC = 27
key = curses.KEY_RIGHT

while key != ESC:

    win.addstr(0, 2, 'Score ' + str(score) + ' ')
    win.timeout(150 - (len(snake)) // 5 + len(snake) // 10 % 120) # Increases the speed based on the lenght of the snake


    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key

    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key

    #Calculate the next coordinate for the snake

    y = snake[0][0]
    x = snake[0][1]
    if key  == curses.KEY_DOWN:
        y += 1
    if key  == curses.KEY_UP:
        y -= 1
    if key  == curses.KEY_LEFT:
        x -= 1
    if key  == curses.KEY_RIGHT:
        x += 1


    snake.insert(0, (y, x)) 


    #Check if we hit the border

    if y == 0: break
    if y == 19: break
    if x == 0: break
    if x == 59: break

    #If snakes runs over itself

    if snake[0] in snake[1:]: break

    if snake[0] == apple:
        #Eat the apple
        score += 1
        apple = ()
        while apple == ():
            apple = (randint(1,18), randint(1,58))
            if apple in snake:
                apple = ()
        win.addch(apple[0], apple[1], '#')
    else:
        # Move the snake
        last = snake.pop()
        win.addch(last[0], last[1], ' ')

    win.addch(snake[0][0], snake[0][1], '*')
    
curses.endwin()
print(f"Final score = {score}")