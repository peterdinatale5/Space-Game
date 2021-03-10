'''
Peter Di Natale
03-02-2021
Description/process: For my final project, I created an animated game using the python library pygame. To start off the project, I thought about 
what the theme of my game should be, what types of charachters I should include, what the challenge should be, etc. I then did some research on youtube 
to learn some more about pygame (see the link below). I was just learning for some of the basic commands to needed to start messing around with some ideas.
I then referred a lot to the pygame documentation and began sketching out on notability some possible game ideas and structures that I thought
would fit well. After more research and a few different iterations, I finally decided on the game I wanted. From here on out, I mainly just referred to
my notability sketches and transformed the ideas in my head into code to make a game.

Background info: This game was inspired by my passion for astronomy and also love for video games. I have always been fascinated by space
and this was a great opportunity for me to show that interest! See the instructions within the game for how you must traverse meteors
to retrieve your lost food supply. By gaining back your bananas, you will have food to eat on your trip home. Enjoy!

Image sources:
background = https://www.123rf.com/photo_123300332_stock-vector-cartoon-space-background-stars-cosmos-night-starry-sky-universe-dust-light-star-milky-way-galaxy-ast.html
meteor: https://www.clipartmax.com/middle/m2H7K9K9H7H7d3Z5_meteoroid-meteorite-meteor-shower-asteroid-clip-art-meteor-vector-png/
mars = http://clipart-library.com/mars-cartoon-cliparts.html
venus = http://clipart-library.com/new_gallery/11-119614_planet-clipart-.png
bananas = http://clipart-library.com/image_gallery/459244.png
ufo ship 1 = https://www.pinclipart.com/maxpin/ihxwiJo/
ufo ship 2 = http://pngimg.com/images/fantasy/ufo

Other Code Sources:
#source for pygame documentaton in general: https://www.pygame.org/docs/
#video that I used to learn introductory information about pygame: https://www.youtube.com/watch?v=i6xMBig-pP4
#source that I used for gaining a general understanding of how to make a start screen/window - https://stackoverflow.com/questions/20356307/how-would-i-add-a-start-screen-to-this-pygame-python-code
#source for drawing invisible rectangle (for collisions) - https://pygame.readthedocs.io/en/latest/3_image/image.html
#source for creating a timer: https://stackoverflow.com/questions/30720665/countdown-timer-in-pygame
#source for installing pygame - https://www.pygame.org/wiki/GettingStarted

Honor Code: "On my honor, I have niether given nor recieved unauthorized aid." Peter M. Di Natale
'''

#-------LIBRARIES------
import pygame
import random
from pygame import mixer


#-------CLASSES--------
class Player(object):
	'''
	This class is used to create the user's charachter and all of the necessary variables that pertain to the movement and collisions that
	the charachter experiences. As seen in the constructor, I first define thex and y position while also loading the image for user
	'''
	def __init__(self, x_pos, y_pos, image):
		#contructor function takes in the initial x and y coordinates of the object as well as the image.
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.jump = 0
		self.jumped = False
		self.image = pygame.image.load(image)
		self.image = pygame.transform.scale(self.image, (player_size, player_size))

	def move(self):
		'''
		Function that controls the movement of user's charachter in the game.
		As seen with series of conditional statements below, there are a few keys
		that the user can press that will change the x and y coordinates of the player
		The x coordinates corespond with the movement left and right while the y controls
		up and down.
		'''
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				self.x_pos -= vel

			if event.key == pygame.K_RIGHT:
				self.x_pos += vel

			if event.key == pygame.K_UP:
				self.y_pos -= vel

			if event.key == pygame.K_DOWN:
				self.y_pos += vel

	def draw(self):
		#function that handles drawing the charachter; blit is used to create an image on the screen
		screen.blit(self.image, (self.x_pos, self.y_pos))
		self.rect = self.image.get_rect(topleft = (self.x_pos, self.y_pos))

	def define_boundaries(self):
		'''
		These conditional statements restrict the charachter from moving off of the screen
		I subtracted chachter size from both the height and the width in certain instances
		This is because when pygame draws an image, it starts from the top left corner.
		'''
		if self.x_pos < 0:
			self.x_pos = 0
		elif self.x_pos > WIDTH-50:
			self.x_pos = WIDTH-50

		if self.y_pos < 0:
			self.y_pos = 0
		elif self.y_pos > HEIGHT-50:
			self.y_pos = HEIGHT-50

	def activate(self):
		#this function calls all of the above function at once to limit any unessary redundancy
		self.move()
		self.draw()
		self.define_boundaries()

