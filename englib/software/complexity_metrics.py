"""
Mega Engineering Library - Software & Systems Engineering: Complexity Metrics Module
Handles code cyclomatic density, structural graph complexities, and software test paths.
Validated against standard software verification guidelines (e.g., McCabe's Complexity Metric).
"""

from englib.common.exceptions import GeometricViolationError

class ComplexityMetrics:

    @staticmethod
    def calculate_mccabe_cyclomatic_complexity(edges: int, nodes: int, connected_components_p: int = 1) -> int:
        """
        Calculates the Cyclomatic Complexity M (or V(G)) of a software module using a Control Flow Graph.
        M = E - N + 2P
        Where:
        E = Number of edges in the graph
        N = Number of nodes in the graph
        P = Number of connected components (defaults to 1 for a single program/function module)
        Interpretation:
        - 1 to 10: Simple code, low risk
        - 11 to 20: Complex code, moderate risk
        - >20: Highly complex code, untestable/high risk
        """
        if edges < 0 or nodes <= 0 or connected_components_p < 0:
            raise GeometricViolationError("Control flow graph structures (edges, nodes, paths) cannot be negative or zero nodes.")
            
        complexity = edges - nodes + (2 * connected_components_p)
        
        if complexity < 1:
            raise ValueError("Invalid graph configuration: Cyclomatic complexity cannot drop below 1.")
            
        return complexity
