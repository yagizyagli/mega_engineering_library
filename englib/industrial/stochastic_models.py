"""
Mega Engineering Library - Industrial Engineering & Operations Research: Stochastic Models Module
Handles queuing systems, birth-death stochastic processes, and arrival performance rates.
Validated against standard industrial logistics manuals (e.g., Hillier & Lieberman).
"""

from englib.common.exceptions import PhysicalBoundaryError

class StochasticModels:

    @staticmethod
    def calculate_average_system_entities(arrival_rate: float, average_system_time: float) -> float:
        """
        Calculates the average number of entities/customers (L) in a stable queueing system using Little's Law.
        L = lambda * W
        Where:
        lambda = Mean arrival rate per time unit
        W = Mean time spent by an entity in the system
        """
        if arrival_rate < 0 or average_system_time < 0:
            raise PhysicalBoundaryError("Stochastic arrival rates and systemic wait durations cannot be negative values.")

        return arrival_rate * average_system_time
