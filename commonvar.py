class Bridge():
    def __init__(self):
        self.name = []
        self.var = []
        self.count = 0
        self.requests = []
        self.tempgrab = []
    def setvar(self,name, data):
        self.name.append(str(name))
        self.var.append(data)
    def getvar(self, name):
        for i in range(len(self.name)):
            self.count = i
            if self.name[i] == str(name):
                return self.var[self.count]
    def updatevar(self,name,data):
        for i in range(int(len(self.name))):
            self.count = i
            if self.name[i] == str(name):
                self.var[i] = data
    def request(self, main,command,insert):
        self.requests.append([main,command,insert])
    def grab(self, program):
        self.tempgrab = []
        for i in self.requests:
            if i[0] == str(program):
                self.tempgrab.append([i[1],i[2]])
        return self.tempgrab
    def solve(self, main,command,insert):
        self.requests.remove([main,command,insert])
bridge = Bridge()