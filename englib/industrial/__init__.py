"""
Industrial Engineering & Operations Research Core Suite - 100% Complete Production Build
Unified entry point for linear programming models, Little's queuing arrivals,
classical EOQ supply chain inventory sizing, and Six Sigma process capability Cp quality metrics.
"""

from englib.industrial.linear_programming import LinearProgramming
from englib.industrial.stochastic_models import StochasticModels
from englib.industrial.supply_chain import SupplyChainManagement
from englib.industrial.quality_control import QualityControl

__all__ = [
    "LinearProgramming",
    "StochasticModels",
    "SupplyChainManagement",
    "QualityControl"
]
