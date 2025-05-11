from pygame import *
from random import randint


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.x < win_height - 80:
            self.rect.y += self.speed     
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 620:
            self.rect.y += self.speed   

win_width = 700
win_height = 500
red = (255, 160, 122)
window = display.set_mode((win_width, win_height))
# clock = pygame.time.Clock()
window.fill(red)
display.set_caption('ping pong')

ship = Player('kotik1.png', 30, 200, 130, 150, 7)
ship2 = Player('kotik2.png', 550, 200, 130, 150, 7)
ball = GameSprite('ball.png', 200, 200, 50, 50, 50)

clock = time.Clock()
FPS = 60

speed_x = 3
speed_y = 3

font.init()
font1 = font.SysFont('Arial', 32)
lose1 = font1.render('PLAYER 1 LOSE! PLAYER 2 WIN!', True, (255, 215, 0))
lose2 = font1.render('PLAYER 2 LOSE! PLAYER 1 WIN!', True, (255, 215, 0))

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if not finish:
        window.fill(red)
        ship.update_l()
        ship2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(ship, ball) or sprite.collide_rect(ship2, ball):
            speed_x *= -1
            speed_y *+ 1

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))
            game_over = True

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200,200))
            game_over = True



  
        ship.draw()
        ship2.draw()
        ball.draw()
        time.delay(50)
        

        
    display.update()
    clock.tick(40)


