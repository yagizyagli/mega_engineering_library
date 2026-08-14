"""
Mega Engineering Library - Chemical Engineering: Reaction Kinetics Module
Handles chemical reaction rates, Arrhenius temperature dependencies, and reactor sizing equations.
Validated against standard chemical reaction engineering literature (e.g., Fogler).
"""

import math
from englib.common.constants import UNIVERSAL_GAS_CONSTANT
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class ReactionKinetics:

    @staticmethod
    def calculate_arrhenius_rate_constant(pre_exponential_factor: float, activation_energy_j_mol: float, temperature_kelvin: float) -> float:
        """
        Calculates the chemical reaction rate constant (k) using the Arrhenius Equation.
        k = A * exp(-Ea / (R * T))
        """
        if temperature_kelvin <= 0:
            raise PhysicalBoundaryError("Absolute temperature must be a positive non-zero Kelvin value.")
        if pre_exponential_factor <= 0:
            raise PhysicalBoundaryError("Pre-exponential frequency factor (A) must be positive.")
        if activation_energy_j_mol < 0:
            raise PhysicalBoundaryError("Activation energy (Ea) cannot be negative.")

        exponent = -activation_energy_j_mol / (UNIVERSAL_GAS_CONSTANT * temperature_kelvin)
        return pre_exponential_factor * math.exp(exponent)

    @staticmethod
    def calculate_cstr_volume(volumetric_flow_rate: float, reactant_initial_conc: float, conversion_fraction: float, reaction_rate: float) -> float:
        """
        Calculates the required volume (V) of a Continuous Stirred-Tank Reactor (CSTR).
        V = (F_A0 * X) / (-r_A) = (v0 * C_A0 * X) / (-r_A)
        Unit: Cubic meters (m³) or Liters (L) depending on input flow standard.
        """
        if volumetric_flow_rate <= 0 or reactant_initial_conc <= 0:
            raise GeometricViolationError("Volumetric flow rate and initial concentration must be positive non-zero values.")
        if conversion_fraction < 0.0 or conversion_fraction >= 1.0:
            raise PhysicalBoundaryError("Conversion fraction (X) must be a bounded ratio between 0.0 and 1.0.")
        if reaction_rate <= 0:
            raise PhysicalBoundaryError("The consumption reaction rate (-rA) must be a positive non-zero value.")

        return (volumetric_flow_rate * reactant_initial_conc * conversion_fraction) / reaction_rate
