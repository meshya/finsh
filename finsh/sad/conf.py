from django.conf import settings
def log(string):
    
    with open(settings.BASE_DIR/'log.txt','ab+') as f:
        f.write(string.encode('UTF-8'))
        f.write('\n'.encode('UTF-8'))
        f.close()
    
    #print(f'__finshlognow__:::{string}')

import termcolor
class c :
    @classmethod
    def red (cls,text):
        return termcolor.colored(text,'red')
    @classmethod
    def blue (cls,text):
        return termcolor.colored(text,'blue')
    @classmethod
    def yellow (cls,text):
        return termcolor.colored(text,'yellow')
    @classmethod
    def grey (cls,text):
        return termcolor.colored(text,'grey')
    @classmethod
    def green (cls,text):
        return termcolor.colored(text,'green')

