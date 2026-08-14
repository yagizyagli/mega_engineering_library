"""
Mega Engineering Library - Electrical & Electronics Engineering: Power Systems Module
Handles AC transmission lines, three-phase power networks, and electrical machine efficiencies.
Validated against standard power engineering literature (e.g., Glover, Sarma & Overbye).
"""

import math
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class PowerSystems:

    @staticmethod
    def calculate_three_phase_apparent_power(line_voltage: float, line_current: float) -> float:
        """
        Calculates the total complex apparent power (S) in a balanced three-phase system.
        S = sqrt(3) * V_line * I_line
        Unit: Volt-Amperes (VA)
        """
        if line_voltage <= 0 or line_current <= 0:
            raise PhysicalBoundaryError("Line voltage and line current must be positive non-zero measurements.")
        return math.sqrt(3.0) * line_voltage * line_current

    @staticmethod
    def calculate_power_factor(real_power_watts: float, apparent_power_va: float) -> float:
        """
        Calculates the power factor (PF) of an electrical system network.
        PF = Real Power (P) / Apparent Power (S)
        Returns a dimensionless ratio between 0.0 and 1.0.
        """
        if apparent_power_va <= 0:
            raise PhysicalBoundaryError("Apparent power must be greater than zero.")
        if real_power_watts < 0 or real_power_watts > apparent_power_va:
            raise PhysicalBoundaryError("Real power cannot be negative or exceed the system's total apparent power.")

        return real_power_watts / apparent_power_va

    @staticmethod
    def calculate_transmission_line_efficiency(power_sent_watts: float, power_received_watts: float) -> float:
        """
        Calculates the grid transmission line efficiency based on resistive line losses.
        Efficiency = Power Received / Power Sent
        """
        if power_sent_watts <= 0:
            raise PhysicalBoundaryError("Power generated/sent into the transmission network must be positive.")
        if power_received_watts < 0 or power_received_watts > power_sent_watts:
            raise PhysicalBoundaryError("Power received cannot be negative or exceed the initial injected transmission energy.")

        return power_received_watts / power_sent_watts
