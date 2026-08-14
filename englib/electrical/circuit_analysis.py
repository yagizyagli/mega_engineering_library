"""
Mega Engineering Library - Electrical & Electronics Engineering: Circuit Analysis Module
Contains fundamental formulations for DC/AC network analysis, nodal laws, and component networks.
Validated against standard electrical engineering textbook methodologies (e.g., Alexander & Sadiku).
"""

from typing import List
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class CircuitAnalysis:

    @staticmethod
    def calculate_ohm_law(voltage: float = None, current: float = None, resistance: float = None) -> float:
        """
        Solves Ohm's Law (V = I * R) for the missing parameters.
        Provide exactly two parameters to calculate the third one.
        """
        params = [voltage, current, resistance]
        provided = sum(1 for p in params if p is not None)
        
        if provided != 2:
            raise ValueError("Exactly two parameters must be provided to solve Ohm's Law.")
            
        if resistance is not None and resistance <= 0:
            raise PhysicalBoundaryError("Resistance must be a positive non-zero value.")

        if voltage is None:
            return current * resistance
        elif current is None:
            return voltage / resistance
        elif resistance is None:
            if current == 0:
                raise ZeroDivisionError("Current cannot be zero when computing resistance.")
            return voltage / current

    @staticmethod
    def calculate_equivalent_resistance_series(resistors: List[float]) -> float:
        """
        Calculates total equivalent resistance for resistors connected in series.
        R_eq = R1 + R2 + ... + Rn
        """
        if not resistors:
            raise ValueError("The resistor list cannot be empty.")
            
        for r in resistors:
            if r <= 0:
                raise PhysicalBoundaryError("All resistor values in the circuit must be greater than zero.")
                
        return sum(resistors)

    @staticmethod
    def calculate_equivalent_resistance_parallel(resistors: List[float]) -> float:
        """
        Calculates total equivalent resistance for resistors connected in parallel.
        1 / R_eq = 1/R1 + 1/R2 + ... + 1/Rn
        """
        if not resistors:
            raise ValueError("The resistor list cannot be empty.")
            
        inverse_sum = 0.0
        for r in resistors:
            if r <= 0:
                raise PhysicalBoundaryError("Parallel resistor values must be positive and non-zero.")
            inverse_sum += 1.0 / r
            
        return 1.0 / inverse_sum
