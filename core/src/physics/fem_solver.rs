/*
 * Mega Engineering Library - Core Backend Physics Engine: FEM Solver Module
 * Handles element stiffness matrix assembly and structural displacement vectors.
 * Optimized for discrete finite element modeling across structural components.
 */

/// Assembles a 2x2 local element stiffness matrix into a global structural stiffness matrix array.
/// Crucial for large scale beam and frame structural calculations.
pub fn assemble_local_stiffness_2d(
    global_matrix: &mut Vec<Vec<f64>>,
    local_matrix: &[Vec<f64>],
    node_indices: &[usize],
) -> Result<(), String> {
    if local_matrix.len() != 2 || local_matrix[0].len() != 2 || node_indices.len() != 2 {
        return Err("FEM Engine Error: This baseline routine only supports 2x2 local 1D/2D element configurations.".to_string());
    }

    let global_size = global_matrix.len();

    // Verify system freedom boundaries before memory mapping execution
    for &idx in node_indices {
        if idx >= global_size {
            return Err(format!(
                "FEM Boundary Error: Local node index {} exceeds global system degree of freedom limit ({}).",
                idx, global_size
            ));
        }
    }

    // Map and assemble localized element stiffness matrices into the global system frame
    for i in 0..2 {
        for j in 0..2 {
            let global_row = node_indices[i];
            let global_col = node_indices[j];
            global_matrix[global_row][global_col] += local_matrix[i][j];
        }
    }

    Ok(())
}
