"""
Mega Engineering Library - Industrial Engineering & Operations Research: Linear Programming Module
Handles objective function modeling, linear constraints, and optimization boundaries.
Validated against standard operations research literature (e.g., Taha's Operations Research: An Introduction).
"""

from typing import List
from englib.common.exceptions import PhysicalBoundaryError

class LinearProgramming:

    @staticmethod
    def calculate_linear_objective_value(coefficients: List[float], decision_variables: List[float]) -> float:
        """
        Calculates the value of a linear objective function (Z) given coefficient weights and variables.
        Z = c1*x1 + c2*x2 + ... + cn*xn
        """
        if not coefficients or not decision_variables:
            raise ValueError("Coefficient and decision variable input lists cannot be empty.")
        if len(coefficients) != len(decision_variables):
            raise ValueError("Mismatched data lengths: The number of coefficients must match the number of variables.")
            
        for x in decision_variables:
            if x < 0:
                raise PhysicalBoundaryError("Operations research standard non-negativity constraint violated: variables cannot be negative.")

        return sum(c * x for c, x in zip(coefficients, decision_variables))
