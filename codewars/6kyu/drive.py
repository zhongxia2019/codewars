# Task: Am I safe to drive?

def drive(drinks, finished, drive_time):
    fin, driv = list(map(lambda str_t: [int(t) for t in str_t.split(':')], [finished, drive_time]))
    delta = driv[0] - fin[0] + (driv[1] - fin[1])/60 + 24 * (driv<=fin)
    drive_units = sum(strength * volume for strength, volume in drinks) / 1000
    return [round(drive_units, 2), delta>drive_units]


'''
# Best Practices

## 1
def drive(drinks, finished, drive_time):
    f, d = (list(map(int, x.split(':'))) for x in [finished, drive_time])
    delta = d[0] - f[0] + (d[1] - f[1]) / 60 + (24 * (f >= d))
    units = sum(strength * volume for strength, volume in drinks) / 1000
    return [round(units, 2), delta > units]

## 2
def drive(alc, fn ,dr):
	to_min = lambda x: int(x.split(":")[0]) * 60 + int(x.split(":")[1])
	units = round(sum(a * b / 1000 for a, b in alc), 2)
	period = to_min(dr) - to_min(fn) + 24 * 60 * (to_min(fn) >= to_min(dr))
	return [units, period > units * 60]
'''