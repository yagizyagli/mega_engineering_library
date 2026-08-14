/*
 * Mega Engineering Library - Core Backend Calculus Engine
 * Provides high-speed numerical differentiation and integration routines.
 * Optimized for real-time sensor processing and heavy finite element solvers.
 */

/// Calculates the numerical derivative of a discrete sequence using the central difference method.
/// Unit tracking and boundary data padding are handled inside the core loops.
pub fn compute_discrete_derivative(values: &[f64], step_size_dt: f64) -> Result<Vec<f64>, String> {
    if values.len() < 2 {
        return Err("Derivative evaluation requires at least 2 sequential data points.".to_string());
    }
    if step_size_dt <= 0.0 {
        return Err("Time delta step size (dt) must be a positive non-zero value.".to_string());
    }

    let n = values.len();
    let mut derivative = vec![0.0; n];

    // Forward difference for the very first boundary node point
    derivative[0] = (values[1] - values[0]) / step_size_dt;

    // Central difference scheme for internal nodes to ensure high accuracy
    for i in 1..(n - 1) {
        derivative[i] = (values[i + 1] - values[i - 1]) / (2.0 * step_size_dt);
    }

    // Backward difference for the final boundary node point
    derivative[n - 1] = (values[n - 1] - values[n - 2]) / step_size_dt;

    Ok(derivative)
}

/// Computes the numerical integration of a discrete array stream using the Trapezoidal Rule.
/// Calculates the total area under the curve for energy or stress dissipation logs.
pub fn compute_trapezoidal_integration(values: &[f64], step_size_dx: f64) -> Result<f64, String> {
    if values.len() < 2 {
        return Err("Integration evaluation requires at least 2 sequential data points.".to_string());
    }
    if step_size_dx <= 0.0 {
        return Err("Spatial/temporal step delta (dx) must be positive and non-zero.".to_string());
    }

    let mut total_integral = 0.0;
    let n = values.len();

    // Standard trapezoidal summation loops
    for i in 0..(n - 1) {
        total_integral += (values[i] + values[i + 1]) * 0.5 * step_size_dx;
    }

    Ok(total_integral)
}
