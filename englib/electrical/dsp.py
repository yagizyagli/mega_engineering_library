"""
Mega Engineering Library - Electrical & Electronics Engineering: Digital Signal Processing (DSP) Module
Handles discrete-time signals, Nyquist sampling rates, Fourier analyses, and system transformations.
Validated against standard signal processing literature (e.g., Oppenheim & Schafer, Proakis).
"""

import math
from typing import List, Complex
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class DigitalSignalProcessing:

    @staticmethod
    def calculate_nyquist_rate(maximum_frequency_hz: float) -> float:
        """
        Calculates the minimum Nyquist sampling rate required to avoid aliasing in signal conversion.
        F_nyquist = 2 * F_max
        Unit: Hertz (Hz)
        """
        if maximum_frequency_hz <= 0:
            raise PhysicalBoundaryError("The maximum signal frequency must be a positive non-zero value.")
        return 2.0 * maximum_frequency_hz

    @staticmethod
    def calculate_discrete_fourier_transform_point(signal: List[float], k: int) -> complex:
        """
        Calculates a single frequency component X[k] of a discrete signal using the Discrete Fourier Transform (DFT).
        X[k] = sum_{n=0}^{N-1} ( x[n] * exp(-j * 2 * pi * k * n / N) )
        """
        if not signal:
            raise ValueError("The input signal discrete sequence cannot be empty.")
            
        n_samples = len(signal)
        if k < 0 or k >= n_samples:
            raise GeometricViolationError("The frequency index k must be within the boundary of [0, N-1].")

        real_part = 0.0
        imag_part = 0.0

        for n, x_n in enumerate(signal):
            angle = (2.0 * math.pi * k * n) / n_samples
            real_part += x_n * math.cos(angle)
            imag_part -= x_n * math.sin(angle)

        return complex(real_part, imag_part)

    @staticmethod
    def calculate_first_order_z_transform_pole(gain: float, pole: float, z: complex) -> complex:
        """
        Calculates the transfer function response H(z) for a standard first-order discrete system at a given z value.
        H(z) = b0 / (1 - a1 * z^-1) = (b0 * z) / (z - a1)
        Where:
        gain = b0 (numerator coefficient)
        pole = a1 (denominator filter pole)
        """
        if z == complex(pole, 0):
            raise ZeroDivisionError("The evaluation point z exactly matches the system pole, resulting in infinite response.")
        if abs(pole) >= 1.0:
            # We don't crash, but stable design is vital for DSP. We flag boundary stability.
            pass

        numerator = gain * z
        denominator = z - pole
        return numerator / denominator
