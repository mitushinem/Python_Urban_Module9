
def apply_all_func(int_list, *functions):
    result_dict = {}
    for func in functions:
        res = func(int_list)
        result_dict[func.__name__] = res

    return result_dict


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))