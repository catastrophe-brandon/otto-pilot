
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
        """ Test prime(5) and make sure it returns [1, 2, 3, 5]. """
        result = self.prime.primes(stop=5)
        assert len(result) == 4, 'list of primes was expected to have length 4'
        assert result[0] == 1
        assert result[1] == 2
        assert result[2] == 3
        assert result[3] == 5

    def test_is_prime(self):
        assert self.prime.is_prime(5)
        assert self.prime.is_prime(7)

        assert not self.prime.is_prime(500)
        assert not self.prime.is_prime(280000)


class TestKnownPrimes(object):
    """Tests focused on the KnownPrimes class."""

    def setup_method(self):
        self.kp = KnownPrimes()

    def teardown_method(self):
        pass

    def test_initialization(self):
        KnownPrimes()

    def test_largest_known_prime(self):
        assert self.kp.largest_known_prime() == 23
        assert not self.kp.is_known(29)
        self.kp.add_prime(29)
        assert self.kp.is_known(29)
        assert self.kp.largest_known_prime() == 29

    def test_get_known_primes(self):
        assert self.kp.largest_known_prime() == 23
        assert len(self.kp.get_known_primes(max_value=23)) == 10
        assert len(self.kp.get_known_primes(max_value=24)) == 10
        assert len(self.kp.get_known_primes(max_value=25)) == 10
        assert len(self.kp.get_known_primes(max_value=26)) == 10
        assert len(self.kp.get_known_primes(max_value=27)) == 10
        assert len(self.kp.get_known_primes(max_value=28)) == 10

        assert len(self.kp.get_known_primes(max_value=22)) == 9


