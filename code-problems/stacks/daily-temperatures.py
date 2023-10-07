"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

FEEDBACK: 
make sure to pay attention to the constraints of the problem. It will be helpful.
"""

temps1 = [73, 74, 75, 71, 69, 72, 76, 73]  # ans = [1, 1, 4, 2, 1, 1, 0, 0]

"""
My brute force approach.
"""


def findDaily(temps):

    days = []

    while(len(temps) > 0):
        # append zero if on the last day in the list
        if len(temps) == 1:
            days.append(0)

        temp = temps.pop(0)
        for index, future_temp in enumerate(temps):
            index += 1
            if future_temp > temp:
                days.append(index)
                break
            else:
                if index == len(temps):
                    days.append(0)
    return days


# print(findDaily(temps1))

"""
Next Array Approach

Intuition

The problem statement asks us to find the next occurrence of a warmer temperature. Because temperatures can only be in [30, 100], if the temperature right now is say, T[i] = 50, we only need to check for the next occurrence of 51, 52, ..., 100 and take the one that occurs soonest.

Algorithm

Let's process each i in reverse (decreasing order). At each T[i], to know when the next occurrence of say, temperature 100 is, we should just remember the last one we've seen, next[100].

Then, the first occurrence of a warmer value occurs at warmer_index, the minimum of next[T[i]+1], next[T[i]+2], ..., next[100].
"""


def dailyTemperatures(T):
    MAX_TEMP = 101
    # nxt stores the index of a temp given temp.
    # if 77 was found on index 98
    # to get the index of temp 77 --> nxt[77] = 98
    nxt = [float('inf')] * MAX_TEMP
    ans = [0] * len(T)

    # Loop in reverse
    for index in xrange(len(T) - 1, -1, -1):
        # Use MAX_TEMP so min(nxt[t]) has a default value
        # take the min of the newly created list of indexes
        # then choose the lowest index
        # [45, 30, 32, ...]
        warmer_index = min(nxt[temp] for temp in xrange(T[index]+1, MAX_TEMP))
        if warmer_index < float('inf'):
            ans[index] = warmer_index - index
        nxt[T[index]] = index
    return ans


# print(dailyTemperatures(temps1))

"""
Approach #2: Stack [Accepted]
Intuition

Consider trying to find the next warmer occurrence at T[i]. What information (about T[j] for j > i) must we remember?

Say we are trying to find T[0]. If we remembered T[10] = 50, knowing T[20] = 50 wouldn't help us, as any T[i] that has its next warmer ocurrence at T[20] would have it at T[10] instead. However, T[20] = 100 would help us, since if T[0] were 80, then T[20] might be its next warmest occurrence, while T[10] couldn't.

Thus, we should remember a list of indices representing a strictly increasing list of temperatures. For example, [10, 20, 30] corresponding to temperatures [50, 80, 100]. When we get a new temperature like T[i] = 90, we will have [5, 30] as our list of indices (corresponding to temperatures [90, 100]). The most basic structure that will satisfy our requirements is a stack, where the top of the stack is the first value in the list, and so on.

Algorithm

As in Approach #1, process indices i in descending order. We'll keep a stack of indices such that T[stack[-1]] < T[stack[-2]] < ..., where stack[-1] is the top of the stack, stack[-2] is second from the top, and so on; and where stack[-1] > stack[-2] > ...; and we will maintain this invariant as we process each temperature.

After, it is easy to know the next occurrence of a warmer temperature: it's simply the top index in the stack.

Here is a worked example of the contents of the stack as we work through T = [73, 74, 75, 71, 69, 72, 76, 73] in reverse order, at the end of the loop (after we add T[i]). For clarity, stack only contains indices i, but we will write the value of T[i] beside it in brackets, such as 0 (73).

When i = 7, stack = [7 (73)]. ans[i] = 0.
When i = 6, stack = [6 (76)]. ans[i] = 0.
When i = 5, stack = [5 (72), 6 (76)]. ans[i] = 1.
When i = 4, stack = [4 (69), 5 (72), 6 (76)]. ans[i] = 1.
When i = 3, stack = [3 (71), 5 (72), 6 (76)]. ans[i] = 2.
When i = 2, stack = [2 (75), 6 (76)]. ans[i] = 4.
When i = 1, stack = [1 (74), 2 (75), 6 (76)]. ans[i] = 1.
When i = 0, stack = [0 (73), 1 (74), 2 (75), 6 (76)]. ans[i] = 1.
"""
#          0   1   2   3   4   5   6   7
temps1 = [73, 74, 75, 71, 69, 72, 76, 73]


def dailyTemps(T):
    T_LENGTH = len(T)
    ans = [0]*T_LENGTH
    stack = []  # store temps from hottest to coldest, right to left

    for idx in range(T_LENGTH-1, -1, -1):

        # while stack is non-empty and Temp in question is greater than the coldest
        # temperature on the stack, keep popping off the colder temperature
        while stack and T[idx] >= T[stack[-1]]:
            stack.pop()

        # We can find ourselves in two states right now.
        # One is where stack is now empty b/c we did not find a warmer temperature on the stack
        # Second, we stopped popping off from stack b/c we found a warmer temperature on the stack
        # Option one is unnecessary b/c ans is already filled with 0's
        # Option two
        if stack:
            ans[idx] = stack[-1] - idx
        stack.append(idx)

    return ans


print(dailyTemps(temps1))
