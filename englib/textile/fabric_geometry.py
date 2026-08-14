"""
Mega Engineering Library - Textile Engineering: Fabric Geometry Module
Handles fabric structural settings, yarn crimp fractions, and cloth packing densities.
Validated against standard structural fabric literature (e.g., Peirce's Geometry of Cloth Structure).
"""

from englib.common.exceptions import PhysicalBoundaryError, GeometricViolationError

class FabricGeometry:

    @staticmethod
    def calculate_yarn_crimp_fraction(yarn_length_in_fabric: float, straightened_yarn_length: float) -> float:
        """
        Calculates the fractional yarn crimp (c) representing the waviness of yarn inside a woven cloth.
        c = (L_straightened - L_fabric) / L_fabric
        Returns a decimal fractional value.
        """
        if yarn_length_in_fabric <= 0:
            raise GeometricViolationError("The boundary length of yarn inside the fabric layout must be greater than zero.")
        if straightened_yarn_length < yarn_length_in_fabric:
            raise PhysicalBoundaryError("Physically impossible structural configuration: Straightened yarn length cannot be shorter than its crimped length inside the fabric.")

        return (straightened_yarn_length - yarn_length_in_fabric) / yarn_length_in_fabric
