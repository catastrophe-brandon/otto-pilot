import logging

logger = logging.getLogger(__name__)


class KnownPrimes(object):
    """ Serves as a means of preserving knowledge about known primes and checking if a new number is prime. """

    def __init__(self):
        """Initialize the instance with a starter set of known primes."""
        self.known_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

    def largest_known_prime(self):
        """Return the largest known prime number."""
        # We always assume the largest prime will be at the end of the list
        return self.known_primes[len(self.known_primes) - 1]

    def add_prime(self, new_prime):
        """Provide an external means of adding a new prime with some minimal validation."""
        # TODO: validate input type
        if not type(new_prime) == int:
            logger.error('Tried to add a non-integer to the list of known primes: {}'.format(new_prime))
            return

        if not self.check_primeness(new_prime):
            logger.error('You tried to add a value that was not prime, but I forgive you.')
            return

    def is_known(self, prime):
        """Not really needed, but makes the OOP fans feel safer."""
        return prime in self.known_primes

    def get_known_primes(self, max_value=10):
        """Return the list of known primes up to a specified max value."""
        # Make a copy so as not to expose the backing structure
        # TODO: there's a more efficient way to do this but I'm too tired to think of it atm :)
        known_primes_result = []
        for prime in self.known_primes:
            if prime <= max_value:
                known_primes_result.append(prime)
            else:
                break

        return known_primes_result

    def check_primeness(self, some_integer):
        """
        Call this if the primeness of a number is not already known.
        If the number is found to be prime it will be added to the list of known primes.
        :return True if some_integer is a prime number.
        """
        if some_integer % 2 == 0:
            return False

        if self.is_known(some_integer):
            return True

        # Ok, now we have to do real work. Le sigh.
        for prime in self.known_primes:
            if prime == 1:
                continue

            if some_integer % prime == 0:
                return False

        # Process of elimination
        self.known_primes.append(some_integer)
        return True


class Prime(object):
    """Encapsulate the logic for walking through the input list and searching for primes."""

    def __init__(self):
        self.known_primes = KnownPrimes()

    def is_prime(self, some_integer):
        """Returns True if some_integer is prime, false otherwise."""
        # TODO: nuke this method?
        if self.known_primes.is_known(some_integer):
            return True

        if self.known_primes.check_primeness(some_integer):
            return True

        return False

    def primes(self, stop=100):
        """
        Returns the list of all prime numbers between 1 and stop.
        :param stop the maximum value of the search range for primes
        :return a list of all the integers that are prime
        """

        logging.debug('Searching for all primes up to {}'.format(stop))
        if stop < 1:
            logging.info('Invalid request')
            return None

        start = self.known_primes.largest_known_prime() + 1
        if start >= stop:
            return self.known_primes.get_known_primes(max_value=stop)

        # Needed to help us skip checking all the even numbers.
        if start % 2 == 0:
            check_this = start + 1
        else:
            check_this = start

        while check_this <= stop:
            self.is_prime(check_this)
            check_this = check_this + 2

        return self.known_primes.get_known_primes(max_value=stop)
