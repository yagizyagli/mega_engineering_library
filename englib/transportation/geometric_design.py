"""
Mega Engineering Library - Transportation Engineering: Geometric Design Module
Handles highway alignments, stopping sight distances (SSD), and super-elevation safety formulas.
Validated against standard highway design literature (e.g., AASHTO Green Book guidelines).
"""

from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class GeometricDesign:

    @staticmethod
    def calculate_stopping_sight_distance(velocity_m_s: float, reaction_time_sec: float, deceleration_rate_m_s2: float) -> float:
        """
        Calculates the total Stopping Sight Distance (SSD) required for an ideal vehicle to brake to a complete stop.
        SSD = (V * t) + (V^2 / (2 * a))
        Where:
        V = Vehicle initial speed (m/s)
        t = Driver reaction time in seconds (AASHTO standard uses 2.5 seconds)
        a = Deceleration comfort rate (AASHTO standard uses 3.4 m/s²)
        Unit: Meters (m)
        """
        if velocity_m_s < 0:
            raise PhysicalBoundaryError("Vehicle initial approach velocity cannot be negative.")
        if reaction_time_sec <= 0:
            raise PhysicalBoundaryError("Driver cognitive reaction window time must be positive and non-zero.")
        if deceleration_rate_m_s2 <= 0:
            raise PhysicalBoundaryError("Braking deceleration force rate parameter must be greater than zero.")

        perception_distance = velocity_m_s * reaction_time_sec
        braking_distance = (velocity_m_s ** 2) / (2.0 * deceleration_rate_m_s2)
        
        return perception_distance + braking_distance
