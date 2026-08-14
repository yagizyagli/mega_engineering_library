"""
Mega Engineering Library - Transportation Engineering: Traffic Engineering Module
Handles traffic flow theory, speed-density relationships, and road capacity limits.
Validated against standard traffic engineering literature (e.g., Roess, Prassas, & McShane's Traffic Engineering).
"""

from englib.common.exceptions import PhysicalBoundaryError

class TrafficEngineering:

    @staticmethod
    def calculate_greenshields_speed(free_flow_speed: float, jam_density: float, current_density: float) -> float:
        """
        Calculates the average stream speed (V) given vehicle density using the Greenshields Model.
        V = Vf * (1 - k / kj)
        Where:
        Vf = Free-flow speed (km/h or mph)
        kj = Jam density (vehicles/km or vehicles/mile)
        k  = Current traffic density
        Unit: Same speed unit as free-flow speed input.
        """
        if free_flow_speed <= 0 or jam_density <= 0:
            raise PhysicalBoundaryError("Free-flow speed and jam density must be positive non-zero parameters.")
        if current_density < 0 or current_density > jam_density:
            raise PhysicalBoundaryError("Current traffic density cannot be negative or exceed the maximum jam density boundary.")

        return free_flow_speed * (1.0 - (current_density / jam_density))
