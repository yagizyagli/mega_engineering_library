"""
Mega Engineering Library - Mechatronics & Robotics Engineering: Kinematics Module
Handles forward/inverse kinematics, transformation matrices, and joint space coordinates for robotic systems.
Validated against standard robotics literature (e.g., Craig's Introduction to Robotics).
"""

import math
from typing import Tuple, Dict
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class RoboticKinematics:

    @staticmethod
    def forward_kinematics_2r_planar(link1_length: float, link2_length: float, theta1_degrees: float, theta2_degrees: float) -> Tuple[float, float]:
        """
        Calculates the end-effector position (X, Y) of a 2-Link (2R) planar robotic arm.
        Uses pure geometric and trigonometric forward kinematics.
        
        X = L1 * cos(theta1) + L2 * cos(theta1 + theta2)
        Y = L1 * sin(theta1) + L2 * sin(theta1 + theta2)
        """
        if link1_length <= 0 or link2_length <= 0:
            raise GeometricViolationError("Robotic link lengths must be positive non-zero values.")
            
        # Convert joint angles from degrees to radians
        t1_rad = math.radians(theta1_degrees)
        t2_rad = math.radians(theta2_degrees)
        
        # Compute Cartesian coordinates of the tip (end-effector)
        x = (link1_length * math.cos(t1_rad)) + (link2_length * math.cos(t1_rad + t2_rad))
        y = (link1_length * math.sin(t1_rad)) + (link2_length * math.sin(t1_rad + t2_rad))
        
        return x, y

    @staticmethod
    def inverse_kinematics_2r_planar(link1_length: float, link2_length: float, target_x: float, target_y: float) -> Tuple[float, float]:
        """
        Calculates the required joint angles (theta1, theta2) in degrees to reach a target (X, Y) point.
        Uses the cosine law to solve the geometric problem (Elbow-Up configuration by default).
        """
        if link1_length <= 0 or link2_length <= 0:
            raise GeometricViolationError("Robotic link lengths must be positive non-zero values.")
            
        # Distance from origin to target point squared
        d_squared = (target_x ** 2) + (target_y ** 2)
        d = math.sqrt(d_squared)
        
        # Check if the target point is outside the robot's physical reach (workspace)
        if d > (link1_length + link2_length) or d < abs(link1_length - link2_length):
            raise GeometricViolationError("Target coordinate is outside the reachable workspace of the robotic arm.")
            
        # Law of Cosines for Theta2
        cos_theta2 = (d_squared - (link1_length ** 2) - (link2_length ** 2)) / (2.0 * link1_length * link2_length)
        # Numerical boundary guard to prevent floating point inaccuracies from crashing acos
        cos_theta2 = max(-1.0, min(1.0, cos_theta2))
        
        theta2_rad = math.acos(cos_theta2)
        
        # Geometric solution for Theta1
        alpha = math.atan2(target_y, target_x)
        beta = math.atan2(link2_length * math.sin(theta2_rad), link1_length + (link2_length * math.cos(theta2_rad)))
        
        theta1_rad = alpha - beta
        
        return math.degrees(theta1_rad), math.degrees(theta2_rad)
