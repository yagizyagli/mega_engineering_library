"""
Mega Engineering Library - Mining & Geological Engineering: Blasting Engineering Module
Handles explosive detonation dynamics, shock wave pressures, and rock fragmentation metrics.
Validated against standard mining explosive literature (e.g., Hustrulid's Blasting Principles).
"""

from englib.common.exceptions import PhysicalBoundaryError

class BlastingEngineering:

    @staticmethod
    def calculate_detonation_pressure(explosive_density_g_cm3: float, detonation_velocity_m_s: float) -> float:
        """
        Calculates the peak detonation pressure (P_det) of a commercial mining explosive charge.
        P_det = 2.5e-7 * rho * V_det^2
        Returns the pressure in Megapascals (MPa).
        """
        if explosive_density_g_cm3 <= 0:
            raise PhysicalBoundaryError("Explosive material density must be a positive non-zero value.")
        if detonation_velocity_m_s <= 0:
            raise PhysicalBoundaryError("Velocity of Detonation (VOD) must be a positive velocity profile.")

        # Imperial-to-Metric industry standard empirical transformation scaling factor: 2.5e-7
        return 2.5e-7 * explosive_density_g_cm3 * (detonation_velocity_m_s ** 2)
