
from prime import prime
from prime import KnownPrimes


class TestPrime(object):
    """Tests focused on the Prime class."""

    def test_prime_happy(self):
        """Test prime() method on the happy path."""
        result = prime()
        assert True

    def test_prime_5(self):
        """ Test prime(5) and make sure it returns [1, 2, 3, 5]. """
        result = prime(5)
        assert len(result) == 4, 'list of primes was expected to have length 4'
        assert result[0] == 1
        assert result[1] == 2
        assert result[2] == 3
        assert result[4] == 5


class TestKnownPrimes(object):
    """Tests focused on the KnownPrimes class."""

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_initialization(self):
        KnownPrimes()
