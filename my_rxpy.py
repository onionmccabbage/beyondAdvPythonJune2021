import rx
from rx import operators as ops

import requests # might need ot pip install requests
import json # from standard Python library

# filter to show only members beginning with chosen letter
def filterNames(x, l): # x is the item and l is the letter
    if (x['name'].startswith(l)):
        return x['name']
    else:
        return ''

def main():
    # ask the user which letter to find
    letter = input('Which letter? ')
    content = requests.get('https://jsonplaceholder.typicode.com/users') # make an API call
    y = json.loads(content.text) # we want the text paresed from JSON
    # use rx to make this an observable
    source = rx.from_(y)
    # use our observable
    case1 = source.pipe(
        ops.filter(lambda c: filterNames(c, letter)),
        ops.map(lambda a: a['name'])
    )
    # wire up subscriptions
    case1.subscribe(
        on_next      = lambda i: print('Received {}'.format(i)),
        on_error     = lambda e: print('Received Error: {}'.format(e)),
        on_completed = lambda: print('All done')
    )

if __name__ == '__main__':
    main()