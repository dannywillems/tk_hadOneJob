class GSFile(file):
    def countLine(self):
        self.seek(0) #Beginning of file
        for line in enumerate(self):
            pass
        self.seek(0) #Replace of the beginning of file
        return line[0]+1
    
    def fetchLine(self, line):
        if line <= 0:
            return None
    
        self.seek(0)
        for l, s in enumerate(self):
            if l+1 >= line:
                break
        self.seek(0)
        return s.strip()

