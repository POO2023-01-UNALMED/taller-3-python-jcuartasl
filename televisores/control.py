class Control:

    def __init__(self):
        self.tv = None
        
    def enlazar(self, tv):
        self.tv = tv
        tv.setControl(self)

    def getTV(self):
        return self.tv
    def setTV(self,tv):
        self.tv = tv
    
    def setCanal(self, cn):
            self.tv.setCanal(cn)
    
    def turnOn(self):
        self.tv.turnOn()
    def turnOff(self):
        self.tv.turnOff()

    def canalUp(self):
        self.tv.canalUp()
    def canalDown(self):
        self.tv.canalDown()
    
    def volumenUp(self):
        self.tv.volumenUp()
    def volumenDown(self):
        self.tv.volumenDown()

