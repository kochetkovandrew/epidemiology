class Rk4:

    state = {}
    data = []
    h = 1
    x = ''
    y = []
    funcs = {}


    def __init__(self, init_list):
        self.h = init_list['h']
        self.x = list(init_list['x'].keys())[0]
        self.y = list(init_list['y'].keys())
        self.state = {self.x: init_list['x'][self.x]}
        for key in self.y:
            self.state[key] = init_list['y'][key]['value']
        self.data.append(self.state)
        self.funcs = {}
        for key in self.y:
            self.funcs[key] = init_list['y'][key]['func']


    def step(self):
        diff1 = {}
        for key in self.y:
            diff1[key] = self.h * self.funcs[key](self.state)
        arg = {self.x: self.state[self.x] + self.h / 2}
        for key in self.y:
            arg[key] = self.state[key] + diff1[key] / 2
        diff2 = {}
        for key in self.y:
            diff2[key] = self.h * self.funcs[key](arg)
        arg = {self.x: self.state[self.x] + self.h / 2}
        for key in self.y:
            arg[key] = self.state[key] + diff2[key] / 2
        diff3 = {}
        for key in self.y:
            diff3[key] = self.h * self.funcs[key](arg)
        arg = {self.x: self.state[self.x] + self.h}
        for key in self.y:
            arg[key] = self.state[key] + diff3[key]
        diff4 = {}
        for key in self.y:
            diff4[key] = self.h * self.funcs[key](arg)
        new_state = {self.x: self.state[self.x] + self.h}
        for key in self.y:
            new_state[key] = self.state[key] + (diff1[key] + 2*diff2[key] + 2*diff3[key] + diff4[key]) / 6
        self.data.append(new_state)
        self.state = new_state
