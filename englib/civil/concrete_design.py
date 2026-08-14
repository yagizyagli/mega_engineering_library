"""
Mega Engineering Library - Civil Engineering: Reinforced Concrete Design Module
Handles ultimate strength design, bending capacities, and rebar reinforcement limits for concrete sections.
Validated against standard structural concrete literature and codes (e.g., ACI 318, Eurocode 2).
"""

from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class ConcreteDesign:

    @staticmethod
    def calculate_nominal_moment_capacity(rebar_area: float, yield_strength: float, effective_depth: float, concrete_strength: float, section_width: float) -> float:
        """
        Calculates the nominal bending moment capacity (Mn) of a singly reinforced rectangular concrete beam.
        Based on the ultimate strength design method (rectangular stress block assumption).
        
        Stress block depth (a) = (As * fy) / (0.85 * f'c * b)
        Moment Capacity (Mn) = As * fy * (d - a/2)
        Unit: Newton-meters (N·m)
        """
        if rebar_area <= 0 or effective_depth <= 0 or section_width <= 0:
            raise GeometricViolationError("Beam dimensions and rebar area must be positive geometric values.")
        if yield_strength <= 0 or concrete_strength <= 0:
            raise PhysicalBoundaryError("Material strengths (steel yield and concrete compressive) must be positive.")

        # Depth of equivalent rectangular stress block (a)
        stress_block_depth = (rebar_area * yield_strength) / (0.85 * concrete_strength * section_width)
        
        if stress_block_depth >= effective_depth:
            raise PhysicalBoundaryError("Over-reinforced or physically impossible section: Stress block depth exceeds effective depth.")

        # Nominal moment capacity calculation
        nominal_moment = rebar_area * yield_strength * (effective_depth - (stress_block_depth / 2.0))
        return nominal_moment

    @staticmethod
    def calculate_reinforcement_ratio(rebar_area: float, section_width: float, effective_depth: float) -> float:
        """
        Calculates the dimensionless reinforcement ratio (rho) of a concrete cross-section.
        rho = As / (b * d)
        """
        if section_width <= 0 or effective_depth <= 0:
            raise GeometricViolationError("Cross-sectional width and effective depth must be greater than zero.")
        if rebar_area < 0:
            raise GeometricViolationError("Rebar area cannot be negative.")

        return rebar_area / (section_width * effective_depth)
