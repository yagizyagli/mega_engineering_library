"""
Mega Engineering Library - Petroleum Engineering: Reservoir Fluid Properties Module
Handles fluid PVT behaviors, gas-oil ratios (GOR), and formation volume factors.
Validated against standard petroleum reservoir literature (e.g., McCain's The Properties of Petroleum Fluids).
"""

from englib.common.exceptions import PhysicalBoundaryError

class ReservoirFluid:

    @staticmethod
    def calculate_solution_gas_oil_ratio_baseline(total_gas_volume_scf: float, total_oil_volume_stb: float) -> float:
        """
        Calculates the baseline Solution Gas-Oil Ratio (Rs).
        Rs = Gas Volume (scf) / Oil Volume (stb)
        Unit: Standard Cubic Feet per Stock Tank Barrel (scf/stb)
        """
        if total_oil_volume_stb <= 0:
            raise PhysicalBoundaryError("Stock tank oil volume (stb) must be a positive non-zero reference measurement.")
        if total_gas_volume_scf < 0:
            raise PhysicalBoundaryError("Produced gas volume cannot be negative.")

        return total_gas_volume_scf / total_oil_volume_stb
