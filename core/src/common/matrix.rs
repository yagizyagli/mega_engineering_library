/*
 * Mega Engineering Library - Core Backend Matrix Engine
 * Handles high-speed linear algebra and matrix multiplications at the hardware layer.
 * Designed for massive structural, mechatronic, and geodetic simulation frameworks.
 */

/// Performs a highly optimized, raw-loop multiplication of two 2D matrices.
/// Implements standard index ordering to maximize CPU cache locality benefits.
pub fn multiply_matrices_2d(matrix_a: &[Vec<f64>], matrix_b: &[Vec<f64>]) -> Result<Vec<Vec<f64>>, String> {
    if matrix_a.is_empty() || matrix_b.is_empty() {
        return Err("Matrix matrices cannot be empty.".to_string());
    }

    let rows_a = matrix_a.len();
    let cols_a = matrix_a[0].len();
    let rows_b = matrix_b.len();
    let cols_b = matrix_b[0].len();

    if cols_a != rows_b {
        return Err("Dimension mismatch: Columns of Matrix A must exactly equal Rows of Matrix B.".to_string());
    }

    // Initialize result matrix with zeros
    let mut result = vec![vec![0.0; cols_b]; rows_a];

    // Transpose Matrix B to optimize memory cache hits significantly during dot-product loops
    let mut matrix_b_transposed = vec![vec![0.0; rows_b]; cols_b];
    for i in 0..rows_b {
        for j in 0..cols_b {
            matrix_b_transposed[j][i] = matrix_b[i][j];
        }
    }

    // High-speed parallel-ready multiplication block
    for i in 0..rows_a {
        for j in 0..cols_b {
            let mut dot_product = 0.0;
            for k in 0..cols_a {
                dot_product += matrix_a[i][k] * matrix_b_transposed[j][k];
            }
            result[i][j] = dot_product;
        }
    }

    Ok(result)
}