class Enemy(object):
	'''
	This is a class that organizes the information needed to run the enemy's actions
	Similar to the player, it stores the x and y values along with the appropriate image.
	The contructor of this function also stores the velocity of the enemy which is generated
	using the random library. I did this to avoid having all of the meteors fall at the same speed
	'''
	def __init__(self):
		#constructor function for the class Enemy; setting position, velocity, and loading the charachter's image
		self.rock_y = 0
		self.rock_x = random.randint(0,WIDTH)
		self.rock_vel = random.randint(5,10)
		self.image = pygame.image.load('meteor.png')
		self.image = pygame.transform.scale(self.image, (40, 40))

	def move(self):
		'''
		chooses a random location for the starting position of the meteor and the process repeats
		when the meteor falls off the screen.
		'''
		if self.rock_y < HEIGHT:
			self.rock_y += self.rock_vel
		else:
			self.rock_y = 0
			self.rock_x = random.randint(0,WIDTH)
			self.rock_y += self.rock_vel

	def collision(self):
		'''
		Checking to see if a collision occurs between the car and the meteor
		in order to check for this condition, I have to draw an invisible rectangle around
		both charachters (and all other charachters in the game) and see if the rectangles collide
		This is because the colliderect function does not apply to images by themselves.
		'''
		if self.rect.colliderect(Car.rect):
			return "meteor strike"
		if self.rect.colliderect(Shield_1) or self.rect.colliderect(Shield_2):
			self.rock_x = random.randint(0,WIDTH)
			self.rock_y = 0

	def draw(self):
		#drawing the image on the screen (different than loading the image)
		#drawing an imaginary rectangle around the charchter
		screen.blit(self.image, (self.rock_x, self.rock_y))
		self.rect = self.image.get_rect(topleft = (self.rock_x, self.rock_y))

	def activate(self):
		#function that activates multiple parts of the class. This is more for organiation purposes
		self.move()
		self.draw()
		self.collision()

class Food(object):
	'''
	This is a class for the food in the game. The only food involved is a banana, but since there are many
	different aspects of th banana (position, image, number of bananas, collision factors, etc) it was 
	easiest to organize all of this information into a class.
	'''
	def __init__(self, food_x, food_y):
		#constructor function that includes basic information such as position, image loading
		self.food_y = random.randint(100, HEIGHT-50)
		self.food_x = random.randint(0, WIDTH-50)
		self.image = pygame.image.load('bananas1.png')
		self.image = pygame.transform.scale(self.image, (30, 30))

	def draw(self):
		#drawing the image into the screen and putting a rectangle around it
		screen.blit(self.image, (self.food_x, self.food_y))
		self.rect = self.image.get_rect(topleft = (self.food_x, self.food_y))

	def eaten(self):
		#function that returns True if the charachter and food collide
		if self.rect.colliderect(Car.rect):
			return True

	def activate(self):
		#function that activates multiple parts of the class. This is more for organiation purposes
		self.draw()
		self.eaten()

class Protector(object):

	def __init__(self, x_pos, y_pos, image_name, size, vel):
		#constructor function that includes basic information such as position, image loading
		self.vel = vel
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.image = pygame.image.load(image_name)
		self.image = pygame.transform.scale(self.image, (size, size))

	def move(self):
		#function for moving the planets across the sreen for protection
		self.x_pos -= self.vel
		if self.x_pos < 0:
			self.x_pos = WIDTH

	def draw(self):
		#Drawing the images onto the screen. Again, this is separate from loading the images from a directory
		screen.blit(self.image, (self.x_pos, self.y_pos))
		self.rect = self.image.get_rect(topleft = (self.x_pos, self.y_pos))

	def activate(self):
		#function that activates multiple parts of the class. This is more for organiation purposes
		self.move()
		self.draw()



#-------FUNCTIONS-------
def print_score():
	#printing the score of the game and the number of seconds that are remaining
	text = "Score:" + str(score)
	label = font.render(text, 1, (255,255,255)) 
	screen.blit(label, (5, 5))

	text_2 = "Time:" + str(seconds)
	label_2 = font.render(text_2, 1, (255,255,255))
	screen.blit(label_2, (WIDTH-180, 5))

def play_music(song):
	#function that can play music simply by passing it into the parenthesis
	mixer.music.load(song)
	mixer.music.play(1000)

def draw_circle():
	#this is a function that exists for testing purposes for the placement of the planets
	circle_center_x = 475
	circle_center_y = 300
	circle_thickness = 3
	circle_radius = 230
	pygame.draw.circle(screen, (255,165,0), (circle_center_x, circle_center_y), circle_radius, circle_thickness)

def create_meteors():
	'''
	Determines the starting positions of the meteors
	The code below ensures that the same position isn't chosen twice for 2 meteors
	'''
	# meteor_rocks = [Enemy() for x in range(10)]

	global meteor_rocks
	meteor_rocks = [] #list of instances of the class Enemy
	meteor_rocks_xs = [] #list of meteor x positions

	#variables start and end are used to circle through the list of meteors
	end = 10
	start = 0 

	for x in range(10):
		#creating 10 separate instances of the class Enemy and keeping track of their starting x positions in a list
		instance = Enemy()
		meteor_rocks_xs.append(instance.rock_x)

	while start < end:
		#cycling through the list to make sure that no two meteors hold the same x position
		instance = Enemy()
		if instance.rock_x not in meteor_rocks_xs: #only add the instance to the final list if its x position isn't already chosen
				meteor_rocks.append(Enemy()) 
				start += 1

