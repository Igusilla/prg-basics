results = [37,51,44,23,78,92,39,84,83,51]

def min_pts(limit):
      return lambda pts: pts>=limit
for i in [70,40,30]:
    grades_higher = list(filter(min_pts(i), results))
    print(f'Min {i} points: {grades_higher}')