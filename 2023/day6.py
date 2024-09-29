import math

time = [58, 99, 64, 69]
record = [478, 2232, 1019, 1071]

# time = [7, 15, 30]
# record = [9, 40, 200]


def part1():
    out = 1
    for i in range(len(time)):
        cur_total_time = time[i]
        cur_record = record[i]
        record_breaks = 0
        for hold_time in range(1, cur_total_time):
            if calc_dist(hold_time, cur_total_time) > cur_record:
                record_breaks += 1
        out *= record_breaks
    return out


def calc_dist(held, total):
    return held * (total - held)


# -held**2 + total*held

# -x^2 + time*x


def part2():
    time = 58996469
    record = 478223210191071

    # time = 71530
    # record = 940200

    # -x^2 + 58996469*x - 478223210191071

    print((time * time))
    print(4 * record)

    root = math.sqrt(time**2 - 4 * record)

    lower = (time - root) / 2 // 1 + 1
    upper = (time + root) / 2 // 1

    print(upper, lower)

    # time = 71530
    # record = 940200

    # left = 0
    # right = time // 2
    # lower = 0
    # upper = time - 14

    # while lower == 0:
    #     mid = (left + right) // 2
    #     mid_bool = calc_dist(mid, time) > record
    #     plus_bool = calc_dist(mid + 1, time) > record
    #     if mid_bool != plus_bool:
    #         lower = mid + 1
    #     if mid_bool:
    #         right = mid-1
    #     else:
    #         left = mid+1

    # left = 3*time // 4
    # right = time

    # while upper == 0:
    #     mid = (left + right) // 2
    #     mid_bool = calc_dist(mid) > record
    #     plus_bool = calc_dist(mid + 1) > record
    #     if mid_bool != plus_bool:
    #         upper = mid
    #     if not mid_bool:
    #         right = mid-1
    #     else:
    #         left = mid+1

    # print(upper, lower)
    # print(calc_dist(upper, time), calc_dist(upper + 1, time))
    # print(calc_dist(lower, time), calc_dist(lower-1, time))

    return upper - lower + 1


# print(part1())

print(part2())
