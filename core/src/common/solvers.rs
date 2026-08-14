/*
 * Mega Engineering Library - Core Backend Numerical Solvers Engine
 * Handles high-speed root-finding and iterative convergence solvers for non-linear equations.
 * Optimized for complex thermodynamic and fluid dynamics equation profiles.
 */

/// Solves a non-linear engineering equation using a fast numerical Newton-Raphson approximation.
/// Expects a function pointer representing the target profile and its localized derivative.
pub fn solve_newton_raphson<F, D>(
    initial_guess: f64,
    tolerance: f64,
    max_iterations: usize,
    f: F,
    f_prime: D,
) -> Result<f64, String>
where
    F: Fn(f64) -> f64,
    D: Fn(f64) -> f64,
{
    if tolerance <= 0.0 {
        return Err("Convergence tolerance threshold must be a positive non-zero value.".to_string());
    }
    if max_iterations == 0 {
        return Err("Maximum iteration limit must be greater than zero.".to_string());
    }

    let mut x_n = initial_guess;

    for _ in 0..max_iterations {
        let fx = f(x_n);
        let dfx = f_prime(x_n);

        if dfx.abs() < 1e-12 {
            return Err("Newton-Raphson failure: Derivative close to zero. Division by zero anomaly.".to_string());
        }

        // Newton-Raphson core step formula: x_{n+1} = x_n - f(x_n)/f'(x_n)
        let next_x = x_n - (fx / dfx);

        // Check if the solution matches our tolerance precision requirement
        if (next_x - x_n).abs() < tolerance {
            return Ok(next_x);
        }

        x_n = next_x;
    }

    Err(format!(
        "Solver failed to converge within the maximum limit of {} iterations.",
        max_iterations
    ))
}
