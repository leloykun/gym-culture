class Cell():
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        
        self.wall = False
        self.agents = []
        self.resources = [self.world.max_res_amount 
                          for _ in range(self.world.res_count)]
    
    def color(self):
        if self.wall:
            return 'black'
        elif this.to_color_cells:
            ratio = sum(self.resources) / (self.world.max_res_amount * self.world.res_count)
            gradient = hex(int(ratio * 64) + 191)[2:]
            if len(gradient) < 2:
                gradient = '0' + gradient
            return '#ffff' + gradient
        else:
            return '#eeeff7'
    
    def load(self, data):
        if data == 'X':
            self.wall = True
            self.resources = [0 for _ in range(self.world.res_count)]
            self.growthRate = [1 for _ in range(self.world.res_count)]
        else:
            self.wall = False
            self.resources = [self.world.max_res_amount 
                              for _ in range(self.world.res_count)]
            self.growthRate = self.world.def_cell_growth_rate
    
    def update(self):
        if TO_UPDATE_CELLS:
            for i in range(self.world.res_count):
                self.resources[i] += self.world.max_res_amount * self.growthRate[i]
                # normalize
                self.resources[i] = min(self.resources[i], self.world.max_res_amount)
