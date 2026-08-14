"""
Mega Engineering Library - Industrial Engineering Validation Suite
"""
import pytest
from englib.industrial.supply_chain import SupplyChainManagement

def test_economic_order_quantity():
    """Validates supply chain logistics cost minimization math models."""
    eoq = SupplyChainManagement.calculate_economic_order_quantity(2000.0, 50.0, 4.0)
    assert eoq == 223.60679774997897
