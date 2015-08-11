import numpy

def main():
    (N, X, Y) = read_data()
    print(N)
    print(X)
    print(Y)

def read_data():
    # 1
    mat = []
    N = int(input())
    for i in range(N):
        row = [float(x) for x in input().strip().split( " ")]
        mat.append(row)
    arr = numpy.array(mat)
    
    # 2
    X = arr[:, 0].tolist()
    Y = arr[:, 1].tolist()
    return (N, X, Y)

if __name__ == "__main__":
    main()