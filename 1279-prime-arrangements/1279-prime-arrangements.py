class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7

        # Function to calculate the factorial of a number modulo MOD
        def factorial(num):
            result = 1
            for i in range(1, num + 1):
                result = (result * i) % MOD
            return result

        # Function to check if a number is prime
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        prime_count = sum(1 for i in range(1, n + 1) if is_prime(i))
        non_prime_count = n - prime_count

        # Calculate the number of valid permutations of prime numbers and non-prime numbers
        result = (factorial(prime_count) * factorial(non_prime_count)) % MOD

        return result

