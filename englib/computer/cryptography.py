"""
Mega Engineering Library - Computer & Software Engineering: Cryptography Module
Handles mathematical foundations for secure communications, encryption keys, and modular math.
Validated against standard computer science cryptography literature (e.g., Stallings, Rivest-Shamir-Adleman formulas).
"""

from englib.common.exceptions import PhysicalBoundaryError

class ComputerCryptography:

    @staticmethod
    def calculate_greatest_common_divisor(a: int, b: int) -> int:
        """
        Calculates the Greatest Common Divisor (GCD) using the classical Euclidean Algorithm.
        Essential for finding coprime numbers during cryptographic public/private key generation.
        """
        a = abs(a)
        b = abs(b)
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def execute_modular_exponentiation(base: int, exponent: int, modulus: int) -> int:
        """
        Computes (base^exponent) % modulus efficiently for large numbers.
        Core mathematical operation for RSA encryption (C = M^e % n) and decryption (M = C^d % n).
        """
        if modulus <= 0:
            raise PhysicalBoundaryError("Modulus must be a positive non-zero integer for secure cryptographic operations.")
        if exponent < 0:
            raise PhysicalBoundaryError("Negative exponents are not supported in this discrete modular operation.")

        result = 1
        base = base % modulus
        
        while exponent > 0:
            if (exponent % 2) == 1:
                result = (result * base) % modulus
            exponent = exponent // 2
            base = (base * base) % modulus
            
        return result
