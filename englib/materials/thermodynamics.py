"""
Mega Engineering Library - Materials Science & Engineering: Materials Thermodynamics Module
Handles alloy phase diagrams, weight fractions, and phase transition equilibria.
Validated against standard metallurgical thermodynamics manuals.
"""

from englib.common.exceptions import PhysicalBoundaryError

class MaterialsThermodynamics:

    @staticmethod
    def calculate_lever_rule_liquid_fraction(overall_composition: float, alpha_composition: float, liquid_composition: float) -> float:
        """
        Calculates the weight fraction of the liquid phase (Wl) in a binary alloy system using the Lever Rule.
        Wl = (C_alpha - C0) / (C_alpha - C_liquid)
        Returns a decimal weight fraction between 0.0 and 1.0.
        """
        if overall_composition < 0 or alpha_composition < 0 or liquid_composition < 0:
            raise PhysicalBoundaryError("Alloy elemental composition weight values cannot be negative numbers.")
            
        denominator = alpha_composition - liquid_composition
        if denominator == 0:
            raise ZeroDivisionError("Phase boundary compositions are identical; Lever Rule division by zero.")

        liquid_fraction = (alpha_composition - overall_composition) / denominator
        
        if liquid_fraction < 0.0 or liquid_fraction > 1.0:
            raise PhysicalBoundaryError("Composition values yield a physically impossible phase weight ratio outside [0, 1].")
            
        return liquid_fraction
