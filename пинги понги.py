from pygame import *
from random import *
init()

game = True
window = display.set_mode((700, 500))
display.set_caption('пинг-понг')
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed=0):
        super().__init__()
        self.img = img
        self.w = w
        self.h = h
        self.speed = speed
        self.image = transform.scale(image.load(img), (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def render(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Ball(GameSprite):
    def move(self):
        if self.rect.y <= 450:
            self.rect.x += self.speed
            self.rect.y += self.speed
        if self.rect.x >= 50:
            self.rect.x -= self.speed
            self.rect.y -= self.speed
ball = Ball('ball.png', 100, 100, 50, 50, 5)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((32, 178, 170))
    clock.tick(60)
    ball.render()
    ball.move()
    display.update()