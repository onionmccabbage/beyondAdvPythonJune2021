import logging
from multiprocessing import Pool

# we need to set defaults for our logging
logging.basicConfig(filename='my_log', level=logging.DEBUG, # or INFO 
        format='%(processName)s %(asctime)s %(levelname)s %(message)s')

def myTask(n):
    r = n*2
    logging.info('{} being processed'.format(n))
    logging.debug('Final result: {}'.format(r))
    return r

def main():
    # invoke a pool of processes
    with Pool(4) as p:
        p.map(myTask, [8,7,6,5,4,3,2])

if __name__ == '__main__':
    main()
