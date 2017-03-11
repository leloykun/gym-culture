class Cell():
    wall = False
    #  placeholder
    resources = [100] * 5
    
    def color(self):
        if self.wall:
            return 'black'
        else:
            ratio = sum(self.resources) / (self.world.max_res_amount * self.world.res_count)
            gradient = hex(int(ratio * 64) + 191)[2:]
            if len(gradient) < 2:
                gradient = '0' + gradient
            return '#ffff' + gradient
            #      '#eeeff7'
    
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
        for i in range(self.world.res_count):
            self.resources[i] += self.world.max_res_amount * self.growthRate[i]
            # normalize
            self.resources[i] = min(self.resources[i], self.world.max_res_amount)
