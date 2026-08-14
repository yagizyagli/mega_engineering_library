"""
Mega Engineering Library - Nuclear Engineering: Reactor Physics Module
Handles neutron reproduction factors, criticality indexes, and chain reaction kinetics.
Validated against standard nuclear engineering literature (e.g., Lamarsh's Introduction to Nuclear Engineering).
"""

from englib.common.exceptions import PhysicalBoundaryError

class NuclearReactorPhysics:

    @staticmethod
    def calculate_six_factor_multiplication_factor(reproduction_factor: float, thermal_utilization: float, resonance_escape_prob: float, fast_fission_factor: float, fast_non_leakage_prob: float, thermal_non_leakage_prob: float) -> float:
        """
        Calculates the effective neutron multiplication factor (k) using the classical Six-Factor Formula.
        k = eta * f * p * epsilon * P_f * P_t
        Criticality states:
        - k < 1.0: Subcritical (Reaction dies out)
        - k == 1.0: Critical (Steady-state self-sustaining reaction)
        - k > 1.0: Supercritical (Reaction accelerates)
        """
        factors = [reproduction_factor, thermal_utilization, resonance_escape_prob, fast_fission_factor, fast_non_leakage_prob, thermal_non_leakage_prob]
        
        for factor in factors:
            if factor <= 0 or factor > 2.5:
                # Standard physical bounded check for microscopic neutron probabilities and yields
                raise PhysicalBoundaryError("Nuclear neutron multiplication factors must be positive and within physical bounds.")

        k_effective = reproduction_factor * thermal_utilization * resonance_escape_prob * fast_fission_factor * fast_non_leakage_prob * thermal_non_leakage_prob
        return k_effective
