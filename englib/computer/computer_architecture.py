"""
Mega Engineering Library - Computer & Software Engineering: Computer Architecture Module
Handles processor performance modeling, memory hierarchy metrics, and parallel scaling laws.
Validated against standard computer architecture literature (e.g., Hennessy & Patterson).
"""

from englib.common.exceptions import PhysicalBoundaryError

class ComputerArchitecture:

    @staticmethod
    def calculate_amdahl_speedup(parallel_fraction: float, speedup_factor_of_part: float) -> float:
        """
        Calculates the theoretical speedup of the execution of a whole task using Amdahl's Law.
        Speedup = 1 / ((1 - P) + (P / S))
        Where:
        P = Parallel fraction of the program (0.0 to 1.0)
        S = Speedup factor of that specific parallel execution part
        """
        if parallel_fraction < 0.0 or parallel_fraction > 1.0:
            raise PhysicalBoundaryError("The parallel fraction (P) must be a bounded ratio between 0.0 and 1.0.")
        if speedup_factor_of_part <= 0:
            raise PhysicalBoundaryError("The localized component speedup factor (S) must be a positive non-zero value.")

        denominator = (1.0 - parallel_fraction) + (parallel_fraction / speedup_factor_of_part)
        return 1.0 / denominator
