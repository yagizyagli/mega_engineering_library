"""
Mega Engineering Library - Textile Engineering: Yarn Mechanics Module
Handles yarn twist geometries, structural twist factors, and linear density conversions.
Validated against standard yarn structure manuals.
"""

import math
from englib.common.exceptions import PhysicalBoundaryError

class YarnMechanics:

    @staticmethod
    def calculate_yarn_twist_factor_tex(twist_per_meter: float, yarn_count_tex: float) -> float:
        """
        Calculates the structural Twist Factor (K_tex) of a yarn using the Tex count system.
        K_tex = Twist_per_meter * sqrt(Yarn_count_tex)
        """
        if twist_per_meter < 0:
            raise PhysicalBoundaryError("Yarn twist per meter turns cannot be negative.")
        if yarn_count_tex <= 0:
            raise PhysicalBoundaryError("Yarn linear density count (Tex) must be a positive non-zero metric.")

        return twist_per_meter * math.sqrt(yarn_count_tex)