def create_start_screen():
	'''
	This is a function that is used for creating the starting window. Within it, I load images, such as both charachters and
	the instructions for the user. I also write some text that welcomes the user. Towards the end of the function, there is
	a while loop that exits the main screen and enters the main game window if one of the charachters is clicked.
	'''
	global end_start_screen, chosen_player

	while (end_start_screen==False):
		#while the start screen is still running
		keys = pygame.key.get_pressed()
		screen.fill(start_color)
		top_label = font.render("Welcome to my space game!", 1, (255, 0, 0))
		bottom_label = font.render("Are you ready to play?", 1, (255, 0, 0))

		#creating the image for the first charachter choice
		starter_ufo = pygame.image.load('ufo.png')
		starter_ufo = pygame.transform.scale(starter_ufo, (70, 70))
		screen.blit(starter_ufo, (100, 180))
		starter_ufo_rect = starter_ufo.get_rect(topleft = (100, 180))

		#creating the image for the second charachter choice
		rocket = pygame.image.load('spaceship.png')
		rocket = pygame.transform.scale(rocket, (70, 70))
		screen.blit(rocket, (320, 180))
		rocket_rect = rocket.get_rect(topleft = (320, 180))

		#loading the image for the instructions of the game
		instructions = pygame.image.load('instructions.png')
		instructions = pygame.transform.scale(instructions, (230, 330))

		for event in pygame.event.get():
			#in pygame, there are instances called "events" that can refer to different actions of the user.
			#if the player hits the red x in the corner of the screen to exit the game, quit pygame
			if event.type == pygame.QUIT:
				pygame.quit()

			if event.type == pygame.MOUSEBUTTONDOWN: #if the mouse is down, check to see which charachter was clicked
				x, y = event.pos

				#two if statements that check to see which of the two images was chosen to be the charachter
				#depending on which one they clicked on, this image will carry over to the main game window
				if starter_ufo_rect.collidepoint(x, y):
					chosen_player = "ufo.png"
					end_start_screen = True

				elif rocket_rect.collidepoint(x, y):
					chosen_player = "spaceship.png"
					end_start_screen = True

		#putting the words onto the screen
		screen.blit(top_label,(50,50))
		screen.blit(bottom_label, (90, 100))
		screen.blit(instructions, (130, 290))
		pygame.display.flip()



#--------VARIABLES-------
pygame.init()
clock = pygame.time.Clock()
FPS = 90

#Variables for players
player_size = 60
vel = 8
charachter_starting_x_pos = 50
charachter_starting_y_pos = 500
chosen_player = "ufo.png"

#Variables for colors
BLUE = (0, 0, 250)
RED = (250, 0, 50)
BLACK = (0,0,0)
start_color = (25,0,80)

#Variables for switching screens
run = True
end_start_screen = False

#Variables for backround
HEIGHT = 650
WIDTH = 500
bg = pygame.image.load('spacef.jpg')
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("times new roman", 35)

score = 0
level = 0



#--------MAIN CODE--------
play_music('ChillingMusic.wav') #playing the music for the game
pygame.display.set_caption("Space Game")
create_start_screen() #calling the function that controls the start screen

#creating instances of the classes above
Car = Player(charachter_starting_x_pos, charachter_starting_y_pos, chosen_player) #creating the main user charachter, which is an instance of the class player
banana = Food(300,300) #creating the food (x_pos, y_pos)
Shield_1 = Protector(80, 90, 'mars.png', 60, 3) #creating planet one
Shield_2 = Protector(350, 300, 'venus.png', 60, 5) #creating planet two
create_meteors()

ticks = pygame.time.get_ticks() #starting ticks (counting in milliseconds) for the timer in the game
while run:
	seconds = (pygame.time.get_ticks() - ticks)/1000 #setting the timer
	for event in pygame.event.get(): #in pygame there are things called events (these include, but are not limited to key movements)
		if event.type == pygame.QUIT: #if the "event" that occurs is the user clicking the x, quit the game
			run = False
		elif score > 100: #win condition
			run = False
			print("you win!")
		elif seconds > 60: #if the time exceeds 60 seconds
			run = False
			print("you lost")

	#activating the instances of certain classes and drawing the background
	#note: the background has to be constantly drawn in the while loop make it appear as if the charachter is "moving"
	screen.blit(bg, (0,0))
	Shield_1.activate()
	Shield_2.activate()
	Car.activate()
	banana.activate()

	for x in range(10):
		#iterate through all of the meteors to check if there is a collision
		meteor_rocks[x].activate()
		if meteor_rocks[x].collision() == "meteor strike":
			score -= .5

	if banana.eaten():
		#if the player collides with the banana, choose a new random location for the food
		#also, when this happens, increase the score
		score += 10
		banana.food_y = random.randint(100, HEIGHT-50)
		banana.food_x = random.randint(0, WIDTH-50)

	print_score()
	pygame.display.update()
	clock.tick(FPS) #setting frames per second to help ensure quality of the video is the same regardless of the device it's played on

pygame.quit()



