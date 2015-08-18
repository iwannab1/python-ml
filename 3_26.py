import numpy as np
import pandas as pd

def main():
    print(do_exercise())

def do_exercise():
    # 1
    aapl = pd.read_csv("data/aapl.csv")

    # 2
    date_index = aapl.Date
    aapl.index = pd.to_datetime(date_index)
    # 3
    new_aapl = aapl[['Open','Close','Volume']]
    print(new_aapl)
    # 4
    return new_aapl[:]['1989':'2003-04']

if __name__ == "__main__":
    main()
