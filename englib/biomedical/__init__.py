"""
Biomedical Engineering Core Suite - 100% Complete Production Build
Unified entry point for orthopedic biomechanics, ECG physiological biosignals, 
in-vivo biomaterial degradation tracking, and X-Ray tissue attenuation imaging models.
"""

from englib.biomedical.biomechanics import Biomechanics
from englib.biomedical.biosignals import Biosignals
from englib.biomedical.biomaterials import Biomaterials
from englib.biomedical.medical_imaging import MedicalImaging

__all__ = [
    "Biomechanics",
    "Biosignals",
    "Biomaterials",
    "MedicalImaging"
]
