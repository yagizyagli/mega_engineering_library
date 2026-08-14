"""
Mega Engineering Library - Mechanical Engineering: Machine Design Module
Focuses on component sizing, stress concentrations, shaft design, bearings, and gears.
Validated against standard mechanical design literature (e.g., Shigley's Mechanical Engineering Design).
"""

import math
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class MachineDesign:

    @staticmethod
    def calculate_shaft_diameter_torsion(torque: float, allowable_shear_stress: float) -> float:
        """
        Calculates the minimum required solid shaft diameter (d) subjected to pure torsion.
        Based on elastic torsion formula: d = ((16 * T) / (pi * tau_allowable))^(1/3)
        Returns diameter in meters (m).
        """
        if allowable_shear_stress <= 0:
            raise PhysicalBoundaryError("Allowable shear stress must be a positive non-zero material limit.")
        if torque < 0:
            raise PhysicalBoundaryError("Torque magnitude cannot be negative for physical sizing.")

        diameter = ((16.0 * torque) / (math.pi * allowable_shear_stress)) ** (1.0 / 3.0)
        return diameter

    @staticmethod
    def calculate_bearing_life_hours(radial_load: float, dynamic_load_rating: float, rpm: float, bearing_type: str = "ball") -> float:
        """
        Calculates the rating life (L10h) of a rolling-element bearing in hours.
        L10 = (C / P)^p where p = 3 for ball bearings, p = 10/3 for roller bearings.
        L10h = (L10 * 10^6) / (60 * RPM)
        """
        if radial_load <= 0:
            raise PhysicalBoundaryError("Equivalent radial load (P) must be greater than zero.")
        if dynamic_load_rating <= 0:
            raise PhysicalBoundaryError("Basic dynamic load rating (C) must be greater than zero.")
        if rpm <= 0:
            raise GeometricViolationError("Rotational speed (RPM) must be positive and non-zero.")

        # Determine exponent based on bearing type
        b_type = bearing_type.lower().strip()
        if b_type == "ball":
            p = 3.0
        elif b_type == "roller":
            p = 10.0 / 3.0
        else:
            raise ValueError("Invalid bearing_type. Must be either 'ball' or 'roller'.")

        life_millions_revolutions = (dynamic_load_rating / radial_load) ** p
        life_hours = (life_millions_revolutions * 1e6) / (60.0 * rpm)
        
        return life_hours

    @staticmethod
    def calculate_gear_tooth_bending_lewis(tangential_force: float, diametral_pitch: float, face_width: float, lewis_form_factor: float) -> float:
        """
        Calculates the fundamental bending stress (sigma) at the root of a spur gear tooth.
        Using the traditional Lewis Equation: sigma = (W_t * P_d) / (F * Y)
        Unit: Pascals (Pa)
        """
        if diametral_pitch <= 0 or face_width <= 0:
            raise GeometricViolationError("Gear geometric parameters (pitch and face width) must be positive.")
        if lewis_form_factor <= 0:
            raise GeometricViolationError("Lewis form factor (Y) must be a positive non-zero coefficient.")
        if tangential_force < 0:
            raise PhysicalBoundaryError("Tangential load cannot be negative.")

        return (tangential_force * diametral_pitch) / (face_width * lewis_form_factor)
