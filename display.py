import pygame
from multiprocessing import Queue
from queue import Empty


class Display:
    BLANK = (0, 0, 0)

    def __init__(self, w=700, h=500, fps=60, title='Game'):
        self.w = w
        self.h = h
        self.center = self.w//2, self.h//2
        self.fps = fps

        pygame.init()
        self.surface: pygame.Surface = pygame.display.set_mode((w, h))
        pygame.display.set_caption(title)
        self.running = False

        self.objects = []
        self.render_schedule = set()
        self.frame_buffer = Queue()
        self.clock = pygame.time.Clock()

    @property
    def size(self):
        return self.w, self.h
    def get_fps(self):
        return self.clock.get_fps()

    def push(self, string):
        self.frame_buffer.put(string)

    def register(self, obj):
        self.objects.append(obj)

    def add_render_function(self, func):
        self.render_schedule.add(func)
    def remove_render_function(self, func):
        self.render_schedule.remove(func)

    def mainloop(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            try:
                data = self.frame_buffer.get_nowait()
                self.surface.fill(self.BLANK)
                render = pygame.image.frombuffer(data, self.size, 'RGB')
                self.surface.blit(render, (0, 0))
            except Empty:
                pass

            for obj in self.objects:
                obj.draw(self)
            for func in self.render_schedule:
                func()

            pygame.display.flip()
            self.clock.tick(self.fps)
