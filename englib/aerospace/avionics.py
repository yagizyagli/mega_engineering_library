"""
Mega Engineering Library - Aerospace Engineering: Avionics & Navigation Module
Handles radar range profiles, flight instrument mathematical tracking, and navigation metrics.
Validated against standard avionics engineering guidelines and textbooks.
"""

import math
from englib.common.exceptions import PhysicalBoundaryError

class AvionicsGNC:

    @staticmethod
    def calculate_maximum_radar_range(peak_power_transmitted: float, antenna_gain: float, radar_cross_section: float, minimum_detectable_signal: float) -> float:
        """
        Calculates the maximum tracking range (R_max) using the fundamental Radar Range Equation.
        R_max = ( (Pt * G^2 * sigma * lambda^2) / ((4 * pi)^3 * Pmin) ) ^ (1/4)
        For simplicity inside this module, assuming a fixed carrier wavelength lambda = 0.03 meters (X-band radar).
        Unit: Meters (m)
        """
        if peak_power_transmitted <= 0 or antenna_gain <= 0 or radar_cross_section <= 0:
            raise PhysicalBoundaryError("Radar active physical cross sections and transmit powers must be positive.")
        if minimum_detectable_signal <= 0:
            raise PhysicalBoundaryError("Receiver sensitivity threshold (Pmin) must be a positive non-zero power level.")

        lambda_wave = 0.03  # Standard 10 GHz radar wave model selection
        numerator = peak_power_transmitted * (antenna_gain ** 2) * radar_cross_section * (lambda_wave ** 2)
        denominator = ((4.0 * math.pi) ** 3) * minimum_detectable_signal
        
        return (numerator / denominator) ** 0.25
