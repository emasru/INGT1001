#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# Lager et sensorobjekt for kollisjon
collisionSensor = TouchSensor(Port.S1)

# Lager et sensorobjekt, og en variabel for å se hvilken state vi er i
onOffButton = TouchSensor(Port.S2) 
onState = False

leftMotor = Motor(Port.C)
rightMotor = Motor(Port.B)

# Initialize drive base
vehicle = DriveBase(leftMotor, rightMotor, wheel_diameter=55.5, axle_track=175)


# Write your program here.

while True:
    if onState: # Vi er i på-modus
        # Kjør så lenge ingenting har skjedd
        vehicle.drive(200, 0)
        # Så lenge ingen av knappene er trykket inn fortsetter den og kjøre
        while not collisionSensor.pressed() and not onOffButton.pressed():
            wait(10)
            
        # Hvis vi trykker på av knappen
        if onOffButton.pressed():
            onState = not onState # Skrur av
            vehicle.stop()
            ev3.speaker.say("Exercise done")
            wait(2000)
        # Hvis vi har møtt på en vegg i stedet
        elif collisionSensor.pressed():
            # Rygger litt og snur mot høyre
            vehicle.straight(-100)
            vehicle.turn(55)

    elif not onState: # Vi er i av-modus
        # Holder oss inn i loop med ingenting helt til på-knappen blir trykket
        while not onOffButton.pressed():
            continue
        onState = not onState # Skrur på
        ev3.speaker.say("Exercise 2")
        wait(2000)



