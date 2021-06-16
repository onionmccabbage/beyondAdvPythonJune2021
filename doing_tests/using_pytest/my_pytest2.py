from collections import namedtuple

# we will declare a 'Task' named-tuple
Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])

# we can set sensible defaults for any Task
Task.__new__.__defaults__ = (None, None, False, None)

# here are some pyttests to exercise our named tuple
def test_default():
    '''using no parameters should invoke the defaults'''
    t1 = Task() # invoke defaults
    t2 = Task(None, None, False, None)
    assert t1 == t2

def test_member_access():
    '''Check the dot-notation access to members of a named tuple'''
    t = Task('have coffee', 'Ada')
    assert t.summary == 'have coffee'
    assert t.owner == 'Ada'
    assert (t.done, t.id) == (False, None)

