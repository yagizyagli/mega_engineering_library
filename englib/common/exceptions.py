"""
Mega Engineering Library - Custom Exceptions
Defines standardized, domain-specific exceptions for engineering boundary violations.
Helps prevent catastrophic simulation errors before calculations execute.
"""

class EngineeringError(Exception):
    """Base exception for all errors in the Mega Engineering Library."""
    pass

class PhysicalBoundaryError(EngineeringError):
    """Exception raised when a value violates fundamental laws of physics."""
    pass

class NegativeAbsoluteTemperatureError(PhysicalBoundaryError):
    """Raised when a temperature is defined below Absolute Zero (-273.15 °C or 0 K)."""
    def __init__(self, temperature: float, unit: str = "C"):
        self.temperature = temperature
        self.unit = unit
        super().__init__(f"Catastrophic Limit: Temperature {temperature}°{unit} is below Absolute Zero!")

class MaterialFailureError(EngineeringError):
    """Exception raised when structural or material calculations indicate immediate structural collapse."""
    pass

class GeometricViolationError(EngineeringError):
    """Raised when structural dimensions are physically impossible (e.g., negative area, negative thickness)."""
    pass
