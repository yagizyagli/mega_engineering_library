"""
Mega Engineering Library - Electrical & Electronics Engineering: Control Systems Module
Handles feedback control loops, error tracking, PID algorithms, and state response formulations.
Validated against standard control engineering literature (e.g., Ogata, Kuo).
"""

from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class ControlSystems:

    @staticmethod
    def calculate_pid_output(error: float, integral_error: float, derivative_error: float, kp: float, ki: float, kd: float) -> float:
        """
        Calculates the controller output u(t) for a Parallel PID controller structure.
        u(t) = Kp * e(t) + Ki * integral(e(t)) + Kd * derivative(e(t))
        """
        if kp < 0 or ki < 0 or kd < 0:
            raise PhysicalBoundaryError("PID controller tuning gains (Kp, Ki, Kd) cannot be negative values.")
            
        proportional_term = kp * error
        integral_term = ki * integral_error
        derivative_term = kd * derivative_error
        
        return proportional_term + integral_term + derivative_term

    @staticmethod
    def calculate_closed_loop_transfer_function(forward_gain_g: float, feedback_gain_h: float) -> float:
        """
        Calculates the overall transfer function T of a standard single-input single-output (SISO) closed-loop system.
        T = G / (1 + G * H) (Assuming negative feedback)
        """
        denominator = 1.0 + (forward_gain_g * feedback_gain_h)
        
        if denominator == 0:
            raise ZeroDivisionError("System feedback loop yields an infinite output (unstable poles at the division point).")
            
        return forward_gain_g / denominator
