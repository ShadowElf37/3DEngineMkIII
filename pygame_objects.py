import pygame
from tools import htrgba
from PIL import Image

class Text:
    def __init__(self, x, y, text='', fg='#ffff', bg=None, font='Calibri', size=16):
        self.font = pygame.font.SysFont(font, size)
        self.fg = htrgba(fg)
        self.bg = htrgba(bg) if bg else bg
        self.text = text
        self.textbox = self.font.render(self.text, False, self.fg, self.bg)

        self.x = x
        self.y = y
        # self.textbox.get_rect().center = self.x, self.y

    def set_text(self, text):
        self.text = text
        self.textbox = self.font.render(self.text, False, self.fg, self.bg)

    def draw(self, display):
        self.update(display)
        display.surface.blit(self.textbox, (self.x, self.y))

    def update(self, display):
        pass


class FPSCounter(Text):
    def update(self, display):
        self.set_text('%.1f FPS' % display.get_fps())


class TestImage:
    def __init__(self, fp, x=0, y=0, resize=()):
        self.fp = fp
        self.img: Image.Image = Image.open(fp)
        self.size = resize or self.img.size
        self.x = x
        self.y = y
        if resize:
            self.img = self.img.resize(resize)

        self.render = pygame.image.frombuffer(self.img.tobytes('raw', 'RGB'), self.size, 'RGB')


    def draw(self, display):
        display.surface.blit(self.render, (self.x, self.y))
