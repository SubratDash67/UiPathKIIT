def numTrees(n):
    catalan = [0] * (n + 1)
    catalan[0] = 1
    catalan[1] = 1
    for i in range(2, n + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - j - 1]
    return catalan[n]


def main():
    N = int(input("Enter the number of nodes (N): "))
    print(
        f"Number of unique BSTs that can be constructed with {N} nodes is: {numTrees(N)}"
    )


if __name__ == "__main__":
    main()
