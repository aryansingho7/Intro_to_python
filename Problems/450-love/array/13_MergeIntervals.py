#merge intervals
#sort by start value 
def overlappedIntervals(Intervals):
  Intervals.sort(key = lambda i: i[0])
  output = [Intervals[0]]

  for start, end in Intervals[1:]:
    lastEnd= output[-1][1]
    if start <= lastEnd:
      output[-1][1]= max(lastEnd, end)
    else:
      output.append([start, end])
    
  return output

Intervals=[[1,4],[4,5]]
print(overlappedIntervals(Intervals))