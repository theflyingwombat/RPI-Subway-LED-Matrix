import datetime
import os
import time
import calendar
import urllib

from samplebase import SampleBase
from rgbmatrix import graphics
from google.transit import gtfs_realtime_pb2
from config import APIKey


class RunText(SampleBase):

    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def drawCircle(self, canvas, offset, color):
        graphics.DrawLine(canvas,7,0 + offset,11,0 + offset,color)
        graphics.DrawLine(canvas,5,1 + offset,13,1 + offset,color)
        graphics.DrawLine(canvas,4,2 + offset,14,2 + offset,color)
        graphics.DrawLine(canvas,4,3 + offset,14,3 + offset,color)
        graphics.DrawLine(canvas,3,4 + offset,15,4 + offset,color)
        graphics.DrawLine(canvas,3,5 + offset,15,5 + offset,color)
        graphics.DrawLine(canvas,3,6 + offset,15,6 + offset,color)
        graphics.DrawLine(canvas,3,7 + offset,15,7 + offset,color)
        graphics.DrawLine(canvas,3,8 + offset,15,8 + offset,color)
        graphics.DrawLine(canvas,4,9 + offset,14,9 + offset,color)
        graphics.DrawLine(canvas,4,10 + offset,14,10 + offset,color)
        graphics.DrawLine(canvas,5,11 + offset,13,11 + offset,color)
        graphics.DrawLine(canvas,7,12 + offset,11,12 + offset,color)

    def draw_a(self, location, canvas):
        if location == 'top':
            text_offset = 0
            circle_offset = 2
        else:
            text_offset= 15
            circle_offset = 17
        blue = graphics.Color(0,57,166)
        black = graphics.Color(0,0,0)
        white = graphics.Color(255, 255, 255)
        yellow = graphics.Color(252,204,10)

        self.drawCircle(canvas, circle_offset, blue)


        graphics.DrawLine(canvas, 7,7 + text_offset,7,11 + text_offset,white)
        graphics.DrawLine(canvas, 11,7 + text_offset,11,11 + text_offset,white)
        graphics.DrawLine(canvas, 8,6 + text_offset,8,6 + text_offset,white)
        graphics.DrawLine(canvas, 9,5 + text_offset,9,5 + text_offset,white)
        graphics.DrawLine(canvas, 10,6 + text_offset,10,6 + text_offset,white)
        graphics.DrawLine(canvas, 8,9 + text_offset,10,9 + text_offset,white)

    def draw_d(self, location, canvas):
        if location == 'top':
            text_offset = 0
            circle_offset = 2
        else:
            text_offset= 15
            circle_offset = 17
        orange = graphics.Color(255,99,25)
        black = graphics.Color(0,0,0)
        white = graphics.Color(255, 255, 255)
        yellow = graphics.Color(252,204,10)

        self.drawCircle(canvas, circle_offset, orange)


        graphics.DrawLine(canvas, 7,5 + text_offset,7,11 + text_offset,black)
        graphics.DrawLine(canvas, 8,5 + text_offset,10,5 + text_offset,black)
        graphics.DrawLine(canvas, 8,11 + text_offset,10,11 + text_offset,black)
        graphics.DrawLine(canvas, 11,6 + text_offset,11,10 + text_offset,black)


    def draw_e(self, location, canvas):
        if location == 'top':
            text_offset = 0
            circle_offset = 2
        else:
            text_offset= 15
            circle_offset = 17
        blue = graphics.Color(0,57,166)
        black = graphics.Color(0,0,0)
        white = graphics.Color(255, 255, 255)
        yellow = graphics.Color(252,204,10)

        self.drawCircle(canvas, circle_offset, blue)


        graphics.DrawLine(canvas, 7,5 + text_offset,7,11 + text_offset,white)
        graphics.DrawLine(canvas, 8,5 + text_offset,11,5 + text_offset,white)
        graphics.DrawLine(canvas, 8,8 + text_offset,10,8 + text_offset,white)
        graphics.DrawLine(canvas, 8,11 + text_offset,11,11 + text_offset,white)


    def draw_m(self, location, canvas):
        if location == 'top':
            text_offset = 0
            circle_offset = 2
        else:
            text_offset= 15
            circle_offset = 17
        orange = graphics.Color(255,99,25)
        black = graphics.Color(0,0,0)
        white = graphics.Color(255, 255, 255)
        yellow = graphics.Color(252,204,10)

        self.drawCircle(canvas, circle_offset, orange)


        graphics.DrawLine(canvas, 6,5 + text_offset,6,11 + text_offset,black)
        graphics.DrawLine(canvas, 12,5 + text_offset,12,11 + text_offset,black)
        graphics.DrawLine(canvas, 7,6 + text_offset,7,6 + text_offset,black)
        graphics.DrawLine(canvas, 8,7 + text_offset,8,7 + text_offset,black)
        graphics.DrawLine(canvas, 9,8 + text_offset,9,8 + text_offset,black)
        graphics.DrawLine(canvas, 10,7 + text_offset,10,7 + text_offset,black)
        graphics.DrawLine(canvas, 11,6 + text_offset,11,6 + text_offset,black)


    def draw_f(self, location, canvas):
        if location == 'top':
            text_offset = 0
            circle_offset = 2
        else:
            text_offset= 15
            circle_offset = 17
        orange = graphics.Color(255,99,25)
        black = graphics.Color(0,0,0)
        white = graphics.Color(255, 255, 255)
        yellow = graphics.Color(252,204,10)

        self.drawCircle(canvas, circle_offset, orange)


        graphics.DrawLine(canvas, 7,5 + text_offset,11,5 + text_offset,black)
        graphics.DrawLine(canvas, 7,6 + text_offset,7,11 + text_offset,black)
        graphics.DrawLine(canvas, 8,8 + text_offset,9,8 + text_offset,black)

    def draw_4(self, location, canvas):
        if location == 'top':
            text_offset = 0
            circle_offset = 2
        else:
            text_offset= 15
            circle_offset = 17
        green = graphics.Color(0, 120, 60)
        black = graphics.Color(0,0,0)
        white = graphics.Color(255, 255, 255)
        yellow = graphics.Color(252,204,10)

        self.drawCircle(canvas, circle_offset, green)


        graphics.DrawLine(canvas, 10,5 + text_offset,10,5  + text_offset,white)
        graphics.DrawLine(canvas,  9,6 + text_offset,10,6 + text_offset,white)
        graphics.DrawLine(canvas,  8,7 + text_offset,8,7 + text_offset,white)
        graphics.DrawLine(canvas,  10,7 + text_offset,10,7 + text_offset,white)
        graphics.DrawLine(canvas,  7,8 + text_offset,7,8 + text_offset,white)
        graphics.DrawLine(canvas,  10,8 + text_offset,10,8 + text_offset,white)
        graphics.DrawLine(canvas,  7,9 + text_offset,11,9 + text_offset,white)
        graphics.DrawLine(canvas,  10,10 + text_offset,10,10 + text_offset,white)
        graphics.DrawLine(canvas,  10,11 + text_offset,10,11 + text_offset,white)

    def draw_q(self, location, canvas):
        if location == 'top':
            text_offset = 2
            circle_offset = 2
        else:
            text_offset = 17
            circle_offset = 17
        green = graphics.Color(0, 120, 60)
        black = graphics.Color(0,0,0)
        white = graphics.Color(255, 255, 255)
        yellow = graphics.Color(252,204,10)
        self.drawCircle(canvas, circle_offset, yellow)

        graphics.DrawLine(canvas,8,3 + text_offset,10,3 + text_offset,black)
        graphics.DrawLine(canvas,7,4 + text_offset,7,4 + text_offset,black)
        graphics.DrawLine(canvas,11,4 + text_offset,11,4 + text_offset,black)
        graphics.DrawLine(canvas,6,5 + text_offset,6,5 + text_offset,black)
        graphics.DrawLine(canvas,12,5 + text_offset,12,5 + text_offset,black)
        graphics.DrawLine(canvas,6,6 + text_offset,6,6 + text_offset,black)
        graphics.DrawLine(canvas,12,6 + text_offset,12,6 + text_offset,black)
        graphics.DrawLine(canvas,6,7 + text_offset,6,7 + text_offset,black)
        graphics.DrawLine(canvas,10,7 + text_offset,10,7 + text_offset,black)
        graphics.DrawLine(canvas,12,7 + text_offset,12,7 + text_offset,black)
        graphics.DrawLine(canvas,7,8 + text_offset,7,8 + text_offset,black)
        graphics.DrawLine(canvas,10,8 + text_offset,11,8 + text_offset,black)
        graphics.DrawLine(canvas,8,9 + text_offset,9,9 + text_offset,black)
        graphics.DrawLine(canvas,11,9 + text_offset,11,9 + text_offset,black)

    def run(self):
        numLoops = 0;
        self.matrix.brightness = 75
        traintime = "86th Q" #self.refresh()
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont('/home/pi/rpi-rgb-led-matrix/fonts/7x13.bdf')
        textColor = graphics.Color(255, 255, 0)
        pos = 18
        my_text = traintime
        yellow = graphics.Color(252,204,10)
        black = graphics.Color(0,0,0)
        white = graphics.Color(220, 220, 220)
        red = graphics.Color(204, 51, 0)
        green = graphics.Color(0, 120, 60)
        orange = graphics.Color(230,138,0)
        sickgreen = graphics.Color(204,204,0)
        left = True
        wait = 10


        while True:
            offscreen_canvas.Clear()
            self.draw_a('top', offscreen_canvas)
            self.draw_a('bottom', offscreen_canvas)
            #self.draw_q('top', offscreen_canvas)
            time.sleep(1)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


if __name__ == '__main__':
    while True:
        run_text = RunText()
        if (not run_text.process()):
            run_text.print_help()

        time.sleep(5)
