# a computer may be on, off, suspend or hybernate
# not all states can be switched to all other states

class ComputerState:
    name = 'state'
    allowed = [] # a list of permitted states

class On(ComputerState):
    name='on'
    allowed = ['off', 'suspend', 'hybernate']

class Off(ComputerState):
    name='off'
    allowed = ['on']

class Suspend(ComputerState):
    pass

class Hybertnate(ComputerState):
    pass

class Computer():
    pass

if __name__ == '__main__':
    comp = Computer()
