import os

import gym
from gym import Env, spaces
from gym_culture.envs.cell import Cell

from itertools import count

def genID():
    for i in count(0):
        yield i

class GridWorldEnv(Env):
    def __init__(self, 
                 map='smallbox3.txt', 
                 res_count=5,
                 max_res_amount=100,
                 def_growth_rate=0.2,
                 to_color_cells=True):
        
        self.map = os.path.dirname(__file__) + "/assets/" + map
        self.res_count = res_count
        self.max_res_amount = max_res_amount
        self.def_cell_growth_rate = [def_growth_rate] * self.res_count
        self.to_color_cells = to_color_cells
        
        self.id = genID()

        with open(self.map) as f:
            lines = f.readlines()
        self.height = len(lines)
        self.width = max(len(line.rstrip()) for line in lines)
        
        self._reset()
        
        self.__load(self.map)
        
    def _reset(self):
        self.grid = [[Cell(self, x, y) for x in range(self.width)]
                     for y in range(self.height)]
        self.agents = []
        self.age = 0
    
    def _step(self, agent, action):
        dir, res = action
        #  do something
    
    def _render(self, cell_size=30):
        print("yolo!")
        #  use pygame here
    
    def __getColor(self, obj):
        pass
    
    def __load(self, map):
        with open(map) as f:
            lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        fh = len(lines)
        fw = max(len(line) for line in lines)
        
        if fh > self.height:
            fh = self.height
            starty = 0
        else:
            starty = (self.height - fh) // 2
        if fw > self.width:
            fw = self.width
            startx = 0
        else:
            startx = (self.width - fw) // 2
            
        #  just in case
        self._reset()
        
        for j in range(fh):
            line = lines[j]
            for i in range(min(fw, len(line))):
                self.grid[starty + j][startx + i].load(line[i])
        
    def getCell(self, x, y):
        return self.grid[y][x]
        
    def getWrappedCell(self, x, y):
        return self.grid[y % self.height][x % self.width]
