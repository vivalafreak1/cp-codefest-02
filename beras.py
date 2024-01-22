def untung(N, M, profit):
    total_profit = sum(profit)
    net_profit = total_profit - M
    max_profit = max(profit)
    return max_profit, net_profit
try:
    N, M = map(int, input().split())
    if not (1 <= N <= 10**2 and 1 <= M <= 10**3):
        raise ValueError("not valid")
    profit = list(map(int, input().split()))
    if not all(1 <= Ai <= 10**2 for Ai in profit):
        raise ValueError("not valid")
except ValueError as e:
    print(f"Error: {e}")
    exit()
max_profit, net_profit = untung(N, M, profit)
print(max_profit, net_profit)
