candidates = [1, 2, 3, 4, 5]

bitmaps = []
def bitops(idx, states): 
    if idx == 5: 
        print(states)
        # bitmaps += [states]
    else: 
        bitops(idx + 1, states)
        states[idx] = 1 
        bitops(idx + 1, states)
        states[idx] = 0
        
def is_overlapped(a, b): 
    return any([x and y for x, y in zip(a, b)])
        
def state_comb(states_lst, stack):
    for s in states_lst: 
        if len(stack) == 0 or (len(stack) > 0 and not any([is_overlapped(s, x)  for x in stack])): 
            stack += [s]
            print(stack)
            state_comb(states_lst, stack)
            stack.pop(-1)

        
bitops(0, [0, 0, 0, 0, 0])
# print(bitmaps)

state_comb(states_lst, [])