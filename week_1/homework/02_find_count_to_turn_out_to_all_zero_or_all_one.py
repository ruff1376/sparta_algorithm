input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    cnt = 0
    for i in range(0, len(string) - 1):
        if string[i] != string[i + 1]:
            cnt += 1
    if cnt % 2 == 0:
        return int(cnt / 2)
    else:
        return int((cnt + 1) / 2)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
