"""
Mega Engineering Library - Environmental Engineering: Solid Waste Management Module
Handles landfill gas generation kinetics and biodegradable waste degradation profiles.
Validated against standard integrated solid waste engineering guidelines.
"""

import math
from englib.common.exceptions import PhysicalBoundaryError

class SolidWaste:

    @staticmethod
    def calculate_landfill_gas_generation_rate(initial_biodegradable_mass: float, gas_production_potential: float, decay_constant_per_year: float, time_years: float) -> float:
        """
        Calculates the active annual methane/gas generation rate (Q) from a landfill mass block.
        Based on a standard first-order decay equation (EPA LandGEM principles).
        Q = k * L0 * M * exp(-k * t)
        Unit: Cubic meters per year (m³/yr)
        """
        if decay_constant_per_year <= 0:
            raise PhysicalBoundaryError("The solid waste biological decay constant (k) must be a positive non-zero value.")
        if initial_biodegradable_mass < 0 or gas_production_potential < 0 or time_years < 0:
            raise PhysicalBoundaryError("Physical waste mass, gas potential constants, and timeline context cannot be negative.")

        return decay_constant_per_year * gas_production_potential * initial_biodegradable_mass * math.exp(-decay_constant_per_year * time_years)
