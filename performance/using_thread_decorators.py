# we can implement threads by writing functions then decorating other functions
from threading import Lock
# here are some functions which will be used as decorators

def lock_class(methodnames, lockfactory): # alternatively, we could iterate over any methods we introspect in the class
    return lambda cls: make_thread_safe(cls, methodnames, lockfactory)

def lock_method(method):
    if getattr(method, '__is_locked', False):
        raise TypeError('Method {} is already locked'.format(method))
    else:
        def locked_method(self, *args, **kwargs):
            with self._lock: # release when done
                return method(self, *args, **kwargs)
        lock_method.__name__ = '{}({})'.format('locked method', method.__name__)
        locked_method.__is_locked = True
        return locked_method

def make_thread_safe(cls, methodnames, lockfactory):
    init = cls.__init__
    def new_init(self, *args, **kwargs):
        init(self, *args, **kwargs)
        self.__lock = lockfactory
    cls.__init__ = new_init
    # iterate over the methods of this class, making the mthread safe
    for methodname in methodnames:
        oldmethod = getattr(cls, methodname)
        print(oldmethod)
        newmethod = lock_method(oldmethod)
        setattr(cls, methodname, newmethod)
        print('method {} is locked'.format(newmethod.__name__))
    return cls

# the decorator needs to pass the lock methods and the lock (provides the lockfactory)
@lock_class(['add', 'remove', 'methodToLock'], Lock) # decorate this class using lock_class function
class ClassDecoratedLockedSet(set): # nb this class does NOT descend from Thread
    # @lock_method # this method gets locked when the class is locked (as a parameter)
    def methodToLock(self): # nb the methods are not themselves threadsafe - only due to the decorator
        print('this method will be locked (and therefore thread-safe)')
    @lock_method # we didn't include this in the method list so we explicityl lock it now
    def otherMethodToLock(self):
        print('this other method will also be locked')
def main():
    my_set = (4,3,2)
    my_inst = ClassDecoratedLockedSet(my_set)
    # is it locked?
    print('Is this locked: {}'.format(my_inst.add.__is_locked))
    print(my_inst.add.__is_locked)
    print(my_inst.methodToLock.__is_locked)
    print(my_inst.otherMethodToLock.__is_locked)

if __name__ == '__main__':
    main()