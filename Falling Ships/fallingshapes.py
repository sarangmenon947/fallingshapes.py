import pgzrun
import random
import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 500

zuko = Actor("man")
bullet = Actor("bullet")
ship = Actor("ship")
gameover = False
shipcount = 0
shiplist = []
zuko.pos = (500, 450)
fireball = False

def createships():
    number = 0
    for i in range(8):
        temp = Actor("ship")
        shiplist.append(temp)
        shiplist[i].pos = (125 * number + 33, 50)
        number = number + 1

createships()

def draw():
    global shiplist
    screen.blit("background", (0, 0))
    zuko.draw()
    bullet.draw()
    for i in shiplist:
        i.draw()
        i.y = i.y + random.randint(0, 3) - 0.8
    
    if fireball == True:
        bullet.y -= 10
    if gameover == True:
        screen.clear()
        screen.fill("pink")
        screen.draw.text("You Lose!", (500, 250))

    if shipcount == 8:
        screen.clear()
        screen.fill("green")
        screen.draw.text("You Win!", (500, 250))

def update():
    global gameover, shiplist, shipcount
    if keyboard.left:
        zuko.x -= 10
    if keyboard.right:
        zuko.x += 10

    if keyboard[keys.SPACE]:
        fire()

    for i in shiplist:
        if i.y > 480:
            gameover = True
    for i in shiplist:
        if bullet.colliderect(i):
            shiplist.remove(i)
            shipcount += 1

def fire():
    global fireball
    bullet.pos = (zuko.x, (zuko.y - 5))
    fireball = True
    
pgzrun.go()


