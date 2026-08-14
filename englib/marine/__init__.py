"""
Marine Engineering & Naval Architecture Core Suite - 100% Complete Production Build
Unified entry point for metacentric ship buoyancy hydrostatics, Froude hull hydrodynamics,
propeller advance coefficient propulsion systems, and midship wave-induced structural loading profiles.
"""

from englib.marine.hydrostatics import MarineHydrostatics
from englib.marine.hydrodynamics import MarineHydrodynamics
from englib.marine.propulsion import MarinePropulsion
from englib.marine.marine_structures import MarineStructures

__all__ = [
    "MarineHydrostatics",
    "MarineHydrodynamics",
    "MarinePropulsion",
    "MarineStructures"
]
