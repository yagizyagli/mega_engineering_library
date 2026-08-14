"""
Mega Engineering Library - Biomedical Engineering Validation Suite
"""
import pytest
from englib.biomedical.biosignals import Biosignals
from englib.common.exceptions import PhysicalBoundaryError

def test_biosignal_heart_rate():
    """Verifies human physiological limits constraints for ECG metrics."""
    bpm = Biosignals.calculate_heart_rate_from_rr_interval(0.8)
    assert bpm == 75.0
    with pytest.raises(PhysicalBoundaryError):
        Biosignals.calculate_heart_rate_from_rr_interval(5.0)
