"""
Mega Engineering Library - Common Unit Conversion Engine
Provides explicit, multi-dimensional conversion matrices between Metric (SI) and Imperial systems.
"""

from englib.common.exceptions import NegativeAbsoluteTemperatureError

class UnitConverter:
    
    # --- PRESSURE CONVERSIONS ---
    @staticmethod
    def pascal_to_psi(pascal: float) -> float:
        """Converts Pascal (Pa) to Pounds per Square Inch (PSI)."""
        return pascal * 0.000145037737

    @staticmethod
    def psi_to_pascal(psi: float) -> float:
        """Converts Pounds per Square Inch (PSI) to Pascal (Pa)."""
        return psi / 0.000145037737

    # --- TEMPERATURE CONVERSIONS ---
    @staticmethod
    def celsius_to_kelvin(celsius: float) -> float:
        """Converts Celsius (°C) to Kelvin (K)."""
        if celsius < -273.15:
            raise NegativeAbsoluteTemperatureError(celsius, "C")
        return celsius + 273.15

    # --- LENGTH CONVERSIONS ---
    @staticmethod
    def meter_to_inch(meter: float) -> float:
        """Converts meters (m) to inches (in)."""
        return meter * 39.3700787
