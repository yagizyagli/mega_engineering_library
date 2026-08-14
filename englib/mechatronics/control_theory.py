"""
Mega Engineering Library - Mechatronics & Robotics Engineering: Control Theory Module
Handles modern control systems, state-space representations, and system controllability metrics.
Validated against standard modern control literature (e.g., Ogata, Dorf & Bishop).
"""

from typing import List
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class MechatronicsControlTheory:

    @staticmethod
    def calculate_state_space_derivative_2d(matrix_a: List[List[float]], state_x: List[float], matrix_b: List[float], input_u: float) -> List[float]:
        """
        Calculates the state derivative vector dx/dt (x_dot) for a 2-state continuous linear system.
        dx/dt = A * x + B * u
        
        Where:
        matrix_a = 2x2 system matrix
        state_x = 2x1 state vector [x1, x2]
        matrix_b = 2x1 input matrix [b1, b2]
        input_u = scalar control input
        """
        if len(matrix_a) != 2 or len(matrix_a[0]) != 2 or len(state_x) != 2 or len(matrix_b) != 2:
            raise GeometricViolationError("State-space dimension violation. This routine requires a 2D state configuration.")

        # Matrix multiplication: A * x
        ax_0 = (matrix_a[0][0] * state_x[0]) + (matrix_a[0][1] * state_x[1])
        ax_1 = (matrix_a[1][0] * state_x[0]) + (matrix_a[1][1] * state_x[1])

        # Input scaling: B * u
        bu_0 = matrix_b[0] * input_u
        bu_1 = matrix_b[1] * input_u

        # Final summing: Ax + Bu
        return [ax_0 + bu_0, ax_1 + bu_1]

    @staticmethod
    def check_controllability_determinant_2d(matrix_a: List[List[float]], matrix_b: List[float]) -> float:
        """
        Computes the determinant of the 2D Controllability Matrix Co = [B | AB].
        If the determinant is non-zero, the 2-state system is fully controllable.
        """
        if len(matrix_a) != 2 or len(matrix_a[0]) != 2 or len(matrix_b) != 2:
            raise GeometricViolationError("Matrices must match 2D state space boundaries.")

        # Compute vector column: AB = A * B
        ab_0 = (matrix_a[0][0] * matrix_b[0]) + (matrix_a[0][1] * matrix_b[1])
        ab_1 = (matrix_a[1][0] * matrix_b[0]) + (matrix_a[1][1] * matrix_b[1])

        # Controllability Matrix Co = [[b0, ab0], [b1, ab1]]
        # Det(Co) = b0 * ab1 - ab0 * b1
        determinant = (matrix_b[0] * ab_1) - (ab_0 * matrix_b[1])
        return determinant
