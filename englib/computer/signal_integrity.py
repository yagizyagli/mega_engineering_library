"""
Mega Engineering Library - Computer & Software Engineering: Signal Integrity Module
Handles high-speed transmission lines, signal reflections, and characteristic impedance models.
Validated against standard high-speed digital design literature (e.g., Johnson & Graham, Bogatin).
"""

import math
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class SignalIntegrity:

    @staticmethod
    def calculate_microstrip_characteristic_impedance(dielectric_constant: float, trace_width: float, dielectric_height: float) -> float:
        """
        Calculates the approximate characteristic impedance (Z0) of a PCB microstrip transmission line.
        Based on IPC standard equations (simplified for common structural ratios).
        Unit: Ohms (Omega)
        """
        if trace_width <= 0 or dielectric_height <= 0:
            raise GeometricViolationError("PCB physical trace dimensions (width and height) must be greater than zero.")
        if dielectric_constant <= 1.0:
            raise PhysicalBoundaryError("Relative dielectric constant (epsilon_r) must be greater than 1.0 (vacuum benchmark).")

        # Simplified empirical formula for modern PCB manufacturing standards
        numerator = 87.0
        denominator = math.sqrt(dielectric_constant + 1.41)
        log_term = math.log((5.98 * dielectric_height) / (0.8 * trace_width + 0.1)) # standard trace thickness assumed
        
        try:
            return (numerator / denominator) * log_term
        except ValueError:
            raise GeometricViolationError("Impossible microstrip geometry parameters resulting in math domain errors.")

    @staticmethod
    def calculate_reflection_coefficient(load_impedance: float, source_impedance: float) -> float:
        """
        Calculates the dimensionless voltage reflection coefficient (Gamma) at a high-speed transmission link boundary.
        Gamma = (Z_load - Z_source) / (Z_load + Z_source)
        Values range strictly between -1.0 and 1.0.
        """
        if load_impedance <= 0 or source_impedance <= 0:
            raise PhysicalBoundaryError("Electrical impedances must be positive non-zero values.")
            
        denominator = load_impedance + source_impedance
        if denominator == 0:
            raise ZeroDivisionError("Impedance mismatch calculation yielded a division by zero anomaly.")
            
        return (load_impedance - source_impedance) / denominator
