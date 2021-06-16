import collections
# we can use a double-ended queue
my_deq = collections.deque('123456')

# alter elements of the deque

my_deq.append('11')
my_deq.appendleft(False)
my_deq.pop()
my_deq.popleft()

print('Deque: {}'.format(my_deq))