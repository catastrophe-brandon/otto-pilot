
import logging

logger = logging.getLogger(__name__)


class KnownPrimes(object):

    def __init__(self):
        self.known_primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]

    def largest_known_prime(self):
        """Return the largest known prime number."""
        # We always assume the largest prime will be at the end of the list
        return self.known_primes[len(self.known_primes) - 1]

    def add_prime(self, new_prime):
        # TODO: validate input type
        if not type(new_prime) == int:
            logger.error('Tried to add a non-integer to the list of known primes: {}'.format(new_prime))
            return

        # TODO: validate input value > largest_known_prime
        if new_prime not in self.known_primes and new_prime > self.largest_known_prime():
            self.known_primes.append(new_prime)
        else:
            logger.warn('Tried to add a new prime, but it was already known: {}'.format(new_prime))

    def is_known(self, prime):
        """Not really needed, but makes the OOP fans feel safer."""
        return prime in self.known_primes


class Prime(object):

    def is_prime(self, some_integer):
        """Returns True if some_integer is prime, false otherwise."""
        # TODO: implement me
        return False


def prime(stop=100):
    """Returns the list of all prime numbers between 1 and stop."""

    logging.debug('Searching for all primes up to {}'.format(stop))
    if stop < 1:
        logging.info('Invalid request')
        return None


    return []
