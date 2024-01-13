import pgzrun

WIDTH = 640
HEIGHT = 480

player_left = Rect(20, 20, 20, 50)
player_right = Rect(WIDTH - 20 - 20, 20, 20, 50)
ball = Rect(WIDTH/2, HEIGHT / 2, 20, 20)

y_speed = 4
x_speed = 4

def update():
    global y_speed, x_speed
    ball.y += y_speed
    ball.x += x_speed
   
    if (ball.bottom > HEIGHT or ball.top < 0):
      y_speed=-y_speed
    if (ball.left<0 or ball.right>WIDTH):
      x_speed = -x_speed
    if (ball.colliderect(player_left) or ball.colliderect(player_right)):
      x_speed = -x_speed

    if keyboard.w:
        player_left.y -= 4
    if keyboard.s:
        player_left.y += 4

    if player_left.top < 0:
        player_left.top = 0
    if player_left.bottom > HEIGHT:
        player_left.bottom = HEIGHT

    if keyboard.up:
        player_right.y -= 4
    if keyboard.down:
        player_right.y += 4

    if player_right.top < 0:
        player_right.top = 0
    if player_right.bottom > HEIGHT:
        player_right.bottom = HEIGHT




    
def draw():
    screen.clear( )
    screen.draw.filled_rect(player_left, 'white')
    screen.draw.filled_rect(player_right, 'white')
    screen.draw.filled_rect(ball, 'white')

pgzrun.go()
