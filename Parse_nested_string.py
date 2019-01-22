# input string, b{c,f,g}a 
# output list of string [bca,bfa,bga]
# b{c,f,g}a -> [bca,bfa,bga]; a{a{b,d}f}g -> [aabfg,aadfg]
# ab{c{d,e}f}g -> ab{cdf,cef}g -> [abcdfg,abcefg]
# ab{c{d,e}{f,g}}h -> ab{cdf,cdg,cef,ceg}h

def parseString(A):
    lst,_ = dfs(A + "}",0)
    print(lst)
    return lst

def dfs(A,start):
    i = start
    stack = [""]
    flag = False
    while i < len(A):
        ch = A[i]
        if ch == "{":
            lst,ix = dfs(A,i + 1)
            i = ix
            stack = [s + x for x in lst for s in stack]
        elif ch == "}":
            if stack[-1] == "":
                return stack[:-1]
            return stack
        elif ch == ",":
            flag = True
            stack.append("")
        else:
            if flag or stack[0] == "":
                stack[-1] += ch
            else:
                stack = [s + ch for s in stack]
        i += 1

a = 'ab{c{d,e}{f,g}}h'
parseString(a)

