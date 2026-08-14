"""
Mega Engineering Library - Computer & Software Engineering: Network Calculus Module
Handles data traffic queuing models, buffer delays, and network performance flows.
Validated against standard queuing theory and network literature (e.g., Kleinrock).
"""

from englib.common.exceptions import PhysicalBoundaryError

class NetworkCalculus:

    @staticmethod
    def calculate_little_law_items(arrival_rate_per_sec: float, average_delay_sec: float) -> float:
        """
        Calculates the average number of data packets (L) inside a network buffer using Little's Law.
        L = Lambda * W
        Where:
        Lambda = Average arrival rate of packets per second
        W = Average time spent by a packet in the system
        """
        if arrival_rate_per_sec < 0 or average_delay_sec < 0:
            raise PhysicalBoundaryError("Packet arrival rates and system delays cannot be negative numbers.")

        return arrival_rate_per_sec * average_delay_sec
