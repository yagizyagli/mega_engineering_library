"""
Mechanical Engineering Core Suite - 100% Complete Production Build
Unified entry point for fluid dynamics, thermal sciences, material strength, component design,
vibration mechanics, advanced manufacturing systems, and HVAC engineering.
"""

from englib.mechanical.thermodynamics import MechanicalThermodynamics
from englib.mechanical.fluid_mechanics import FluidMechanics
from englib.mechanical.solid_mechanics import SolidMechanics
from englib.mechanical.heat_transfer import HeatTransfer
from englib.mechanical.machine_design import MachineDesign
from englib.mechanical.theory_of_machines import TheoryOfMachines
from englib.mechanical.manufacturing import ManufacturingTechnology
from englib.mechanical.hvac import HVACSystems

__all__ = [
    "MechanicalThermodynamics",
    "FluidMechanics",
    "SolidMechanics",
    "HeatTransfer",
    "MachineDesign",
    "TheoryOfMachines",
    "ManufacturingTechnology",
    "HVACSystems"
]
