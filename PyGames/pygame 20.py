import pygame, sys, random
from pygame.locals import *

pygame.init()

width = 800
height = 600
input_text = ''
typing = False

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Type Speed Program")


def print_text(screen, massage, x, y, font_s, clr):
    font = pygame.font.Font(None, font_s)
    text = font.render(massage, True, clr)
    screen.blit(text, (x, y))
    pygame.display.update()


def get_sentence():
    t_f = open('sentences.txt').read()
    sentences = t_f.split("\n")
    sentence = random.choice(sentences)
    return sentence


def start_game():
    sentence_s = get_sentence()
    print_text(win, sentence_s, 100, 250, 40, (255, 0, 0))
    pygame.draw.rect(win, (255, 255, 0), (75, 300, 650, 50), 3)
    pygame.display.update()


start_game()


while True:
    win.fill((0, 0, 0), (75, 300, 650, 50))
    print_text(win, input_text, 80, 310, 35, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if event.button == 1:
                if (75 <= x <= 725) and (300 <= y <= 350):
                    typing = True
                    input_text = ''
        elif event.type == KEYDOWN:
            if typing:
                if event.key == K_RETURN:
                    print(input_text)
                if event.key == K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
    print_text(win, "Typing Speed", 150, 100, 100, (0, 255, 255))
    pygame.display.update()
