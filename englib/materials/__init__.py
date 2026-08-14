"""
Materials Science & Engineering Core Suite - 100% Complete Production Build
Unified entry point for Bragg crystal lattice spacings, Griffith brittle fracture critical stresses,
alloy binary phase diagram Lever Rule metrics, and macromolecular PDI polymer weights.
"""

from englib.materials.crystallography import Crystallography
from englib.materials.mechanics import MaterialsMechanics
from englib.materials.thermodynamics import MaterialsThermodynamics
from englib.materials.polymers import PolymerEngineering

__all__ = [
    "Crystallography",
    "MaterialsMechanics",
    "MaterialsThermodynamics",
    "PolymerEngineering"
]
