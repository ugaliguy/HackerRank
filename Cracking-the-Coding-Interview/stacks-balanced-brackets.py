def is_matched(expression):
    brackets = {'(':')', '[':']' , '{':'}'}
    rights = []
    for ch in expression:
        if ch in brackets.keys():
            rights.append(brackets[ch])
        elif len(rights) > 0 and ch == rights[-1]:
            rights.pop()
        else:
            return False
    return len(rights) == 0

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"