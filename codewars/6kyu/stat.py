# Task: Statistics for an Athletic Association

def stat(strg):
    if not strg:
        return ""
    res = []
    for r in strg.split(','):
        r_hms = list(map(int, r.split('|')))
        res.append(r_hms[0]*3600 + r_hms[1]*60 + r_hms[2])
    r_range = max(res) - min(res)
    r_average = sum(res) // len(res)
    res = sorted(res)
    r_median = (res[len(res)//2] + res[len(res)//2-1]) // 2 if len(res) % 2 == 0 else res[(len(res)-1)//2]
    def s2str(second):
        hour = second // 3600
        minute = (second % 3600 ) // 60
        seco = second - hour*3600 - minute*60
        return f'{hour:02d}|{minute:02d}|{seco:02d}'
    return f'Range: {s2str(r_range)} Average: {s2str(r_average)} Median: {s2str(r_median)}'


'''
# Best Practices

## 1
def stat(strg):

    def get_time(s):
        hh, mm, ss = [int(v) for v in s.split('|')]
        return hh * 3600 + mm * 60 + ss
    
    def format_time(time):
        hh = time // 3600
        mm = time // 60 % 60
        ss = time % 60
        return '{hh:02d}|{mm:02d}|{ss:02d}'.format(**locals())
    
    def get_range(times):
        return times[-1] - times[0]
    
    def get_average(times):
        return sum(times) // len(times)
    
    def get_median(times):
        middle = len(times) >> 1
        return (times[middle] if len(times) & 1 else
                (times[middle - 1] + times[middle]) // 2)
    
    if strg == '':
        return strg
    times = [get_time(s) for s in strg.split(', ')]
    times.sort()
    rng = format_time(get_range(times))
    avg = format_time(get_average(times))
    mdn = format_time(get_median(times))
    return 'Range: {rng} Average: {avg} Median: {mdn}'.format(**locals())
'''