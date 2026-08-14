"""
Mega Engineering Library - Mechanical Engineering: Thermodynamics Module
Contains core formulations for energy conservation, ideal gases, power cycles, and psychrometrics.
Validated against standard engineering thermodynamics literature (e.g., Moran & Shapiro, Cengel).
"""

import math
from englib.common.constants import UNIVERSAL_GAS_CONSTANT
from englib.common.exceptions import PhysicalBoundaryError, NegativeAbsoluteTemperatureError

class MechanicalThermodynamics:

    @staticmethod
    def calculate_ideal_gas_pressure(density: float, specific_gas_constant: float, temperature_kelvin: float) -> float:
        """
        Calculates the pressure (P) of an ideal gas using the equation of state: P = rho * R * T
        Returns pressure in Pascals (Pa).
        """
        if temperature_kelvin < 0:
            raise NegativeAbsoluteTemperatureError(temperature_kelvin, "K")
        if density <= 0:
            raise PhysicalBoundaryError("Gas density must be a positive non-zero value.")
        if specific_gas_constant <= 0:
            raise PhysicalBoundaryError("Specific gas constant must be positive based on molecular weight.")

        return density * specific_gas_constant * temperature_kelvin

    @staticmethod
    def calculate_carnot_efficiency(temp_low_kelvin: float, temp_high_kelvin: float) -> float:
        """
        Calculates the theoretical maximum thermal efficiency (eta) of a power cycle operating between two temperatures.
        Thermal Efficiency = 1 - (T_low / T_high)
        Returns the efficiency as a decimal fraction (0.0 to 1.0).
        """
        if temp_low_kelvin < 0:
            raise NegativeAbsoluteTemperatureError(temp_low_kelvin, "K")
        if temp_high_kelvin < 0:
            raise NegativeAbsoluteTemperatureError(temp_high_kelvin, "K")
        if temp_low_kelvin >= temp_high_kelvin:
            raise PhysicalBoundaryError("The low-temperature reservoir must be colder than the high-temperature reservoir.")
        if temp_high_kelvin == 0:
            raise ZeroDivisionError("High temperature reservoir cannot be absolute zero.")

        return 1.0 - (temp_low_kelvin / temp_high_kelvin)

    @staticmethod
    def calculate_rankine_network(turbine_work: float, pump_work: float, heat_added: float) -> float:
        """
        Calculates the thermal efficiency of an ideal Rankine power cycle.
        Net Work = Turbine Work - Pump Work
        Efficiency = Net Work / Heat Added
        """
        if heat_added <= 0:
            raise PhysicalBoundaryError("Heat input to the boiler must be a positive non-zero value.")
        if turbine_work < 0 or pump_work < 0:
            raise PhysicalBoundaryError("Work values cannot be negative in standard power production definitions.")
            
        net_work = turbine_work - pump_work
        if net_work < 0:
            raise PhysicalBoundaryError("The cycle consumes more work than it produces; efficiency is invalid.")

        return net_work / heat_added
