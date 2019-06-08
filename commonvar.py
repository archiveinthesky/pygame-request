class Bridge():
    def __init__(self):
        self.name = []
        self.var = []
        self.count = 0
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
bridge = Bridge()