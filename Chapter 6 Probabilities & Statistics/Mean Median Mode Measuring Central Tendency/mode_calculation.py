import statistics

def calculate_mode(values):
    return statistics.mode(values)

# Example usage
data = [150, 220, 120, 250, 200, 200]
result = calculate_mode(data)
print(f"Mode: {result}")