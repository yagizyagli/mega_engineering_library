"""
Mega Engineering Library - Chemical Engineering: Process Heat Transfer Module
Handles design metrics for chemical plant heat exchangers and thermal equipment.
Validated against standard heat transfer manuals (e.g., Kern's Process Heat Transfer).
"""

import math
from englib.common.exceptions import PhysicalBoundaryError

class ChemicalHeatTransfer:

    @staticmethod
    def calculate_log_mean_temperature_difference(delta_t1: float, delta_t2: float) -> float:
        """
        Calculates the Logarithmic Mean Temperature Difference (LMTD) for heat exchanger profiles.
        LMTD = (delta_t1 - delta_t2) / ln(delta_t1 / delta_t2)
        Unit: Kelvin (K) or Celsius (°C)
        """
        if delta_t1 <= 0 or delta_t2 <= 0:
            raise PhysicalBoundaryError("Temperature driving forces (delta_t) at both exchanger ends must be positive.")
        
        if delta_t1 == delta_t2:
            # Mathematical guard for identical boundaries to prevent division by zero
            return delta_t1

        numerator = delta_t1 - delta_t2
        denominator = math.log(delta_t1 / delta_t2)
        return numerator / denominator
