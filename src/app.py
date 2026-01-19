def dot(x, y):
    if len(x) != len(y):
        raise ValueError(f"Vector length mismatch, got {x}, {y}")
    return sum(x[i]*y[i] for i in range(len(x)))


def main():

    x = (-1,1)
    y = (1,-1)
    product = dot(x, y)

    print("Product:", product)



if __name__ == "__main__":
    main()