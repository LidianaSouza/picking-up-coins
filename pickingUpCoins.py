# code author: Lidiana Souza dos Anjos
# GitHub: https://github.com/LidianaSouza/
# GitLab: https://gitlab.com/Lidiana

# ----------------------------------------------------------------- #

# imports
import machine
import framebuf
import pyb
import time
import sys

# ----------------------------------------------------------------- #

# hardware components settings
i2c = machine.I2C('X')
y4 = machine.Pin('Y4')
adc = pyb.ADC(y4)

# ----------------------------------------------------------------- #

# LCD settings
width,high = 64,32
fbuf = framebuf.FrameBuffer(bytearray(width * high // 8), width, high, framebuf.MONO_HLSB)
fbuf.fill(0)

# ----------------------------------------------------------------- #

# init settings
playerWidth, playerHigh = 2,2
posPlayerX = int((width - playerWidth)/2) # int(): in case of a decimal number
posPlayerY = int((high - playerHigh))

# ----------------------------------------------------------------- #

#classes

# this class was made by Peter Hinch: https://forum.micropython.org/viewtopic.php?t=2727
class Rando(object):
    def __init__(self, strInit = ""):
        self.x  = [1200, 2345, 5798]            # Arbitrary initial state
        self.modify(strInit)                    # Modify initial values using the passed string
        self.xSave = [self.x[0], self.x[1], self.x[2]] # Save a copy of the initial values

    def reset(self):                            # Restore from saved value
        self.x = [self.xSave[0], self.xSave[1], self.xSave[2]]

    def modify(self, strMod):                   # Modify initial generator state using a string
        for strX in strMod:
            nIdx = self.value(3)                # Iterate the generator and get a random index between 0 and 2
            self.x[nIdx] ^= ord(strX)           # Modify the integer stored at that index using the passed character
            if self.x[nIdx] == 0:               # Disallow zero values
                self.x[nIdx] = ord(strX)

    def value(self, nModulo):                   # Return a random integer in range 0 to nModulo -1
        self.x[0] = 171*(self.x[0] % 177) - 2*(self.x[0] //177)
        if self.x[0] < 0:
            self.x[0] += 30269
        self.x[1] = 172*(self.x[1] % 176) - 35*(self.x[1] // 176)
        if self.x[1] < 0:
            self.x[1] += 30307
        self.x[2] = 170*(self.x[2] % 178) - 63*(self.x[2] // 178)
        if self.x[2] < 0:
            self.x[2] += 30323
        temp = self.x[0]/30269.0 + self.x[1]/30307.0 + self.x[2]/30323.0
        temp = (temp - int(temp))*nModulo
        return int(temp)


class Forms(object):


    def __init__(self, x, y, w=1, h=1):

        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):

        fbuf.fill_rect(self.x,self.y,self.w,self.h, 0xffff)
        i2c.writeto(8, fbuf)

    def update(self):
        pass


class Player(Forms):


    def __init__(self, x, y, w=1, h=1):

        super().__init__(x, y, w, h)
        self.lX = 0


    def update(self, posPlayerX):

        self.x = posPlayerX
        if self.x!=self.lX:
            fbuf.fill(0)
        self.lX = self.x
        super().draw()


class Coins(Forms):


    def __init__(self, x, y, w=1, h=1):

        super().__init__(x, y, w, h)
        self.lX = 0
        self.lY = 0
        self.c = 0

    def update(self, coinX, speed):

        super().draw()
        if self.c == high:
            self.x = coinX
        if self.c <= high:
            fbuf.pixel(self.lX,self.lY,0)
            self.y = self.c
            super().draw()
            time.sleep_ms(speed)
            self.lX = self.x
            self.lY = self.y
            self.c += 1
        else:
            self.c = 0


# ----------------------------------------------------------------- #

print("|*******************************************************|")
print("|                                                       |")
print("|  Welcome to Picking Up Coins to Have Lunch at Bandejão!  |")
print("|                                                       |")
print("|*******************************************************|")

print("")
print("")

time.sleep_ms(200)

print("To close the game properly, press Reset buttom")

a = Rando('girtiv') # Arbitrary string scrambles initial value
coinX = a.value(width)

p = Player(posPlayerX, posPlayerY, playerWidth, playerHigh)
c = Coins(coinX, 0, 1, 1)
score = 0
try:
    while True:

        posPlayerX = int(adc.read()*(width-playerWidth)/255)
        p.update(posPlayerX)

        coinX = a.value(width)
        c.update(coinX, 0)
        if (c.y == p.y and c.x == p.x) or (c.y == p.y+1 and c.x == p.x+1):
            score += 10
            print("Your score: "+str(score))

except KeyboardInterrupt: # when Ctrl+c
    print("The game was closed by the user.")

        
