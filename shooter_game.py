from pygame import *
scr = display.set_mode((700,500))
display.set_caption("shyter")
galaxy = transform.scale(image.load("galaxy.jpg"), (700,500))
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
kick = mixer.Sound('fire.ogg')
kick.play()
game = True
clock = time.Clock()
FPS = 60
lose = False
win = False


class obiekt(sprite.Sprite):
    def __init__(self, picimage, sx,sy, sspeed):
        super().__init__()
        self.image = transform.scale(image.load(picimage),(65,65))
        self.speed = sspeed
        self.rect = self.image.get_rect()
        self.rect.x = sx
        self.rect.y = sy
    def reset(self):
        scr.blit(self.image, (self.rect.x,self.rect.y))

geroi = obiekt("bullet.png", 5, 600, 12)


class igrok(obiekt):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT]:
            self.rect.x -=5
        if keys_pressed[K_RIGHT]:
            self.rect.x +=5
        if keys_pressed[K_SPACE]:
            b.rect.x = self.rect.x
            b.rect.y = self.rect.y


        def reset(self):
            scr.bilt(self.image, (self.rect.x,self.rect.y))

geroi3 = igrok("rocket.png", 50, 400, 15)

class Enemy(obiekt):
    def update(self):
        if self.rect.y < 500:
            self.rect.y += self.speed
        else:
            self.rect.y =0
            self.rect.x = randint(0,650)

geroi2 = Enemy("ufo.png", 120, 150, 2)
geroi4 = Enemy("ufo.png", 75, 320, 2)
geroi5 = Enemy("ufo.png", 75, 250, 2)
geroi12 = Enemy("ufo.png", 70, 244, 2)
geroi13 = Enemy("ufo.png", 70, 248, 2)

class Bullet(obiekt):
    def fire(self):
        if self.rect.y > 0:
            self.rect.y -= self.speed
        else:
            self.rect.y = -100
b = Bullet("bullet.png", -50, -50,5)

from random import*

class Strelba(obiekt):
    def update(self):
        if self.rect.y < 500:
            self.rect.y += self.speed
        else:
            self.rect.y =0
            self.rect.x = randint(0,650)

geroi6 = Strelba("tnt.jpg", 120, 150, 2)
geroi7 = Strelba("tnt.jpg", 75, 320, 2)
   
class Bomba(obiekt):
    def update(self):
        if self.rect.y < 500:
            self.rect.y += self.speed
        else:
            self.rect.y =0
            self.rect.x = randint(0,650)

geroi9 = Bomba("ptnt.png", 120, 150, 2)
geroi10 = Bomba("ptnt.png", 65, 250, 2)

class Pom(obiekt):
    def update(self):
        if self.rect.y < 500:
            self.rect.y += self.speed
        else:
            self.rect.y =0
            self.rect.x = randint(0,650)

geroi14 = Pom("ybl.png", 120, 150, 2)


font.init()
fonti = font.Font(None, 50)
ochki = 0
while game:
    scr.blit(galaxy, (0 , 0))
    txt = "glasses"+str(ochki)
    text = fonti.render(txt, 1, (255, 0, 0))
    scr.blit(text, (10, 20))
    if sprite.collide_rect(geroi5, b):
        geroi5.rect.y= -50
        geroi5.rect.x = randint(0,650)
        ochki+=1
    if sprite.collide_rect(geroi2, b):
        geroi2.rect.y= -50
        geroi2.rect.x = randint(0,650)
        ochki+=1
    if sprite.collide_rect(geroi4, b):
        geroi4.rect.y= -50
        geroi4.rect.x = randint(0,650)
        b.rect.y= -100
        ochki+=1
    if sprite.collide_rect(geroi12, b):
        geroi12.rect.y= -50
        geroi12.rect.x = randint(0,650)
        b.rect.y= -100
        ochki+=1
    if sprite.collide_rect(geroi14, b):
        geroi14.rect.y= -50
        geroi14.rect.x = randint(0,650)
        b.rect.y= -100
        ochki+=7
    if sprite.collide_rect(geroi13, b):
        geroi13.rect.y= -50
        geroi13.rect.x = randint(0,650)
        b.rect.y= -100
        ochki+=1
    if sprite.collide_rect(geroi6, b):
        geroi6.rect.y = -50
        geroi6.rect.x = randint(0,650)
        b.rect.y = -100
        ochki-=1
    if sprite.collide_rect(geroi7, b):
        geroi7.rect.y = -50
        geroi7.rect.x = randint(0,650)
        b.rect.y = -100
        ochki-=1
    if sprite.collide_rect(geroi9, b):
        geroi9.rect.y = -50
        geroi9.rect.x = randint(0,650)
        b.rect.y = -100
        ochki-=5.0
    if sprite.collide_rect(geroi10, b):
        geroi10.rect.y = -50
        geroi10.rect.x = randint(0,650)
        b.rect.y = -100
        ochki-=5
    if ochki >25:
        game = False
        win = True
    for e in event.get():
        if e.type == QUIT:
            game = False
    if ochki <-25:
        game = False
        lose = True
    for e in event.get():
        if e.type == QUIT:
            game = False



    geroi.reset()
    geroi2.reset()
    geroi3.reset()
    geroi4.reset()
    geroi5.reset()
    geroi6.reset()
    geroi7.reset()
    geroi9.reset()
    geroi10.reset()
    geroi12.reset()
    geroi13.reset()
    geroi14.reset()
    geroi.update()
    geroi2.update()
    geroi3.update()
    geroi4.update()
    geroi5.update()
    geroi6.update()
    geroi7.update()
    geroi9.update()
    geroi10.update()
    geroi12.update()
    geroi13.update()
    geroi14.update()
    b.reset()
    b.fire()
    display.update() 
    clock.tick(FPS)

while lose:
    lose = transform.scale(image.load("died.jpg"), (700,500))
    scr.blit(lose, (0 , 0))
    for e in event.get():
        if e.type == QUIT:
            lose = False
    
    display.update() 

while win:
    win1 = transform.scale(image.load("win.jpg"), (700,500))
    scr.blit(win1, (0 , 0))
    for e in event.get():
        if e.type == QUIT:
            win = False
    
    display.update() 