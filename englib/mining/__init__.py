"""
Mining & Geological Engineering Core Suite - 100% Complete Production Build
Unified entry point for Hoek-Brown rock mechanics, commercial explosive detonation pressures,
Atkinson mine airway ventilation friction losses, and spatial IDW ore reserve geostatistics.
"""

from englib.mining.rock_mechanics import RockMechanics
from englib.mining.blasting import BlastingEngineering
from englib.mining.ventilation import MineVentilation
from englib.mining.geostatistics import Geostatistics

__all__ = [
    "RockMechanics",
    "BlastingEngineering",
    "MineVentilation",
    "Geostatistics"
]
