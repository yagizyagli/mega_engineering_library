"""
Mega Engineering Library - Aerospace Engineering: Aerodynamics Module
Handles fluid-wing interactions, aerodynamic lift/drag forces, and compressible flow thresholds.
Validated against standard aeronautical engineering literature (e.g., Anderson's Introduction to Flight).
"""

from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class Aerodynamics:

    @staticmethod
    def calculate_aerodynamic_force(dynamic_pressure: float, wing_area: float, force_coefficient: float) -> float:
        """
        Calculates the aerodynamic lift or drag force acting on an aircraft wing configuration.
        F = q * S * C_f
        Where:
        q = Dynamic pressure (0.5 * rho * V^2)
        S = Wing planform area
        C_f = Dimensionless lift (Cl) or drag (Cd) coefficient
        Unit: Newtons (N)
        """
        if wing_area <= 0:
            raise GeometricViolationError("Aircraft wing planform area (S) must be a positive non-zero metric.")
        if dynamic_pressure < 0:
            raise PhysicalBoundaryError("Dynamic pressure (q) cannot be negative.")
        if force_coefficient < 0:
            # Sürüklenme veya kaldırma katsayıları teorik olarak sıfırın altına inmez (belirli ekstrem durumlar hariç)
            raise PhysicalBoundaryError("Aerodynamic force coefficients must be non-negative values.")

        return dynamic_pressure * wing_area * force_coefficient

    @staticmethod
    def calculate_mach_number(flow_velocity: float, speed_of_sound: float) -> float:
        """
        Calculates the dimensionless Mach Number (M) to define flight regimes.
        M = V / a
        Regimes:
        - M < 0.8: Subsonic
        - 0.8 <= M <= 1.2: Transonic
        - 1.2 < M <= 5.0: Supersonic
        - M > 5.0: Hypersonic
        """
        if speed_of_sound <= 0:
            raise PhysicalBoundaryError("Local speed of sound must be a positive non-zero velocity property.")
        if flow_velocity < 0:
            raise PhysicalBoundaryError("Aircraft true airspeed velocity cannot be negative.")

        return flow_velocity / speed_of_sound
