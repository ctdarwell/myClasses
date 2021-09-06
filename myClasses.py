#this inherits Python dict but reap returns a default instead of get's None type
# ***ALWAYS*** put in C:\Users\Windows\Anaconda3\Lib\site-packages

#modifies list.remove(), list.index() & provides set() & wildcard()
class xList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__list__ = self

    def rest(self, qw): #alt to remove()
        return xList([x for x in self if x != qw])
    
    def update_rm(self, qw): #cf. remove()
        self[:] = [x for x in self if x != qw] #this updates self
        return self

    def indxs(self, qw): #yield all indexes - cf. index()
        return xList([x for x in range(len(self)) if self[x] == qw])

    def items(self): #yields xl set
        return xList(list(set(self))) #set as a list
    
    def wildcard(self, w): #yield wildcard in list strings
        try: return xList([x for x in self if w in x])
        except: print("Incorrect data type. <None> returned!")


class xDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.out = 0

    def reap(self, qw):
        if qw not in self.keys(): return self.out
        else: return self.get(qw)
        
    def modify(self, qw):
        self.out = qw
