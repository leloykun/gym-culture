import os
import random
from itertools import count

import gym
from gym import Env, spaces
from gym_culture.envs.cell import Cell
from gym_culture.envs.display import PygameDisplay

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
        
        with open(self.map) as f:
            lines = f.readlines()
        self.height = len(lines)
        self.width = max(len(line.rstrip()) for line in lines)
        
        self.id = genID()
        self.display = self.__make_display()
        
        self._reset()
        
        self.__load(self.map)
        
    def _reset(self):
        self.grid = [[self.__make_cell(x, y) for x in range(self.width)]
                     for y in range(self.height)]
        self.dictBackup = [[{} for x in range(self.width)]
                           for y in range(self.height)]
        self.agents = []
        self.age = 0
    
    def _step(self, agent, action):
        dir, res = action
        
        cell = self.get_wrapped_cell(agent.cell.x + dir[0], 
                                     agent.cell.y + dir[1])
        
        agent.work(cell, res)
        agent.eat()
        
        return agent.calc_state(), agent.calc_reward(), None, None
    
    def _render(self, cell_size=30):
        print("yolo!")
        if not self.display.activated:
            self.display.activate(size=30)
            self.display.delay = 1
        self.display.redraw()
        self.display.update()
    
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
    
    def __make_display(self):
        d = PygameDisplay()
        d.world = self
        return d
    
    def __make_cell(self, x, y):
        c = Cell()
        c.x = x
        c.y = y
        c.resources = [self.max_res_amount 
                       for _ in range(self.res_count)]
        c.world = self
        c.agents = []
        return c
    
    def get_cell(self, x, y):
        return self.grid[y][x]
        
    def get_wrapped_cell(self, x, y):
        return self.grid[y % self.height][x % self.width]
    
    def pick_randon_cell(self):
        while True:
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            cell = self.get_cell(x, y)
            if not cell.wall and len(cell.agents) < self.res_count:
                return cell
    
    def add_agent(self, agent, cell=None):
        if cell is None:
            cell = self.pick_randon_cell()
        
        self.agents.append(agent)
        agent.env = self
        agent.id = next(self.id)
        agent.cell = cell
        
    def remove_agent(self, agent):
        self.agents.remove(agent)
        agent.cell.agents.remove(agent)
    