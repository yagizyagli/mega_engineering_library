"""
Civil Engineering Core Suite - 100% Complete Production Build
Unified entry point for structural statics, structural dynamics, reinforced concrete design,
structural steel mechanics, geotechnical foundations, and hydraulic fluid systems.
"""

from englib.civil.statics import CivilStatics
from englib.civil.structural_dynamics import StructuralDynamics
from englib.civil.concrete_design import ConcreteDesign
from englib.civil.steel_design import SteelDesign
from englib.civil.geotechnical import GeotechnicalEngineering
from englib.civil.hydraulics import CivilHydraulics

__all__ = [
    "CivilStatics",
    "StructuralDynamics",
    "ConcreteDesign",
    "SteelDesign",
    "GeotechnicalEngineering",
    "CivilHydraulics"
]
