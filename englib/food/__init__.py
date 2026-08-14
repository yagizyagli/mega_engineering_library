"""
Food Engineering Core Suite - 100% Complete Production Build
Unified entry point for microbial thermal destruction kinetics, D-value configurations,
and non-Newtonian Power Law food fluid rheology models.
"""

from englib.food.thermal_processing import FoodThermalProcessing
from englib.food.preservation_fluid import FoodRheology

__all__ = [
    "FoodThermalProcessing",
    "FoodRheology"
]
