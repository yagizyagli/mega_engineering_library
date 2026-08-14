"""
Common Utilities Package Initializer
Exposes cross-disciplinary unit converters, universal constants, and custom exception definitions.
"""

from englib.common.constants import GRAVITY, UNIVERSAL_GAS_CONSTANT, AVOGADRO, SPEED_OF_LIGHT, PI, E
from englib.common.units import UnitConverter
from englib.common.exceptions import (
    EngineeringError,
    PhysicalBoundaryError,
    NegativeAbsoluteTemperatureError,
    MaterialFailureError,
    GeometricViolationError
)

__all__ = [
    "GRAVITY",
    "UNIVERSAL_GAS_CONSTANT",
    "AVOGADRO",
    "SPEED_OF_LIGHT",
    "PI",
    "E",
    "UnitConverter",
    "EngineeringError",
    "PhysicalBoundaryError",
    "NegativeAbsoluteTemperatureError",
    "MaterialFailureError",
    "GeometricViolationError"
]
