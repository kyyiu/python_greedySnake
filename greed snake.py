# _*_coding:utf-8_*_
import pygame
from sys import exit
import random
from pygame.locals import *

def paused(win):#暂停函数
    pause = True
    while pause:
        text = pygame.font.SysFont('arial', 100)
        tp = text.render('Pause', True, (255, 255, 255))
        win.blit(tp, (375, 175))
        pygame.display.update()
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pause = False

def gameover(win):
    text = pygame.font.SysFont('arial',100)
    tp = text.render("gameo",True,(255,255,255))
    tp2 = text.render('space',True,(255,255,255))
    win.blit(tp,(375,175))
    win.blit(tp2,(375,275))
    pygame.display.update()
    while True:
        for event in  pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    startgame()

def startgame():
    pygame.init()
    pygame.mixer.init()
    pygame.event.set_allowed([ KEYDOWN, QUIT])
    pygame.mixer.music.load(r'bgm.mp3')
    strawberry =pygame.image.load(r'fruit\strawbe.gif')
    pinaple = pygame.image.load(r'fruit\pinaple.gif')
    mongle = pygame.image.load(r'fruit\mongle.gif')
    fruits = [strawberry,pinaple,mongle]
    sh = pygame.image.load(r'snake\shead.gif')
    sb = pygame.image.load(r'snake\sbody.gif')
    st = pygame.image.load(r'snake\stail.gif')
    snake = [sh,sb,st]
    fruit_count = 1
    win = pygame.display.set_mode((1000,600))
    pygame.display.set_caption('键盘事件')
    x,y = 500-sh.get_rect().width//2,300-sh.get_rect().height//2
    headposition = [x,y]
    head = 'left'
    operatehead = head
    frand = random.randint(0,2)
    fx, fy = 100,100
    position = [[x, y],[x + sh.get_rect().width+50, y], [x + sh.get_rect().width + st.get_rect().width+50, y]]
    pygame.mixer.music.play()
    scored = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    paused(win)
                if  event.key == K_RIGHT:
                    operatehead = 'right'
                elif event.key == K_LEFT:
                    operatehead = 'left'
                elif event.key == K_UP:
                    operatehead = 'up'
                elif event.key == K_DOWN:
                    operatehead = 'down'
        if operatehead == 'right' and not head == 'left':
            head = 'right'
        if operatehead == 'left' and not head == 'right':
            head = 'left'
        if operatehead == 'up' and not head == 'down':
            head = 'up'
        if operatehead == 'down' and not head == 'up':
            head = 'down'
        if head == 'right':
            headposition[0] += 30
        if head == 'left':
            headposition[0] -= 30
        if head == 'up':
            headposition[1] -= 30
        if head == 'down':
            headposition[1] += 30
        win.fill(0)
        position.insert(0,list(headposition))
        if fruit_count == 0:
            fx,fy = random.randint(2, 15)*50,random.randint(2, 8)*50
            frand = random.randint(0,2)
            fruit_count = 1
        if fx < headposition[0] < fx+fruits[frand].get_rect().width and fy < headposition[1] <fy+fruits[frand].get_rect().height:
            fruit_count = 0
            snake.insert(0,sh)
            snake[1] = sb
            scored += 50
        else:
            position.pop()
        i = 0
        for z in position:
            win.blit(snake[i],z)
            win.blit(fruits[frand], (fx, fy))
            i+=1
        if headposition[0] < 0 or headposition[0] > 1000:
            gameover(win)
        if headposition[1] < 0 or headposition[1] > 600:
            gameover(win)
        #print(position)
        for p in position[1::]:
            if p[0] == headposition[0] and p[1] == headposition[1]:
                gameover(win)
        sc = pygame.font.SysFont('arial',50)
        sc_idi = sc.render('score:%d'%scored,True,(255,255,255))
        win.blit(sc_idi,(0,0))
        pygame.display.update()
        pygame.time.Clock().tick(3)


if __name__ == "__main__":
    startgame()