"""
Mega Engineering Library - Chemical Engineering: Chemical Thermodynamics Module
Handles phase equilibria, vapor pressures, and multi-component system equations.
Validated against standard chemical thermodynamics literature (e.g., Smith, Van Ness, & Abbott).
"""

from englib.common.exceptions import PhysicalBoundaryError

class ChemicalThermodynamics:

    @staticmethod
    def calculate_raoult_partial_pressure(mole_fraction: float, pure_vapor_pressure: float) -> float:
        """
        Calculates the partial vapor pressure (Pi) of a component in an ideal liquid mixture using Raoult's Law.
        P_i = x_i * P_i_sat
        Unit: Pascals (Pa) or Bar
        """
        if mole_fraction < 0.0 or mole_fraction > 1.0:
            raise PhysicalBoundaryError("Liquid phase mole fraction (x) must be a strict ratio between 0.0 and 1.0.")
        if pure_vapor_pressure <= 0:
            raise PhysicalBoundaryError("Pure component saturation vapor pressure must be greater than zero.")

        return mole_fraction * pure_vapor_pressure
