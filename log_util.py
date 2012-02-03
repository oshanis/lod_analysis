import os 
from parse_tools import *

DB33_34_SWDF = 'db33_34_swdf'
DB36 = 'db36'
BIORDF = 'biordf'

class Log(object):
    
    def __init__(self, raw_text, folder, parse_syntax):
        self.folder = folder
        self.raw_text = raw_text
        self.parse_syntax = parse_syntax
        self.load()
        
    def to_dict(self):
        return self.ret
        
    def load(self):
        log = self.raw_text
        if self.parse_syntax == DB33_34_SWDF:
            self.ret = getLogLineBNF_DBpedia33().parseString(log)
        elif self.parse_syntax == DB36:
            self.ret = getLogLineBNF_DBpedia36().parseString(log)
             

class DirWalker(object):

    def __init__(self, root,syntax):
        self.root = root
        self.curdir = None
        self.skipped = 0
        self.parsed = 0
        self.syntax = syntax

    def __iter__(self):
        class DirIter():
            def __init__(self, walker):
                self.w = walker
                self.g = self.generator()
                
            def generator(self):
                for root, dir, files in os.walk(self.w.root):
                    folder = os.path.basename(root)
                    for fname in files:
                        print 'now process fname:',fname 
                        try:
                            with file(os.path.join(root, fname)) as f:
                                for line in f:
                                    yield Log(line, folder,self.w.syntax).to_dict() # very important bug....self.w.root not self.root
                            self.w.parsed += 1
                        except Exception as e:
                            self.w.skipped += 1
                            pass
                
            def next(self):
                for retval in self.g:
                    return retval
                raise StopIteration

        return DirIter(self)
    
if __name__ == '__main__':
    import sys
    
    w = DirWalker(sys.argv[1],DB33_34_SWDF)
    ip_country_dict = {} 
    for fields in w:
        (haship,country) = fields['hashIP'],fields['country']
        if ip_country_dict.has_key((haship, country)):
            ip_country_dict[(haship,country)] += 1
        else:
            ip_country_dict[(haship,country)] = 1

    print 'total:',sum(ip_country_dict.values())

    for k,v in ip_country_dict.items():
        print k, v
 