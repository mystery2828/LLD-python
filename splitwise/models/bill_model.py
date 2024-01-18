class Bill(object):
    def __init__(self):
        self.id = None
        self.group = None
        self.contribution = {}
        self.paidBy = {}
    
    def setId(self,id):
        self.id = id
    
    def getId(self):
        return self.id

    def setGroup(self, group):
        self.group = group
    
    def getGroup(self):
        return self.group

    def setContribution(self, contribution):
        self.contribution = contribution
        
    def getContribution(self):
        return self.contribution

    def setPaidBy(self, paidBy):
        self.paidBy = paidBy
    
    def getPaidBy(self):
        return self.paidBy