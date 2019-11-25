import board
import time
import pulseio

class RGB(object):

    def __init__(self, r, g, b):
        self.r = pulseio.PWMOut(r)
        self.g = pulseio.PWMOut(g)
        self.b = pulseio.PWMOut(b)

    def red(self):
        self.r.duty_cycle = 0
        self.g.duty_cycle = (2**16)-1
        self.b.duty_cycle = (2**16)-1
		
    def green(self):
        self.r.duty_cycle = (2**16)-1
        self.g.duty_cycle = 0
        self.b.duty_cycle = (2**16)-1
		
    def blue(self):
        self.r.duty_cycle = (2**16)-1
        self.g.duty_cycle = (2**16)-1
        self.b.duty_cycle = 0
		
    def cyan(self):
        self.r.duty_cycle = (2**16)-1
        self.g.duty_cycle = 0
        self.b.duty_cycle = 0

    def magenta(self):
        self.r.duty_cycle = 0
        self.g.duty_cycle = (2**16)-1
        self.b.duty_cycle = 0
		
    def yellow(self):
        self.r.duty_cycle = 0
        self.g.duty_cycle = 0
        self.b.duty_cycle = (2**16)-1
		
    def rainbow(self, x):
        if x == "rate1":
            self.r.duty_cycle = 0
            self.b.duty_cycle = (2**16)-1
            self.g.duty_cycle = (2**16)-1
            for i in range(1, 13106):
                self.r.duty_cycle += 6
                self.b.duty_cycle -= 4
                time.sleep(.002)
            self.r.duty_cycle = (2**16)-1
            self.b.duty_cycle = 0
            self.g.duty_cycle = (2**16)-1
            for i in range(1, 13106):
                self.b.duty_cycle += 6
                self.g.duty_cycle -= 4
                time.sleep(.002)
            self.r.duty_cycle = (2**16)-1
            self.b.duty_cycle = (2**16)-1
            self.g.duty_cycle = 0
            for i in range(1, 13106):
                self.g.duty_cycle += 6
                self.r.duty_cycle -= 4
                time.sleep(.002)

        elif x == "rate2":
            self.r.duty_cycle = 0
            self.b.duty_cycle = (2**16)-1
            self.g.duty_cycle = (2**16)-1
            for i in range(1, 6553):
                self.r.duty_cycle += 11
                self.b.duty_cycle -= 9
            self.r.duty_cycle = (2**16)-1
            self.b.duty_cycle = 0
            self.g.duty_cycle = (2**16)-1
            for i in range(1, 6553):
                self.b.duty_cycle += 11
                self.g.duty_cycle -= 9
            self.r.duty_cycle = (2**16)-1
            self.b.duty_cycle = (2**16)-1
            self.g.duty_cycle = 0
            for i in range(1, 13106):
                self.g.duty_cycle += 6
                self.r.duty_cycle -= 4