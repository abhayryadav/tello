# controll
import pygame
def init():
    pygame.init()
    win = pygame.display.set_mode((400,400))

def keyy(name_0f_key):
    ans = False
    for event in pygame.event.get() : pass
    inputkey = pygame.key.get_pressed()
    mykey = getattr(pygame,'K_{}'.format(name_0f_key))
    if inputkey[mykey]:
        ans =True
    pygame.display.update()
    return ans
def main():
    if keyy("LEFT"):
        print("left pressed")
    if keyy("RIGHT"):
        print("right pressed")
    if keyy("UP"):
        print("up pressed")
    if keyy("DOWN"):
        print("down pressed")

if __name__ =='__main__':
    init()
    while True:
        main()