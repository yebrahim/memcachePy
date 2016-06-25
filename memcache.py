from collections import defaultdict

class Memcache(object):

    def __init__(self):
        self.d={}
        self.c=defaultdict(int)
        self.l=[]

    def set(self,k,v,logundo=True):
        d,c,l = self.d, self.c, self.l[-1] if len(self.l) else None
        oldv = d[k] if k in d else None
        d[k] = v
        if logundo and l is not None:
            if oldv: # we're changing the value
                # does this relog? do we care? we will probably just get rid of the whole thing
                l.append((self.set,k,oldv,False))
            else: # new value
                l.append((self.delete,k,False))
        if not oldv or v != oldv:
            c[v]+=1
            if oldv: c[oldv] -= 1

    def get(self,k):
        return self.d[k] if k in self.d else 'NULL'

    def delete(self,k,logundo=True):
        d,c,l = self.d, self.c, self.l[-1] if len(self.l) else None
        if k in d:
            if logundo and l is not None: l.append((self.set,k,d[k],False))
            v = d[k]
            del d[k]
            c[v]-=1

    def count(self,v):
        c = self.c
        return c.get(v,0)

    def begin(self):
        self.l.append([])

    def rollback(self):
        l = self.l[-1] if len(self.l) else None
        if l is not None:
            for command in l[::-1]:
                command[0](*command[1:])
            self.l.pop()
        else:
            return 'NO TRANSACTION'

    def commit(self):
        l = self.l[-1] if len(self.l) else None
        if l is not None: # get rid of all the undo logs
            self.l = []
        else:
            return 'NO TRANSACTION'


