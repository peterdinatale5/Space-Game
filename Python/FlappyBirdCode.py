import pygame
import time
import neat
import os
import random

WIN_WIDTH = 100
WIN_HEIGHT = 800

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("igms", "bird1.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("igms", "bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("igms", "bird3.png")))] #transform to go through multiple images; scale2x to make the pictures bigger
PIPE_IMG = [pygame.transform.scale2x(pygame.image.load(os.path.join("igms", "pipe.png")))]
BASE_IMG = [pygame.transform.scale2x(pygame.image.load(os.path.join("igms", "base.png")))]
BG_IMG = [pygame.transform.scale2x(pygame.image.load(os.path.join("igms", "bg.png")))]

class Bird():
	IMGS = BIRD_IMGS #constants that relate to the movement of the bird
	MAX_ROTATION = 25
	ROT_VEL = 5
	ANIMATION_TIME = 5

	def __init__(self, x, y):
		self.x = x #everything below is what we are starting with
		self.y = y
		self.tilt = 0 #how much the bird is tilted. it is 0 or flat until we begin moving
		self.tick_count = 0
		self.vel = 0
		self.height = self.y
		self.img_count = 0
		self.img = self.IMGS[0]

	def jump(self):
		self.vel = -10.5 #negative because the origin is at the top
		self.tick_count = 0 #takes count of when we last jumped
		self.height = self.y #keeps track of where the bird jumped from

	def move(self):
		self.tick_count += 1 #a tick happened and a frame went by

		d = self.vel*self.tick_count + 1.5*self.tick_count**2 #tickcount represents how many seconds we have been moving for
																# displacment - how many pixles we are moving up or down this frame
		if 

while True:
	bird.move()



