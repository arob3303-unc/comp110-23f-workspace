def free_biscuits(info: dict[str, list[int]]) -> dict[str, bool]:
    result: dict[str, bool] = {}

    for games in info:
        print(games)
        i: int = 0
        points: int = 0
        game_list = info[games]
        while i < len(info[games]):
            points += game_list[i]
            i += 1
        if points >= 100:
            result[games] = True
        if points < 100:
            result[games] = False
    return result

print(free_biscuits({ "UNCvsDuke": [38, 20, 42], "UNCvsState": [9, 51, 16, 23] }))

def max_key(input: dict[str, list[int]]) -> str:
    result: str = ''
    max: int = 0
    for key in input:
        sum: int = 0
        sum_list: list[int] = input[key]
        for item in sum_list:
            sum += item
        if sum > max:
            max = sum
            result = key
    return result

print(max_key({"a": [1,2,13], "b": [4,5,6]}))
        
        
        

