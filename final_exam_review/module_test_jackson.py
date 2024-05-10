import read_two_columns_text
import calculate_bivariate_statistics
import calculate_quadratic_fit
import fit_curve_array
import plot_data_with_fit
import calculate_lowest_eigenvectors
import annotate_plot

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
