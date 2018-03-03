import logging
import sys

from prime import Prime

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def main(min_prime, max_prime):
    """Parse the args and if all is good, summon Prime to do the computation."""
    logger.debug('Inside main()')
    print('Calculating prime numbers between {} and {}'.format(min_prime, max_prime))
    primes = Prime().primes_between(start=min_prime, stop=max_prime)
    print('Found {} prime numbers'.format(len(primes)))
    print(primes)


def help():
    """Print any relevant help message required to tell the user what to do next."""
    print('Example: python main.py 1 100')


if __name__ == '__main__':

    try:
        int(sys.argv[1])
    except IndexError:
        print('The first value you gave was not an integer')
        help()
        exit(1)

    try:
        int(sys.argv[2])
    except IndexError:
        print('The second value you gave was not an integer.')
        help()
        exit(1)

    min_prime = int(sys.argv[1])
    max_prime = int(sys.argv[2])

    if max_prime <= min_prime:
        print('You needed to give a max value that is larger than the min value')
        exit(1)

    print('You entered: min={} max={}'.format(min_prime, max_prime))
    main(min_prime, max_prime)

