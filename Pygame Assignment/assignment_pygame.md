# PyGame Assignment

##  What is pygame? Can you modify its source code?

PyGame is a Free and Open Source python programming language library for making multimedia applications like games built on top of the SDL library. You can modify its source code since it's open source, but ***Only*** if you know what you're doing.

##  What is Rectangle? How do you create a rectangle? (give sample code)

Rectangle is a plane figure with 4 straight sides and four right angles. In PyGame you use the `pygame.Rect` to store the *rectangular coordinates*.
```python
# in pygame you have 3 methods to initialize rectangle
rect1 = pygame.Rect(left, top, width, height)
rect2 = pygame.Rect((left, top), (width, height))
rect3 = pygame.Rect(object)
# those three will return a pygame.Rect object
```

##  Can you play music with pygame? (give sample code)

You can play music in PyGame using `pygame.mixer` module

```python
# first initialize the pygame.mixer
pygame.mixer.init()
# load the music
pygame.mixer.load(music_filepath)
# play the music
pygame.mixer.play(1) # you can change the 1 to any other number to loop x times
```

##  A lot of games involve timer in its gameplay. How do you create a timer from round start to round finish? (give sample code)

```python
# initialize a global time (using time module, you can use pygame timer if you want)
xtime = time.time()

def update():
    # some other code

    # checking if time elapsed is more than 5 second
    if time.time() - xtime >= 5:
        # do something
```

##  What is sprite and groups? When do you use it? (give sample code)

"The Sprite class is intended to be used as a base class for the different types of objects in the game." -PyGame docs

"The Group class that simply stores sprites." -PyGame docs

You use this when you want to add something like a projectile or something like that

```python
pygame.init()

class Bullet(Sprite):
    def __init__(self, settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
```

##  What is collision detection? Why is it important? (give sample code)

Collision detection is the computational problem of detecting the intersection of two or more objects. It's important because you have to need a boundary for one object and the other.

```python
# initialize the rectangle
rect1 = pygame.Rect(left, top, width, height)
rect2 = pygame.Rect(left2, top2, width2, height2)

# check if it's colliding
if rect1.colliderect(rect2):
    # do something
```

##  How do you display image in pygame? What is the function of blit? (give sample code)

Blitting is doing a complete copy of one set of pixels onto another
```python
# initialize pygame
pygame.init()
# set the display to 1920x1080
screen = pygame.display.set_mode(1920, 1080)
# load image
image = pygame.image.load(image_filepath)
# copy the image to the screen at 0,0
screen.blit(image, (0, 0))
# updating the screen
pygame.display.update()
# or 
pygame.display.flip()```

##  How do you tell a bunch of sprites to update and draw at (almost) the same time? (give sample code)

```python
# initialize pygame
pygame.init()
# set the display to 1920x1080
screen = pygame.display.set_mode(1920, 1080)
for sprite in sprites_list:
    sprite.update()
    # pretend that the sprites is an image
    screen.blit(sprite.image, sprite.image.get_rect())
```

##  What is game physics? Why is it important?

Game physics involves the introduction of the laws of physics into a simulation or game engine, particularly in 3D computer graphics, for the purpose of making the effects appear more realistic to the observer.

##  How do you display text in pygame? (give sample code)

```python
# initialize pygame
pygame.init()
# set the display to 1920x1080
screen = pygame.display.set_mode(1920, 1080)

# load a font
font = pygame.font.Font("fonts/OpenSans-Regular.ttf", 32)
# First parameter is the text
# Second parameter is anti-aliasing
# Third parameter is the color
text = font.render("Something to write", True, (255, 255, 255))
# Copy the text to the screen
screen.blit(text, text.get_rect())
# Update the screen
pygame.display.update()
```

##  How do you move a sprite / image in pygame? (give sample code)

```python
import enum


class MoveTypes(enum.Enum):
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3

class Ship:
    def __init__(self, screen):
        self.screen = screen
        self.health = 100
        self.image = pygame.image.load('images/ships/ship1.png')
        self.rect = self.image.get_rect()
        self.screenRect = self.screen.get_rect()
        self.isMoving = False
        self.moveDirection = MoveTypes.RIGHT
        self.time = time.time()
        self.rect.centerx = self.screenRect.centerx
        self.rect.bottom = self.screenRect.bottom-25

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.isMoving:
            self.move(self.moveDirection)

    def move(self, moveType):
        if moveType == MoveTypes.UP:
            if (self.rect.top - 1 >= self.screenRect.top) ^ (self.rect.top <= self.screenRect.centery*1.25):
                self.rect.centery -= 1
        elif moveType == MoveTypes.DOWN:
            if self.rect.bottom + 1 <= self.screenRect.bottom:
                self.rect.centery += 1
        elif moveType == MoveTypes.RIGHT:
            if self.rect.right + 1 <= self.screenRect.right:
                self.rect.centerx += 1
        elif moveType == MoveTypes.LEFT:
            if self.rect.left - 1 >= self.screenRect.left:
                self.rect.centerx -= 1
```

##  How do you fill a color of a surface? (give sample code)

```python
# initialize a surface object
surface = Surface((width, height))
# fill the surface with white
surface.fill((255, 255, 255))
```

##  You have a player sprite. How do you randomize its position in a screen? (give sample code)

```python
import random
screen_size = (1920, 1080)
# initialize a player object (just pretend that i have it)
player = Player()
# and pretend that the player have a rect variable
# by using random.randint you can randomize its position
player.rect.center = (random.randint(0, screen_size[0]), random.randint(0, screen_size[1]))
```

##  Did you notice there is no number 9? (Y/N)

Not at first Glance, But yes.

Done By: 1. Fauzan Ardhana Putra (2301933295)

         2. Ellis Pax Mapakama (2301960024)