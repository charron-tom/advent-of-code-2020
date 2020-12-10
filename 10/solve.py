def dp(adapters):
    v = [0] * (max(adapters) + 3)
    v[adapters[-1]] = 1
    i = len(adapters) - 1
    while i >= 0:
        adapter = adapters[i]
        if adapter + 1 in adapters:
            v[adapter] += v[adapter + 1]
        if adapter + 2 in adapters:
            v[adapter] += v[adapter + 2]
        if adapter +3 in adapters:
            v[adapter] += v[adapter + 3]
        i -= 1
    return v[adapters[0]]



def part1(adapters):
    diff_1 = 0
    diff_3 = 0
    for i in range(len(adapters) - 1):
        if adapters[i+1] - adapters[i] == 1:
            diff_1 += 1
        elif adapters[i+1] - adapters[i] == 3:
            diff_3 += 1
    return diff_1 * diff_3

def main():
    with open("puzzle", "r") as f:
        adapters = [0]
        for line in f:
            adapters.append(int(line.strip()))
        adapters.sort()
        adapters.append(adapters[-1] + 3)
        return dp(adapters)


if __name__ == "__main__":
    print main()
