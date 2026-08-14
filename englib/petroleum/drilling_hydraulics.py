"""
Mega Engineering Library - Petroleum Engineering: Drilling Hydraulics Module
Handles mud velocities, annular pressure drops, and equivalent circulating density profiles.
Validated against standard drilling engineering manuals (e.g., Bourgoyne's Applied Drilling Engineering).
"""

from englib.common.exceptions import PhysicalBoundaryError, GeometricViolationError

class DrillingHydraulics:

    @staticmethod
    def calculate_equivalent_circulating_density(static_mud_density_ppg: float, annular_pressure_loss_psi: float, true_vertical_depth_feet: float) -> float:
        """
        Calculates the Equivalent Circulating Density (ECD) of drilling fluids downhole.
        ECD = Mud_Density + Annular_Loss / (0.052 * TVD)
        Unit: Pounds per Gallon (ppg)
        """
        if true_vertical_depth_feet <= 0:
            raise GeometricViolationError("True Vertical Depth (TVD) of the wellbore must be a positive non-zero length measurement.")
        if static_mud_density_ppg <= 0:
            raise PhysicalBoundaryError("Static mud density constant must be greater than zero.")
        if annular_pressure_loss_psi < 0:
            raise PhysicalBoundaryError("Frictional annular pressure drop cannot be negative.")

        conversion_factor = 0.052
        hydrostatic_denominator = conversion_factor * true_vertical_depth_feet
        
        return static_mud_density_ppg + (annular_pressure_loss_psi / hydrostatic_denominator)
