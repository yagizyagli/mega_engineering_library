"""
Mega Engineering Library - Aerospace Engineering Validation Suite
Verifies continuum aerodynamics forces and orbital trajectory escape profiles.
"""

import pytest
from englib.aerospace.aerodynamics import Aerodynamics
from englib.aerospace.orbital_mechanics import OrbitalMechanics

def test_aerodynamic_lift():
    """Validates wing fluid boundary load assertions."""
    # Dynamic pressure = 1200 Pa, Area = 15 m², Cl = 1.2
    lift = Aerodynamics.calculate_aerodynamic_force(1200.0, 15.0, 1.2)
    assert lift == 21600.0

def test_planetary_escape_velocity():
    """Validates gravity well escape trajectories."""
    # Earth benchmark parameters setup
    earth_mu = 3.986004418e14
    earth_radius = 6378137.0
    v_esc = OrbitalMechanics.calculate_escape_velocity(earth_mu, earth_radius)
    assert v_esc > 11100.0  # Must be approximately 11.2 km/s
