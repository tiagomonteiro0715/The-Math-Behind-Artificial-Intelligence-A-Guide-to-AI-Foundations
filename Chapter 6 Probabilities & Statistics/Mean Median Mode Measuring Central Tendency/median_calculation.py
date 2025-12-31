import statistics

def calculate_median(values):
    return statistics.median(values)

# Example usage
data = [4.2, 5.8, 3.9, 6.1, 4.7, 5.3]
result = calculate_median(data)
print(f"Median: {result}")