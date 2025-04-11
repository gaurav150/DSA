num_of_test_cases = int(input())

for _ in range(num_of_test_cases):
    cost_of_balloons = list(map(int, input().split()))
    num_of_participants = int(input())
    
    count_problem1 = 0
    count_problem2 = 0
    
    for _ in range(num_of_participants):
        a, b = map(int, input().split())
        count_problem1 += a
        count_problem2 += b

    # Two possibilities: assign costs either way
    cost1 = cost_of_balloons[0] * count_problem1 + cost_of_balloons[1] * count_problem2
    cost2 = cost_of_balloons[1] * count_problem1 + cost_of_balloons[0] * count_problem2
    
    print(min(cost1, cost2))

'''
2
9 6
10
1 1
1 1
0 1
0 0
0 1
0 0
0 1
0 1
1 1
0 0
1 9
10
0 1
0 0
0 0
0 1
1 0
0 1
0 1
0 0
0 1
0 0
'''