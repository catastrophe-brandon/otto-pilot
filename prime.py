import copy
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
            return

    def is_known(self, prime):
        """Not really needed, but makes the OOP fans feel safer."""
        return prime in self.known_primes

    def get_known_primes(self, max_value=10):
        """Return the list of known primes."""
        # Make a copy so as not to expose the backing structure
        known_primes_result = []
        for prime in self.known_primes:
            if prime <= max_value:
                known_primes_result.append(prime)
            else:
                break

        return known_primes_result


class Prime(object):

    def __init__(self):
        self.known_primes = KnownPrimes()

    def is_prime(self, some_integer):
        """Returns True if some_integer is prime, false otherwise."""
        if self.known_primes.is_known(some_integer):
            return True

        if self._check_primeness(some_integer):
            return True

        return False

    def _check_primeness(self, some_integer):
        """Call this if the prime is not already known."""
        if some_integer % 2 == 0:
            return False

        # Ok, now we have to do real work. Le sigh.
        for prime in self.known_primes.get_known_primes():
            if some_integer % prime == 0:
                return False

        # Process of elimination
        self.known_primes.add_prime(some_integer)
        return True

    def primes(self, stop=100):
        """Returns the list of all prime numbers between 1 and stop."""

        logging.debug('Searching for all primes up to {}'.format(stop))
        if stop < 1:
            logging.info('Invalid request')
            return None

        start = self.known_primes.largest_known_prime() + 1
        if start >= stop:
            return self.known_primes.get_known_primes(max_value=stop)

        check_this = start
        while check_this <= stop:
            self.is_prime(check_this)
            check_this = check_this + 1

        return self.known_primes.get_known_primes(max_value=stop)
