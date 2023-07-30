params = {
    "queryStringParameters" : {
        "draw_index": 3,
        "nums": [4, 4, 8, 9, 11],
        "suits": [1, 2, 3, 2, 4]
    }

}

import json

def lambda_handler(event, context):
    score = 0
    cards = event["queryStringParameters"]
    fifteens_score = fifteens(cards)
    runs_score = runs(cards)
    pairs_score = pairs(cards)
    flush_score = flush(cards)
    nob_score = nob(cards)

    calculated_score = fifteens_score + runs_score + pairs_score + flush_score + nob_score
    print(calculated_score)
    score = {"value" : calculated_score}
    return {
        'statusCode': 200,
        'body': json.dumps(score)
    }

def fifteens(cards):
    nums = cards["nums"]
    suits = cards["suits"]
    score = 0

    for i in range(0, len(nums)):
        remaining_nums = nums.copy()

        del remaining_nums[i]

        for j in range(0, len(remaining_nums)):
            total = nums[i] + remaining_nums[j]
            if total == 15:
                print(f'{nums[i]} + {remaining_nums[j]} = {total}')
                print("The total is 15")
                score = score + 2

    score = score // 2 # Every had is double counted, need to divided by 2 to get the result
    print(f'The total score 15s is {score}')
    return score

def runs(cards):
    nums = cards["nums"]
    ordered_nums = nums.copy()
    ordered_nums.sort()
    score = 0
    max_count = 1
    print(f'The ordered nums are: {ordered_nums}')

    for i in range(0, len(ordered_nums)-1):
        count = 1
        next_i = i + 1

        for j in range(i, len(ordered_nums)):
            if ordered_nums[j] == ordered_nums[j-1]+1:
                count = count + 1

        if count > max_count:
            max_count = count

    print(f'The count is {max_count}') 

    if max_count > 2:
        score = max_count

    print(f'The total score for runs is {score}')
    return score  

def pairs(cards):
    score = 0
    nums = cards["nums"]
    ranked_nums = nums.copy()

    ranked_nums_set = set(ranked_nums.copy())
    ranked_nums_set_list = list(ranked_nums_set)
    
    for num in ranked_nums_set_list:
        count = ranked_nums.count(num)
        print(f'{num} has a count of {count}')
        if count == 2:
            score = score + 2
        elif count == 3:
            score = score + 6
        elif count == 4:
            score = score + 12
    return score 

def flush(cards):
    score = 0
    suits = cards["suits"]
    draw_index =  cards["draw_index"]

    hand_suits = suits.copy()
    del hand_suits[draw_index]
    print(f'hand_suits are {hand_suits}')
    hand_suits_set = set(hand_suits)

    if len(hand_suits_set) == 1:
        score = 4
        if list(hand_suits_set)[0] == suits[draw_index]:
            print("Extra Point from draw index suit")
            score = score + 1

    return score

def nob(cards):
    suits = cards["suits"]
    nums = cards["nums"]
    draw_index =  cards["draw_index"]
    score = 0

    started_suit = suits[draw_index]

    for i in range(0, len(nums)):
        if nums[i] == 11 and suits[i] == started_suit:
            score = 1

    return score


lambda_handler(params, "context")