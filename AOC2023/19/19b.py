file = 'test.txt'
file = 'input.txt'

index = {}
index['x'] = 0
index['m'] = 1
index['a'] = 2
index['s'] = 3

rules = {}
parts = []
with open(file) as inp:
    z = inp.read()
    z = z.strip()


for line in z.split('\n\n')[0].split('\n'):
    left,right = line.split('{')
    rules[left] = []
    right = right[:-1]
    for elem in right.split(','):
        if ':' in elem:
            l,r = elem.split(':')
            rules[left].append((l,r))
        else:
            rules[left].append(elem)


def function(state,rangesIn):
    #Base cases
    #If any ranges are completely empty, prune this branch
    for i in range(0,4):
        if len(rangesIn[i]) == 0:
            return 0
    if state == 'R':
        return 0
    if state == 'A':
        product = 1
        for arr in rangesIn:
            options = 0
            for r in arr:
                options += r[1]-r[0]+1
            product *= options
        return product

    #The scary recursive cases
    ranges = rangesIn.copy()  # I don't want to risk concurrent list modification, each function instance gets its own
    ret = 0
    stateRules = rules[state]
    #print(stateRules)
    for (rule,dest) in stateRules[:-1]:
        category = index[rule[0]]
        op = rule[1]
        number = int(rule[2:])
        keep = []
        send = []
        match op:
            case '>':
                for i in range(0,len(ranges[category])):
                    r = ranges[category][i]
                    if r[0] >= number:
                        send.append(r)
                    elif r[1] < number:
                        keep.append(r)
                    elif r[0] < number and r[1] >= number:
                        #(2000,3000) on x > 2006 should keep (2000,2006) and send (2007,3000)
                        keep.append((r[0],number))
                        send.append((number+1,r[1]))
                    else:
                        print("I'm not sure how we got here lol")
                        print(r)
                        print(number)
                        exit()
            case '<':
                for i in range(0,len(ranges[category])):
                    r = ranges[category][i]
                    if r[1] < number:
                        send.append(r)
                    elif r[0] >= number:
                        keep.append(r)
                    elif r[0] < number and r[1] >= number:
                        #(2000,3000) on x < 2006 should send (2000,2005) and send (2006,3000)
                        send.append((r[0],number-1))
                        keep.append((number,r[1]))
                    else:
                        print("I'm not sure how we got here lol but other op")
                        print(r)
                        print(number)
                        exit()
        ranges[category] = send  # temporarly set my ranges to what will be sent off
        ret += function(dest,ranges)
        ranges[category] = keep  # Now set to what will be kept for future iterations

    # only the last unconditional state is left
    dest = stateRules[-1]
    return ret + function(dest,ranges)



print(function('in',[[(1,4000)],[(1,4000)],[(1,4000)],[(1,4000)]]))