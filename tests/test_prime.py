
from prime import KnownPrimes, Prime


class TestPrime(object):
    """Tests focused on the Prime class."""

    def setup_method(self):
        self.prime = Prime()

    def test_prime_happy(self):
        """Test prime() method on the happy path."""
        result = self.prime.primes()
        assert result is not None
        assert True

    def test_prime_5(self):
        """ Test prime(5) and make sure it returns [2, 3, 5]. """
        result = self.prime.primes(stop=5)
        assert len(result) == 3, 'list of primes was expected to have length 3'
        assert result[0] == 2
        assert result[1] == 3
        assert result[2] == 5

    def test_is_prime(self):
        assert self.prime.is_prime(5)
        assert self.prime.is_prime(7)

        assert not self.prime.is_prime(500)
        assert not self.prime.is_prime(280000)

    def test_primes(self):
        result = self.prime.primes(stop=100000)
        print(result)

    def test_primes_between(self):
        result = self.prime.primes_between(1, 5)

        expected_result = [2, 3]
        assert result == expected_result, 'Expected list of primes did not match'

        expected_result = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
        result = self.prime.primes_between(5, 97)
        assert result == expected_result, 'Expected list of primes did not match'

        # When min and max yield an empty set, we should get an empty list
        result = self.prime.primes_between(4, 5)
        assert result == [], 'Result should have been an empty list'


class TestKnownPrimes(object):
    """Tests focused on the KnownPrimes class."""

    def setup_method(self):
        self.kp = KnownPrimes()

    def teardown_method(self):
        pass

    def test_initialization(self):
        KnownPrimes()

    def test_largest_known_prime(self):
        """
        Confirm that mutating the list of largest known primes works in the following cases.
        1. Checking the largest value prior to expansion. (23)
        2. Add a new, larger prime into the list, confirm it is known.
        3. Confirm the newly added larger prime is returned as the largest known prime.
        4. Try adding a non-prime into the list causes the list to remain unaltered.
        """
        assert self.kp.largest_known_prime() == 23
        assert not self.kp.is_known(29)
        self.kp.add_prime(29)
        assert self.kp.is_known(29)
        assert self.kp.largest_known_prime() == 29
        self.kp.add_prime(30)
        assert not self.kp.is_known(30)
        assert not self.kp.largest_known_prime() == 30

    def test_get_known_primes(self):
        assert self.kp.largest_known_prime() == 23
        assert len(self.kp.get_known_primes(max_value=23)) == 9
        assert len(self.kp.get_known_primes(max_value=24)) == 9
        assert len(self.kp.get_known_primes(max_value=25)) == 9
        assert len(self.kp.get_known_primes(max_value=26)) == 9
        assert len(self.kp.get_known_primes(max_value=27)) == 9
        assert len(self.kp.get_known_primes(max_value=28)) == 9

        assert len(self.kp.get_known_primes(max_value=22)) == 8

    def test_check_primeness(self):
        """Check all the even numbers from 2 through 10000 to see if they are prime."""
        primes = [3, 5, 7, 11]
        for prime in primes:
            assert self.kp.check_primeness(prime), 'Thinks {} is not prime'.format(prime)

        # confirm order doesn't matter
        primes = [11, 7, 5, 3]
        for prime in primes:
            assert self.kp.check_primeness(prime)

        even_number = 2
        while even_number <= 10000:
            assert not self.kp.check_primeness(even_number)
            even_number = even_number + 2

        assert self.kp.check_primeness(29)


