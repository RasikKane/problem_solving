"""
Minimum characters required to be removed to make frequency of each character unique
Given string str, the task is to find the minimum count of characters that need to be deleted from the string such that 
the frequency of each character of the string is unique.
"""


def charDelFrequency(inputString):

    # dictioanary to store count of occurance for each character
    dict_char_freq = {}
    dict_count_freq = {}
    # list serving as priority queue
    priority_q = []
    count_del_ch = 0

    # store character frequency
    for ch in set(inputString):
        dict_char_freq[ch] = inputString.count(ch)

    dict_char_freq = dict(sorted(dict_char_freq.items(), key=lambda item: item[1]))

    print(dict_char_freq)
    return count_del_ch


# Driver Code
if __name__ == '__main__':
    inputString = "ccaaffddecee"
    print(charDelFrequency(inputString))


# """
# Minimum characters required to be removed to make frequency of each character unique
# Given string str, the task is to find the minimum count of characters that need to be deleted from the string such that 
# the frequency of each character of the string is unique.
# """

# def charDelFrequency(inputString):

#     # dictioanry to store count of occurance for each character
#     dict_char_freq = {}

#     # list serving as priority queue 
#     priority_q = []
#     count_del_ch = 0

#     # store character frequency
#     for ch in set(inputString):
#         dict_char_freq[ch] = inputString.count(ch)

#     # store count of characters into priority queue
#     priority_q = list(dict_char_freq.values())    
#     priority_q = sorted(priority_q)

#     # Traverse the priority_queue
#     while (len(priority_q) > 0):
        
#         # element of priority_q
#         high_freq = priority_q[-1]

#         # remove most freuqent element
#         del priority_q[-1]

#         # return count if queue is empty
#         if (len(priority_q) == 0):
#             return count_del_ch

#         # If count of previous high_freq and current  high_freq element are equal
#         if (high_freq == priority_q[-1]):

#             # If high_freq > 1, decrement it and add it to list
#             if (high_freq > 1):
#                 priority_q.append(high_freq - 1)

#             count_del_ch += 1

#         priority_q = sorted(priority_q)

#     return count_del_ch


# # Driver Code
# if __name__ == '__main__':
#     inputString = "eeee"
#     print(charDelFrequency(inputString))
