"""
Mega Engineering Library - Mechanical Engineering: Manufacturing Technology Module
Provides formulations for metal cutting economics, machining operations, and casting kinetics.
Validated against standard manufacturing processes literature (e.g., Groover, Kalpakjian).
"""

import math
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class ManufacturingTechnology:

    @staticmethod
    def calculate_cutting_speed_turning(diameter_mm: float, rpm: float) -> float:
        """
        Calculates the linear cutting speed (V) in a lathe turning operation.
        V = (pi * D * N) / 1000
        Returns cutting speed in meters per minute (m/min).
        """
        if diameter_mm <= 0:
            raise GeometricViolationError("Workpiece diameter must be greater than zero.")
        if rpm <= 0:
            raise GeometricViolationError("Spindle rotational speed (RPM) must be positive.")

        return (math.pi * diameter_mm * rpm) / 1000.0

    @staticmethod
    def calculate_material_removal_rate_turning(cutting_speed_m_min: float, feed_mm_rev: float, depth_of_cut_mm: float) -> float:
        """
        Calculates the Material Removal Rate (MRR) for traditional lathe turning.
        MRR = V * f * d * 1000
        Returns MRR in cubic millimeters per minute (mm³/min).
        """
        if cutting_speed_m_min < 0 or feed_mm_rev < 0 or depth_of_cut_mm < 0:
            raise PhysicalBoundaryError("Machining feed, depth, and speed parameters cannot be negative.")

        # Converting speed to mm/min internally (V * 1000)
        return cutting_speed_m_min * 1000.0 * feed_mm_rev * depth_of_cut_mm

    @staticmethod
    def calculate_casting_solidification_time(volume: float, surface_area: float, mold_constant: float, exponent: float = 2.0) -> float:
        """
        Calculates total solidification time (T) of a metal casting using Chvorinov's Rule.
        T = B * (V / A)^n
        Where:
        B = Mold constant (s/mm² or min/mm²)
        V = Volume of the casting
        A = Surface area of the casting
        n = Exponent (typically 2.0)
        """
        if volume <= 0 or surface_area <= 0:
            raise GeometricViolationError("Casting volume and surface area must be positive geometry values.")
        if mold_constant <= 0:
            raise PhysicalBoundaryError("The mold constant (B) must be a positive physical property.")

        return mold_constant * ((volume / surface_area) ** exponent)
