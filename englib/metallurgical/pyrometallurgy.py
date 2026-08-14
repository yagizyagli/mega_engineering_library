"""
Mega Engineering Library - Metallurgical Engineering: Pyrometallurgy Module
Handles blast furnace heat balances, slag-metal chemical equilibria, and pyrometallurgical reduction math.
Validated against standard metallurgical engineering literature (e.g., Rosenqvist's Principles of Extractive Metallurgy).
"""

from englib.common.exceptions import PhysicalBoundaryError

class Pyrometallurgy:

    @staticmethod
    def calculate_slag_basicity_ratio(weight_percent_cao: float, weight_percent_sio2: float) -> float:
        """
        Calculates the baseline slag basicity ratio (V-value) crucial for steel refinery desulfurization loops.
        Basicity = %CaO / %SiO2
        """
        if weight_percent_sio2 <= 0:
            raise PhysicalBoundaryError("Silica (SiO2) weight percentage inside the slag matrix must be a positive non-zero value.")
        if weight_percent_cao < 0:
            raise PhysicalBoundaryError("Lime (CaO) composition cannot be negative.")

        return weight_percent_cao / weight_percent_sio2
