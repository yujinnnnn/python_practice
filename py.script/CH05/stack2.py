def stack_bracket(text):
    stack=[]
    for i in text:
        open_brk = '({['
        close_brk = ')}]'

        if i in open_brk:
            stack.append(i)
        elif i in close_brk:
            if open_brk.find(stack.pop()) != close_brk.find(i):
                return False

    if not stack: #stack이 비어있지 않으면 True
        return True
    else:
        return False

if __name__ =='__main__':
    exp = input("input expression >>") 
    print(stack_bracket(exp))   