def max_profit(N, M, prices):
    assert 1 <= N <= 10**2, "Constraint: 1 <= N <= 10^2"
    assert 1 <= M <= 10**3, "Constraint: 1 <= M <= 10^3"
    assert all(1 <= Ai <= 10**2 for Ai in prices), "Constraint: 1 <= Ai <= 10^2"

    max_profit = 0
    max_profit_index = -1

    for i in range(N):
        remaining_money = M
        current_profit = 0
        for j in range(i, N):
            if prices[j] <= remaining_money:
                remaining_money -= prices[j]
                current_profit += prices[j]
            else:
                break

        if current_profit > max_profit:
            max_profit = current_profit
            max_profit_index = i

    return max_profit, max_profit_index

# Example usage:

# Input #1
N1, M1 = map(int, input().split())
prices1 = list(map(int, input().split()))
output1 = max_profit(N1, M1, prices1)
print(output1)

# Input #2
N2, M2 = map(int, input().split())
prices2 = list(map(int, input().split()))
output2 = max_profit(N2, M2, prices2)
print(output2)
