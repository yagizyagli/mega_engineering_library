"""
Mega Engineering Library - Electrical & Electronics Engineering: Microelectronics Module
Contains core mathematical models for semiconductor physics and MOSFET/BJT transistor operation.
Validated against standard microelectronics literature (e.g., Sedra & Smith, Razavi).
"""

from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class Microelectronics:

    @staticmethod
    def calculate_mosfet_saturation_current(process_transconductance: float, width_over_length: float, gate_to_source_voltage: float, threshold_voltage: float) -> float:
        """
        Calculates the drain current (Id) of an NMOS transistor operating in the saturation region.
        Id = 0.5 * k'_n * (W/L) * (Vgs - Vth)^2
        Unit: Amperes (A)
        """
        if process_transconductance <= 0:
            raise PhysicalBoundaryError("Process transconductance parameter (k'_n) must be positive.")
        if width_over_length <= 0:
            raise GeometricViolationError("Transistor aspect ratio (W/L) must be a positive non-zero physical geometry ratio.")
        if gate_to_source_voltage < threshold_voltage:
            raise PhysicalBoundaryError("Transistor is not in the saturation region (Vgs must be greater than or equal to Vth).")

        overdrive_voltage = gate_to_source_voltage - threshold_voltage
        drain_current = 0.5 * process_transconductance * width_over_length * (overdrive_voltage ** 2)
        return drain_current
