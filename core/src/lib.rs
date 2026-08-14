use pyo3::prelude::*;

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

/// Unified entry point for the compiled compiled high-speed Rust core extension module
#[pymodule]
fn core_backend(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(compute_hardware_stress_limit, m)?)?;
    m.add_function(wrap_pyfunction!(fast_scalar_dot_product, m)?)?;
    Ok(())
}
