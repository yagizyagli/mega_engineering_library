"""
Mega Engineering Library - Nuclear Engineering: Fusion Physics Module
Handles plasma confinement scaling, Lawson fusion metrics, and thermonuclear thresholds.
Validated against standard plasma physics literature.
"""

from englib.common.exceptions import PhysicalBoundaryError

class FusionPhysics:

    @staticmethod
    def evaluate_lawson_criterion_product(electron_density_m3: float, confinement_time_seconds: float) -> float:
        """
        Calculates the Lawson Criterion triple product index component (n * tau_e) for nuclear fusion.
        For a D-T (Deuterium-Tritium) plasma to ignite, this product typically needs to surpass 1e20 s/m³.
        Unit: seconds per cubic meter (s/m³)
        """
        if electron_density_m3 <= 0 or confinement_time_seconds <= 0:
            raise PhysicalBoundaryError("Fusion plasma electron densities and core confinement durations must be positive values.")

        return electron_density_m3 * confinement_time_seconds
