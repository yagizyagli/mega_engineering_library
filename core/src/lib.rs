use pyo3::prelude::*;

// Reference the core sub-modules explicitly
pub mod common {
    pub mod matrix;
    pub mod calculus;
    pub mod solvers;
}

pub mod physics {
    pub mod fem_solver;
    pub mod cfd_solver;
}

/// Multiplies structural load profiles or vector factors at raw hardware speed.
#[pyfunction]
fn compute_hardware_stress_limit(load: f64, area: f64, safety_factor: f64) -> PyResult<f64> {
    if area <= 0.0 {
        return Err(pyo3::exceptions::PyValueError::new_err("Cross-sectional area must be greater than zero."));
    }
    Ok((load / area) * safety_factor)
}

/// Computes a fast scalar matrix dot product for multi-dimensional engineering conversions.
#[pyfunction]
fn fast_scalar_dot_product(vector_a: Vec<f64>, vector_b: Vec<f64>) -> PyResult<f64> {
    if vector_a.len() != vector_b.len() {
        return Err(pyo3::exceptions::PyValueError::new_err("Mismatched engineering vector lengths for dot product."));
    }
    let dot: f64 = vector_a.iter().zip(vector_b.iter()).map(|(a, b)| a * b).sum();
    Ok(dot)
}

/// Exposes the high-speed 2D matrix multiplication routine to Python interface layers.
#[pyfunction]
fn fast_matrix_multiply_2d(matrix_a: Vec<Vec<f64>>, matrix_b: Vec<Vec<f64>>) -> PyResult<Vec<Vec<f64>>> {
    match common::matrix::multiply_matrices_2d(&matrix_a, &matrix_b) {
        Ok(result) => Ok(result),
        Err(err) => Err(pyo3::exceptions::PyValueError::new_err(err)),
    }
}

/// Exposes the hardware-accelerated discrete derivative routine to Python.
#[pyfunction]
fn fast_discrete_derivative(values: Vec<f64>, step_size_dt: f64) -> PyResult<Vec<f64>> {
    match common::calculus::compute_discrete_derivative(&values, step_size_dt) {
        Ok(result) => Ok(result),
        Err(err) => Err(pyo3::exceptions::PyValueError::new_err(err)),
    }
}

/// Exposes the hardware-accelerated trapezoidal integration engine to Python.
#[pyfunction]
fn fast_trapezoidal_integration(values: Vec<f64>, step_size_dx: f64) -> PyResult<f64> {
    match common::calculus::compute_trapezoidal_integration(&values, step_size_dx) {
        Ok(result) => Ok(result),
        Err(err) => Err(pyo3::exceptions::PyValueError::new_err(err)),
    }
}

/// Exposes the hardware-accelerated FEM local stiffness matrix assembly to Python.
#[pyfunction]
fn fast_fem_local_stiffness_assembly(mut global_matrix: Vec<Vec<f64>>, local_matrix: Vec<Vec<f64>>, node_indices: Vec<usize>) -> PyResult<Vec<Vec<f64>>> {
    match physics::fem_solver::assemble_local_stiffness_2d(&mut global_matrix, &local_matrix, &node_indices) {
        Ok(_) => Ok(global_matrix),
        Err(err) => Err(pyo3::exceptions::PyValueError::new_err(err)),
    }
}

/// Exposes the hardware-accelerated 1D advection-diffusion CFD solver to Python.
#[pyfunction]
fn fast_cfd_advection_diffusion_1d(grid_size: usize, velocity_u: f64, diffusion_d: f64, delta_x: f64) -> PyResult<Vec<f64>> {
    match physics::cfd_solver::compute_steady_advection_diffusion_1d(grid_size, velocity_u, diffusion_d, delta_x) {
        Ok(result) => Ok(result),
        Err(err) => Err(pyo3::exceptions::PyValueError::new_err(err)),
    }
}

/// Unified entry point for the compiled high-speed Rust core extension module
#[pymodule]
fn core_backend(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(compute_hardware_stress_limit, m)?)?;
    m.add_function(wrap_pyfunction!(fast_scalar_dot_product, m)?)?;
    m.add_function(wrap_pyfunction!(fast_matrix_multiply_2d, m)?)?;
    m.add_function(wrap_pyfunction!(fast_discrete_derivative, m)?)?;
    m.add_function(wrap_pyfunction!(fast_trapezoidal_integration, m)?)?;
    m.add_function(wrap_pyfunction!(fast_fem_local_stiffness_assembly, m)?)?;
    m.add_function(wrap_pyfunction!(fast_cfd_advection_diffusion_1d, m)?)?;
    Ok(())
}
