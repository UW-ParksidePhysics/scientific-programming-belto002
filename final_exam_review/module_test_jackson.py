from beltoya_final_exam import read_two_columns_text, calculate_quadratic_fit, calculate_bivariate_statistics, \
    calculate_lowest_eigenvectors, annotate_plot
import fit_curve_array
import plot_data_with_fit

if __name__ == "__main__":
    modules = [
        read_two_columns_text,
        calculate_bivariate_statistics,
        calculate_quadratic_fit,
        fit_curve_array,
        plot_data_with_fit,
        calculate_lowest_eigenvectors,
        annotate_plot
    ]

    for module in modules:
        module_name = module.__name__
        module_file = module_name.replace('_', '') + '.py'
        with open(module_file) as f:
            code = f.read()
        exec(code)
