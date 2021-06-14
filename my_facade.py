
class Coder():
    def __init__(self):
        print('Bring coding skills')
    def __isAvailable__(self):
        print('coding skills are available')
        return True
    def bookTime(self):
        if self.__isAvailable__():
            print('coder booking made\n')

class Tester():
    def __init__(self):
        print('Preparing tests') 
    def testing(self):
        print('tests are in place')

class Artisan():
    def __init__(self):
        print('Designing stuff') 
    def makePrototype(self):
        print('Prototypes are ready')

class Technician():
    def __init__(self):
        print('Sound and vision for the team') 
    def doStuff(self):
        print('PA, Projector, Virtual Fridge')

class Manager(): # facade
    def __init__(self):
        print('manager says: I can arange the team')
    def arrange(self):
        self.tester = Tester()
        self.tester.testing()
        self.technician = Technician()
        self.technician.doStuff()
        self.coder = Coder()
        self.coder.bookTime()
        self.artisan = Artisan()
        self.artisan.makePrototype()

class You(): # client
    def __init__(self):
        print('we need a team ...')
    def askManager(self):
        print('lets contact the manager')
        m = Manager()
        m.arrange() # all done!
    def __del__(self):
        print('all done')

if __name__ == '__main__':
    you = You()
    you.askManager()
