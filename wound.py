import time
import picamera

with picamera.PiCamera() as camera:
	camera.resolution = (1920,1080)
	camera.hflip = True
	camera.vflip = True

	camera.start_preview()
