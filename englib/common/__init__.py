"""
Common utilities, physical constants, and custom exceptions shared across all engineering branches.
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
