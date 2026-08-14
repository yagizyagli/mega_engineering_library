"""
Mega Engineering Library - Industrial Engineering & Operations Research: Supply Chain Module
Handles dynamic inventory management models, safety stock profiles, and order optimizations.
Validated against standard supply chain management literature (e.g., Chopra & Meindl).
"""

import math
from englib.common.exceptions import PhysicalBoundaryError

class SupplyChainManagement:

    @staticmethod
    def calculate_economic_order_quantity(annual_demand: float, setup_ordering_cost: float, holding_cost_per_unit_year: float) -> float:
        """
        Calculates the optimal order size that minimizes total inventory costs using the classical EOQ formula.
        EOQ = sqrt( (2 * D * S) / H )
        """
        if holding_cost_per_unit_year <= 0:
            raise PhysicalBoundaryError("Inventory annual holding cost (H) must be a positive non-zero value.")
        if annual_demand < 0 or setup_ordering_cost < 0:
            raise PhysicalBoundaryError("Annual market demand (D) and fixed ordering setup costs (S) cannot be negative.")

        numerator = 2.0 * annual_demand * setup_ordering_cost
        return math.sqrt(numerator / holding_cost_per_unit_year)
