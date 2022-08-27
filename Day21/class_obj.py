import statistics as stat

class MyStat:
    def __init__(self,ages):
        self.ages = ages

    def count(self):
        return self.ages

    def sum(self):
        result = 0
        for it in self.ages:
            result = result + it
        return result
    
    def min(self):
        return min(self.ages)

    def max(self):
        return max(self.ages)

    def range(self):
        return data.max() - data.min()

    def mean(self):
        return stat.mean(self.ages)
    
    def median(self):
        return stat.median(self.ages)
    
    def mode(self):
        return stat.mode(self.ages)

    def std(self):
        return stat.stdev(self.ages)
    
    def var(self):
        return stat.variance(self.ages)


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = MyStat(ages)


print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
