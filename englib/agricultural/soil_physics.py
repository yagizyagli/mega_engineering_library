"""
Mega Engineering Library - Agricultural & Biosystems Engineering: Soil Physics Module
Handles soil porosity, moisture content, bulk density, and hydraulic conductivities.
Validated against standard agricultural engineering literature (e.g., Hillel's Environmental Soil Physics).
"""

from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class SoilPhysics:

    @staticmethod
    def calculate_soil_porosity(bulk_density: float, particle_density: float = 2.65) -> float:
        """
        Calculates the dimensionless total soil porosity (f).
        f = 1 - (rho_b / rho_p)
        Where particle_density (rho_p) defaults to a standard quartz profile value of 2.65 g/cm³.
        """
        if bulk_density <= 0 or particle_density <= 0:
            raise PhysicalBoundaryError("Soil bulk density and particle density must be positive non-zero values.")
        if bulk_density >= particle_density:
            raise PhysicalBoundaryError("Physically impossible: Bulk density cannot exceed solid particle density.")

        return 1.0 - (bulk_density / particle_density)

    @staticmethod
    def calculate_volumetric_water_content(gravimetric_water_content: float, bulk_density: float, water_density: float = 1.0) -> float:
        """
        Calculates the volumetric water content (theta) of a soil profile sample.
        theta = w * (rho_b / rho_w)
        """
        if gravimetric_water_content < 0 or bulk_density < 0:
            raise PhysicalBoundaryError("Water content ratio and soil density values cannot be negative.")
        if water_density <= 0:
            raise PhysicalBoundaryError("Reference water density must be greater than zero.")

        return gravimetric_water_content * (bulk_density / water_density)
