import pygame, random,time

slow = False

f = 0
h = []
inscription = True
d=0
modo = 'usual'  # slowdown,gocenter,explosion


def key():
    a = {'speedx': random.randint(1, 8),
         'speedy': random.randint(1, 9),
         'p': random.randint(7, 21),
         'x': random.randint(25, 600 - 25),
         'y': random.randint(25, 650 - 25),
         'color': [random.randint(5, 255), random.randint(5, 255), random.randint(5, 255)]}
    h.append(a)


def play():
    for f in h:
        playmini(f)


def playmini(a):
    if f == 0 and a['speedx'] != 0:
        a['x'] += a['speedx']
        a['y'] += a['speedy']
        if a['x'] + a['p'] >= 600:
            a['x'] = 600 - a['p']
            a['speedx'] = -a['speedx']
        if a['x'] - a['p'] <= 0:
            a['x'] = a['p']
            a['speedx'] = -a['speedx']
        if a['y'] + a['p'] >= 650:
            a['y'] = 650 - a['p']
            a['speedy'] = -a['speedy']
        if a['y'] - a['p'] <= 0:
            a['y'] = a['p']
            a['speedy'] = -a['speedy']


def zachem():
    for a in h:
        if a['speedx'] > 0:
            a['speedx'] = a['speedx'] - 0.1
            if a['speedx'] < 0.1:
                a['speedx'] = 0
        elif a['speedx'] < 0:
            a['speedx'] = a['speedx'] + 0.1
            if a['speedx'] > -0.1:
                a['speedx'] = 0

        if a['speedy'] > 0:
            a['speedy'] = a['speedy'] - 0.1
            if a['speedy'] < 0.1:
                a['speedy'] = 0
        elif a['speedy'] < 0:
            a['speedy'] = a['speedy'] + 0.1
            if a['speedy'] > -0.1:
                a['speedy'] = 0


def stay_balls():
    for i in h:
        if i['speedx'] != 0 or i['speedy'] != 0:
            return False
    return True


def stop_center():
    for a in h:
        if a['x'] > 305 or a['x'] < 295:
            return False
    return True


def boom(timer):
    global modo,d
    if modo == 'slowdown':
        zachem()
        if stay_balls():
            modo = 'gocenter'
            for a in h:
                a['speedx'] = (300 - a['x']) / 300
                a['speedy'] = (325 - a['y']) / 300
    if modo == 'gocenter' and stop_center():
        for a in h:
            a['x'] = 300
            a['y'] = 325
            a['speedx'] = 0
            a['speedy'] = 0
        d=time.time()
        modo = 'explosion'
    if modo == 'explosion':
        print(time.time()-d)
        if  time.time()-d>=3:
            for a in h:
                a['speedx'] = random.randint(-18, 18)
                a['speedy'] = random.randint(-18, 18)
            modo = 'slowdown'
