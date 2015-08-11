import statsmodels.api
import numpy

def main():
    (N, X, Y) = read_data()

    results = do_multivariate_regression(N, X, Y)
    print(results.summary())

    effective_variables = get_effective_variables(results)
    print(effective_variables)

def read_data():
    # 1
    N = 30
    students = numpy.loadtxt("c:\\temp\\students.txt", delimiter=" ", skiprows=1)
    X = students[:,0:5]
    Y = students[:,5]

    print(X)

    # X must be numpy.array in (30 * 5) shape.
    # Y must be 1-dimensional numpy.array.
    X = numpy.array(X)
    Y = numpy.array(Y)
    return (N, X, Y)

def do_multivariate_regression(N, X, Y):
    # 2
    results = statsmodels.api.OLS(Y,X).fit()
    return results

def get_effective_variables(results):
    eff_vars = []
	# 3
    pvalues = results.pvalues

    idx = 1
    for p in pvalues:
        if p < 0.05:
            eff_vars.append("X" + str(idx))
        idx += 1

    return eff_vars

def print_students_data():
    with open("students.dat") as f:
        for line in f:
            print(line)

if __name__ == "__main__":
    main()
