"""
Mega Engineering Library - Mechatronics & Robotics Validation Suite
"""
import pytest
from englib.mechatronics.kinematics import RoboticKinematics

def test_robotic_forward_kinematics():
    """Validates 2R planar robotic arm tip location geometry mapping."""
    x, y = RoboticKinematics.forward_kinematics_2r_planar(1.0, 1.0, 0.0, 90.0)
    assert round(x, 2) == 1.0
    assert round(y, 2) == 1.0
