# we can implement threads by writing functions then decorating other functions

# here are some functions which will be used as decorators

def lock_class(methodnames, lockfactory):
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


def make_thread_safe():
    pass

@lock_class # decorate this class using lock_class function
class ClassDecoratedLockedSet(set):
    pass

def main():
    my_set = (4,3,2)
    my_inst = ClassDecoratedLockedSet(my_set)
    # is it locked?
    print('Is this locked: {}'.format(my_inst.add.__is_locked))
    # print(my_inst)

if __name__ == '__main__':
    main()