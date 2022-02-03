import timeit
start = timeit.timeit()
output = 10*40
end = timeit.timeit()
print(timeit.timeit('output=10*40'))
print(end-start)