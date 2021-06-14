# making use of Abstract Base Classes

from collections.abc import Container

class OddContainer:
    # does this contain an odd number?
    def __contains__(self, x):
        if not isinstance(x, int) or not x%2:
            return False
        return True

if __name__ == '__main__':
    print( Container.__abstractmethods__ )
    odd_c = OddContainer()
    print( isinstance(odd_c, Container) )
    print( issubclass(OddContainer, Container) )
    print( 1 in odd_c)
    print( 2 in odd_c)
    print( "1" in odd_c)