"""
Mega Engineering Library - Electrical & Electronics Engineering: Electromagnetics Module
Handles electromagnetic wave propagation, wave impedances, and transmission lines.
Validated against standard electromagnetics literature (e.g., Hayt & Buck, Sadiku).
"""

import math
from englib.common.constants import SPEED_OF_LIGHT
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class Electromagnetics:

    @staticmethod
    def calculate_wave_impedance_lossless(relative_permeability: float, relative_permittivity: float) -> float:
        """
        Calculates the intrinsic wave impedance (eta) of a lossless dielectric medium.
        eta = eta_0 * sqrt(mu_r / epsilon_r)
        Where eta_0 (intrinsic impedance of free space) ~ 376.7303136 Ohms.
        Unit: Ohms (Omega)
        """
        if relative_permeability <= 0 or relative_permittivity <= 0:
            raise PhysicalBoundaryError("Relative permeability and permittivity must be positive non-zero material properties.")

        intrinsic_impedance_free_space = 376.7303136
        return intrinsic_impedance_free_space * math.sqrt(relative_permeability / relative_permittivity)

    @staticmethod
    def calculate_wavelength_in_medium(frequency_hz: float, relative_permittivity: float, relative_permeability: float = 1.0) -> float:
        """
        Calculates the wavelength (lambda) of an electromagnetic wave inside a specific medium.
        v = c / sqrt(epsilon_r * mu_r)
        lambda = v / frequency
        Unit: Meters (m)
        """
        if frequency_hz <= 0:
            raise PhysicalBoundaryError("Wave frequency must be a positive non-zero value.")
        if relative_permittivity <= 0 or relative_permeability <= 0:
            raise PhysicalBoundaryError("Medium constitutive parameters must be greater than zero.")

        # Phase velocity in the medium
        velocity_in_medium = SPEED_OF_LIGHT / math.sqrt(relative_permittivity * relative_permeability)
        return velocity_in_medium / frequency_hz
