import gym
from gym import Env, spaces

from cell import Cell

class GridWorldEnv(Env):
    def __init__(self, args):
        
        self.res_count = args.res_count
        self.max_res_amount = args.max_res_amount
        self.def_cell_growth_rate = [args.def_growth_rate] * self.res_count
        
        self.to_color_cells = args.to_color_cells
        
        with open(args.map) as f:
            temp_data = f.readlines()
        self.height = len(temp_data)
        self.width = max(len(x.rstrip()) for x in temp_data)
        
        self._reset()
        
        self.__load(map)
        
    def _reset(self):
        self.grid = [[Cell(self, x, y) for x in range(self.width)]
                     for y in range(self.height)]
        self.agents = []
        self.age = 0
    
    def _step(self, agent, action):
        dir, res = action
    
    def _render(self):
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
            line = lines[i]
            for i in range(min(fw, len(line))):
                self.grid[start + j][startx + i].load(line[i])
        
    def getCell(self, x, y):
        return self.grid[y][x]
        
    def getWrappedCell(self, x, y):
        return self.grid[y % self.height][x % self.width]
