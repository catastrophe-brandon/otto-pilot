import logging
import sys

from prime import Prime

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def main(max_prime):
    """Parse the args and if all is good, summon Prime to do the computation."""
    logger.debug('Inside main()')
    print('Calculating prime numbers less than or equal to {}'.format(max_prime))
    primes = Prime().primes(stop=max_prime)
    print('Found {} prime numbers'.format(len(primes)))


if __name__ == '__main__':
    max_prime = int(sys.argv[1])
    print('You entered: {}'.format(max_prime))
    main(max_prime)

