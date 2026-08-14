"""
Environmental Engineering Core Suite - 100% Complete Production Build
Unified entry point for Gaussian air pollutant plume dispersions, Streeter-Phelps water quality deficits,
landfill methane bio-gas decay generation rates, and subsurface aquifer seepage contaminant velocities.
"""

from englib.environmental.air_dispersion import AirDispersion
from englib.environmental.water_quality import WaterQuality
from englib.environmental.solid_waste import SolidWaste
from englib.environmental.remediation import GroundwaterRemediation

__all__ = [
    "AirDispersion",
    "WaterQuality",
    "SolidWaste",
    "GroundwaterRemediation"
]
