import datetime

class FileWrite:
    def __init__(self, filename):
        self.file = None
        self.opened = False
        self.filename = filename
        self.log = ''
        self.timestamp = None
    
    def __enter__(self):
        self.file = open(self.filename, 'r')
        self.opened = True
        self.timestamp = datetime.now().timestamp()
        msg = '{:<20}|{:<15}| OPEN \n'.format(timestamp,self.filename, diff)
        return self.file
    
    def __exit__(self, exc_type, exc_val? exc_tb):
        if self.opened:
            self.file.close()
            self.opened = False
    