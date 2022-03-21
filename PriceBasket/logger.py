import time

class Logger:
    enabled = False
    info = 'INFO'
    warning = 'WARNING'
    error = 'ERROR'   

    def log(self, message, level=info):        
        if self.enabled:
            now = time.strftime('%Y-%m-%d %H:%M:%S')
            print('{} {}: {}'.format(now, level, message))