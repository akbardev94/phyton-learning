from turtle import *
from datetime import datetime

def jump (distanz, winkel=0):
    penup()
    right(winkel)
    forward(distance)
    left(winkel)
    pendown()

def hand(laenge, spitze):
    fd(laenge*1.15)
    rt(90)
    fd(spitze/2.0)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze/2.0)

def make_hand_shape(name, laenge, spitze):
    reset()
    jump(-laenge*0.15)
    begin_poly()
    hand(laenge, spitze)
    end_poly()
    hand_form = get_poly()
    register_shape(name, hand_form)

    def clockface(radius):
        reset()
        pensize(7)
        for i in range(60):
            jump(radius)
            if i % 5 == 0:
                fd(25)
                jump(-radius-25)
            else:        
                dot(3)
                jump(-radius)
                rt(6)