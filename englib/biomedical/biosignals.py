"""
Mega Engineering Library - Biomedical Engineering: Biosignals Module
Handles physiological signal metrics, ECG/EEG wave interpretations, and heart rate conversions.
Validated against standard biomedical signal processing guidelines (e.g., Tompkins).
"""

from englib.common.exceptions import PhysicalBoundaryError

class Biosignals:

    @staticmethod
    def calculate_heart_rate_from_rr_interval(rr_interval_seconds: float) -> float:
        """
        Calculates the Heart Rate (BPM) from an ECG signal's R-to-R interval.
        BPM = 60 / RR_interval
        """
        if rr_interval_seconds <= 0.2 or rr_interval_seconds > 3.0:
            # Human physiological limits check (0.2s = 300 BPM, 3s = 20 BPM)
            raise PhysicalBoundaryError("RR interval falls outside realistic human physiological boundaries.")

        return 60.0 / rr_interval_seconds
