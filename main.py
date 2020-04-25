import display
from tools import htrgba
from pygame_objects import FPSCounter, TestImage
from PIL import Image

screen = display.Display(700, 500, title='3D Engine MkIII')
#i: Image.Image = Image.open('gold_block.png')
#i = i.resize(screen.size)
#screen.push(i.tobytes('raw', 'RGB'))
screen.register(TestImage('gold_block.png', resize=(700, 500)))
screen.register(FPSCounter(10, 10, fg='#00ff'))

screen.mainloop()
