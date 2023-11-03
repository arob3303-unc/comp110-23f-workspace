"""My Function."""

def odd_and_even(list1: list[int]) -> list[int]:
    list2: list[int] = list1
    new_list: list[int] = []
    i: int = 0

    for num in list2:
        if num % 2 == 1:
            if i % 2 == 0:
                new_list.append(num)
                i += 1
            else:
                i += 1
        else:
            i += 1
    return new_list

print(odd_and_even([2, 3, 4, 5]))
print(odd_and_even([7 , 8 , 10 , 10 , 5 , 12 , 3 , 2 , 11 , 8]))


