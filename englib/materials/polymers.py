"""
Mega Engineering Library - Materials Science & Engineering: Polymer Technology Module
Handles polymer molecular weight profiles, polydispersity indexes, and polymer structural chain metrics.
Validated against standard macromolecular engineering guidelines.
"""

from englib.common.exceptions import PhysicalBoundaryError

class PolymerEngineering:

    @staticmethod
    def calculate_polydispersity_index(weight_average_mw: float, number_average_mn: float) -> float:
        """
        Calculates the Polydispersity Index (PDI) measuring the heterogeneity of polymer molecular weights.
        PDI = Mw / Mn
        Note: PDI is always >= 1.0; a value of 1.0 indicates a perfectly monodisperse polymer chain array.
        """
        if number_average_mn <= 0 or weight_average_mw <= 0:
            raise PhysicalBoundaryError("Polymer average molecular weights (Mw, Mn) must be positive values.")
        if weight_average_mw < number_average_mn:
            raise PhysicalBoundaryError("Physically impossible: Weight-average molecular weight (Mw) cannot be less than number-average (Mn).")

        return weight_average_mw / number_average_mn
