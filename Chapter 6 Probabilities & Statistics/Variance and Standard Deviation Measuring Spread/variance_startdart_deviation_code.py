import statistics

def calculate_variance_and_std(values):
    variance = statistics.variance(values)
    std_dev = statistics.stdev(values)
    return variance, std_dev

# Example usage
data = [4.2, 5.8, 3.9, 6.1, 4.7, 5.3]
variance, std_dev = calculate_variance_and_std(data)
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")