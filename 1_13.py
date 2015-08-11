import statsmodels.api
import numpy
import elice_utils

def main():
    (N, X, Y) = read_data()
    results = do_simple_regression(N, X, Y)

    # 3
    print(elice_utils.visualize(X, Y, results))

def read_data():
    # 1
    N = int(input().strip())

    X = []
    Y = []
    for i in range(0, N):
        splitted = input().strip().split()
        x = float(splitted[0])
        y = float(splitted[1])
        X.append(x)
        Y.append(y)

    return (N, X, Y)

def do_simple_regression(N, X, Y):
    # 2
    X = numpy.array(X).T
    X = statsmodels.api.add_constant(X)
    results = statsmodels.api.OLS(Y,X).fit()
    

    return results

if __name__ == "__main__":
    main()
