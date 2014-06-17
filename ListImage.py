from urllib import urlopen
from bs4 import BeautifulSoup

from random import randint
from GSFile import *

from os import system

class ListImage(object):
    def __init__(self, update, f="hadOneJob.list"):
        self.URL = "http://hadonejob.com/"
        self.SEEN = []
        self.list = f
        
        if update:
            self.writeLink()
        
        self.length = GSFile(self.list).countLine()
        self.old = ""
    
    def writeLink(self):
        print "Update links from hadonejob.com. Don't be shy ! Add other websites"
        f = open(self.list, "w")
        a = self._sourcePage().find_all("img")
        for i in a:
            if "data-original" in i.attrs:
                if "\n" in i["data-original"]:
                    s = i["data-original"].split("/\n")
                else:
                    s = i["data-original"].split("/")
                s = "/full/".join(s)
                f.write(self.URL+s + "\n")
        f.close()
    
    def _sourcePage(self):
        return BeautifulSoup(urlopen(self.URL).read())
    
    def _hasRedAll(self):
        return len(self.SEEN) == self.length
  
    def _getRandInt(self):
        rdm = randint(1, self.length)        
        while rdm in self.SEEN:
            rdm = randint(1, self.length)       
        return rdm
    
    def _dlImg(self, link, rdm):
        s = ["wget", "-O", "img"+str(rdm)+".jpg", link]
        system(" ".join(s))
            
    def _rmOldImg(self):
        s = ["rm", self.old]
        system(" ".join(s))
        
    def getRandomImg(self):    
        if self._hasRedAll():
            self.SEEN = []
        
        rdm = self._getRandInt()
        self.SEEN.append(rdm)
        
        link = GSFile(self.list).fetchLine(rdm)
        self._dlImg(link, rdm)
        
        self._rmOldImg()
        
        self.old = "img"+str(rdm)+".jpg"
        
        return self.old        
