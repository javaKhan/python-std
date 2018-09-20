if __name__ == '__main__':
    a, b, result = 0, 1, 0
    maxValue = 1000
    while result < maxValue:
        result = a + b
        print("a:", a, "  b:", b, "  result:", result)
        a = b
        b = result
