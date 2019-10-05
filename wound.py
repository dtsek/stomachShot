#!/usr/bin/python3

# Libraries
from picamera import PiCamera
from time import sleep

def holeView():

  # create camera object
  camera = PiCamera()
  #camera.rotation = 180
  #camera.resolution = (1920, 1080)
  #camera.framerate = 30
  #camera.brightness = 100
  #cameera.contrast = 1

  while True:
    camera.start_preview()
    sleep(100)  #bug avoidance
    camera.stop_preview()

if __name__ == '__main__':
  print('Starting the program...\n')
  holeView()

