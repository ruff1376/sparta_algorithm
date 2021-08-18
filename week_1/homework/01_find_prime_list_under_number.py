input = 20

result_array = []


def is_prime(n):
    for i in result_array:
        if n % i == 0 and i ** 2 <= n:
            return False
    return True


def find_prime_list_under_number(number):
    for i in range(2, number + 1):
        if is_prime(i):
            result_array.append(i)
    return result_array


result = find_prime_list_under_number(input)
print(result)
