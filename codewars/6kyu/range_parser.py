# Task: Range Parser

def range_parser(s):
    s_list = []
    for s_single in s.split(','):
        if '-' not in s_single:
            s_single = s_single + '-' + s_single
        if ':' not in s_single:
            s_single = s_single + ':' + '1'
        s_start, s_end, s_step = s_single.split('-')[0], s_single.split('-')[1].split(':')[0], s_single.split('-')[1].split(':')[1]
        s_list.append([int(s_start), int(s_end), int(s_step)])
    res = []
    for s_start, s_end, s_step in s_list:
        res += [x for x in range(s_start, s_end+1, s_step)]
    return res


'''
# Best Prantices

## 1
def range_parser(string):
    res = []
    for range_ in string.split(','):
        first_last, _, step = range_.partition(':')
        first, _, last = first_last.partition('-')
        res += range(int(first), int(last or first) + 1, int(step or 1))
    return res

## 2
import re

def range_parser(s):
    return [x for r in re.split(r', *', s)
              for start,end,step in re.findall(r'(\d+)-?(\d*):?(\d*)',r) 
              for x in range(int(start), int(end or start)+1, int(step or '1'))]

## 3
def range_parser(inp):
    res = []
    for r in inp.split(','):
        r = list(map(int, r.replace(':', '-').split('-')))
        if len(r) > 1:
            r[1] += 1
            res += range(*r)
        else:
            res.append(r[0])
    return res
'''
