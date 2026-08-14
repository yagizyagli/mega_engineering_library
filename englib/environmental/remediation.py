"""
Mega Engineering Library - Environmental Engineering: Groundwater Remediation Module
Handles subsurface contaminant transport tracking and aquifer seepage velocities.
Validated against standard hydrogeology literature (e.g., Freeze & Cherry).
"""

from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class GroundwaterRemediation:

    @staticmethod
    def calculate_seepage_velocity(hydraulic_conductivity: float, hydraulic_gradient: float, effective_porosity: float) -> float:
        """
        Calculates the actual contaminant seepage velocity (Vs) through a porous soil/rock aquifer section.
        Based on Darcy's Law and porous medium mechanics.
        Vs = (K * i) / n_eff
        Unit: Meters per day (m/day) or meters per second (m/s)
        """
        if effective_porosity <= 0.0 or effective_porosity > 1.0:
            raise PhysicalBoundaryError("Effective soil porosity (n) must be a bounded ratio strictly between 0.0 and 1.0.")
        if hydraulic_conductivity <= 0:
            raise PhysicalBoundaryError("Aquifer hydraulic conductivity (K) must be a positive physical parameter.")
        if hydraulic_gradient < 0:
            raise GeometricViolationError("Hydraulic gradient (i) cannot be negative for physical gravity transport flow mapping.")

        return (hydraulic_conductivity * hydraulic_gradient) / effective_porosity
