# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(G):
    # write your code in Python 3.6

    input_val = G.lower()
    total_rock = 0
    total_paper = 0
    total_scissor = 0

    # Rock case
    for alphabet in input_val:
        if "r" == alphabet:
            total_rock += 1
        elif "s" == alphabet:
            total_rock += 2

    # Paper case
    for alphabet in input_val:
        if "p" == alphabet:
            total_paper += 1
        elif "r" == alphabet:
            total_paper += 2

    # Scissor case
    for alphabet in input_val:
        if "s" == alphabet:
            total_scissor += 1
        elif "p" == alphabet:
            total_scissor += 2

    if total_rock > total_paper > total_scissor:
        return total_rock
    elif total_rock == total_paper or total_rock == total_scissor:
        return total_rock

    if total_paper > total_rock and total_paper > total_scissor:
        return total_paper
    elif total_paper == total_rock or total_paper == total_scissor:
        return total_paper

    if total_scissor > total_rock and total_scissor > total_paper:
        return total_scissor
    elif total_scissor == total_rock or total_scissor == total_paper:
        return total_scissor


solution('RPSRSPRS')
