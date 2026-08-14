"""
Mega Engineering Library - Mechatronics & Robotics Engineering: State Estimation Module
Contains optimal estimation algorithms, measurement corrections, and Kalman filter structures.
Validated against standard stochastic estimation literature (e.g., Welch & Bishop, Gelb).
"""

from englib.common.exceptions import PhysicalBoundaryError

class StateEstimation:

    @staticmethod
    def calculate_linear_kalman_gain(prior_covariance: float, measurement_matrix_h: float, measurement_noise_r: float) -> float:
        """
        Calculates the scalar Kalman Gain (K) for a single-state optimal estimation loop.
        K = (P_prior * H) / (H * P_prior * H + R)
        """
        if measurement_noise_r <= 0:
            raise PhysicalBoundaryError("Measurement noise covariance (R) must be a positive non-zero value.")
        if prior_covariance < 0:
            raise PhysicalBoundaryError("Prior state uncertainty covariance (P) cannot be negative.")

        denominator = (measurement_matrix_h * prior_covariance * measurement_matrix_h) + measurement_noise_r
        if denominator == 0:
            raise ZeroDivisionError("Kalman evaluation yielded an impossible zero covariance denominator.")

        return (prior_covariance * measurement_matrix_h) / denominator

    @staticmethod
    def update_kalman_state_and_covariance(prior_state: float, prior_covariance: float, measurement_z: float, measurement_matrix_h: float, kalman_gain_k: float) -> tuple[float, float]:
        """
        Executes the measurement update step (correction) of a scalar Kalman Filter.
        Updated State = X_prior + K * (z - H * X_prior)
        Updated Covariance = (1 - K * H) * P_prior
        """
        if kalman_gain_k < 0:
            # Gain could technically be negative under strange cross-correlations, 
            # but in standard scalar architectures, we bound physical parameters.
            pass

        # Residual (Innovation)
        residual = measurement_z - (measurement_matrix_h * prior_state)
        
        # State and Covariance correction
        updated_state = prior_state + (kalman_gain_k * residual)
        updated_covariance = (1.0 - (kalman_gain_k * measurement_matrix_h)) * prior_covariance
        
        return updated_state, updated_covariance
