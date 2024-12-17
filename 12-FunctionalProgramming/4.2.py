speeds = [48,47,54,50,42,68,39,46]
too_fast = list(filter(lambda x:x>50, speeds))
print('Speeding speeds: ',too_fast)