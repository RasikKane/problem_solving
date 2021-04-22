# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(riddle):
    if riddle == "" or riddle.__contains__('?') == -1:
        return riddle
    prev= '0'
    finalOutput = ''
    for index,val in enumerate(riddle):
        nextValue = '0'
        current = val
        if current == '?':
            if index != len(riddle) - 1:
                nextIndex = index + 1
                nextValue = riddle[nextIndex]
            if prev != 'a' and nextValue != 'a':
                current ='a'
            elif prev != 'b' and nextValue != 'b':
                current = 'b'
            else:
                current = 'c'

        finalOutput+= current
        prev = current
    print(finalOutput)
    return finalOutput


solution("ab?ac?")
solution("rd?e?wg??")
solution("??????")