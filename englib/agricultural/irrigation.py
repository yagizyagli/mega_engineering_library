"""
Mega Engineering Library - Agricultural & Biosystems Engineering: Irrigation Systems Module
Handles localized irrigation hydraulics, crop water consumption, and system efficiencies.
Validated against standard water engineering standards and global frameworks.
"""

from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class IrrigationSystems:

    @staticmethod
    def calculate_irrigation_efficiency(water_stored_in_root_zone: float, water_delivered_to_field: float) -> float:
        """
        Calculates the application efficiency (Ea) of an active farm irrigation setup loop.
        Ea = (Water Stored in Root Zone / Total Water Delivered)
        """
        if water_delivered_to_field <= 0:
            raise PhysicalBoundaryError("Total volume of water delivered to the agricultural field must be positive.")
        if water_stored_in_root_zone < 0 or water_stored_in_root_zone > water_delivered_to_field:
            raise PhysicalBoundaryError("Stored root zone volume cannot be negative or exceed total dynamic fluid delivery volumes.")

        return water_stored_in_root_zone / water_delivered_to_field
