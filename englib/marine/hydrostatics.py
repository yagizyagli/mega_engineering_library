"""
Mega Engineering Library - Marine Engineering & Naval Architecture: Hydrostatics Module
Handles ship buoyancy, intact stability, center of gravity shifts, and metacentric heights.
Validated against standard naval architecture literature (e.g., Lewis's Principles of Naval Architecture).
"""

from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class MarineHydrostatics:

    @staticmethod
    def calculate_metacentric_height(transverse_metacentric_radius_bm: float, center_of_buoyancy_kb: float, center_of_gravity_kg: float) -> float:
        """
        Calculates the Metacentric Height (GM), the fundamental metric for initial ship stability.
        GM = KB + BM - KG
        Sign significance:
        - GM > 0: Stable equilibrium (Ship rights itself)
        - GM == 0: Neutral equilibrium
        - GM < 0: Unstable equilibrium (Ship capsizes)
        Unit: Meters (m)
        """
        if transverse_metacentric_radius_bm <= 0:
            raise GeometricViolationError("Transverse metacentric radius (BM) must be a positive non-zero dimension.")
        if center_of_buoyancy_kb < 0 or center_of_gravity_kg < 0:
            raise GeometricViolationError("Ship vertical reference centers (KB, KG) from the keel must be non-negative.")

        # If KG is higher than the combined KB and BM, GM becomes negative, which means unstable ship profile.
        return center_of_buoyancy_kb + transverse_metacentric_radius_bm - center_of_gravity_kg
