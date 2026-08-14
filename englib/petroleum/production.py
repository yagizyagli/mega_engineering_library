"""
Mega Engineering Library - Petroleum Engineering: Production Engineering Module
Handles well deliverability curves, nodal analysis, and wellbore performance metrics.
Validated against standard production engineering literature (e.g., Beggs, Economides).
"""

from englib.common.exceptions import PhysicalBoundaryError

class PetroleumProduction:

    @staticmethod
    def calculate_vogel_inflow_performance(maximum_flow_rate_qmax: float, flowing_bottomhole_pressure: float, average_reservoir_pressure: float) -> float:
        """
        Calculates the estimated oil production rate (Q) at a specific bottomhole pressure using Vogel's IPR method.
        Valid for solution-gas drive reservoirs below bubble point pressure.
        Q = Qmax * (1 - 0.2 * (Pwf/Pr) - 0.8 * (Pwf/Pr)^2)
        Unit: Stock Tank Barrels per Day (stb/day)
        """
        if maximum_flow_rate_qmax <= 0:
            raise PhysicalBoundaryError("The maximum open-flow potential rate (Qmax) must be a positive non-zero value.")
        if average_reservoir_pressure <= 0:
            raise PhysicalBoundaryError("Average static reservoir pressure (Pr) must be greater than zero.")
        if flowing_bottomhole_pressure < 0 or flowing_bottomhole_pressure > average_reservoir_pressure:
            raise PhysicalBoundaryError("Flowing bottomhole pressure (Pwf) cannot be negative or exceed static reservoir pressure.")

        pressure_ratio = flowing_bottomhole_pressure / average_reservoir_pressure
        efficiency_reduction = 1.0 - (0.2 * pressure_ratio) - (0.8 * (pressure_ratio ** 2))
        
        return maximum_flow_rate_qmax * efficiency_reduction
