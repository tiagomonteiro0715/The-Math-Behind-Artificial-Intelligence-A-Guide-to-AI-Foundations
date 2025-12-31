import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42)
X = np.linspace(0, 10, 50)
y_true = 3 * X + 2
noise = np.random.normal(0, 2, 50)
y = y_true + noise

w = 0.1 
b = 0.5
learning_rate = 0.01
iterations = [0, 1, 2, 3, 4, 5]
saved_states = []



# Create figure with 3 subplots
y_pred_first = w * X + b
fig, axes = plt.subplots(1, 3, figsize=(15, 4))



# Plot 1: True line only
axes[0].plot(X, y_true, 'g--', linewidth=2, label='True line (y = 3x + 2)', alpha=0.7)
axes[0].set_xlabel('X', fontsize=12)
axes[0].set_ylabel('y', fontsize=12)
axes[0].grid(True, alpha=0.3)
axes[0].set_ylim(-5, 35)
axes[0].set_xlim(-0.5, 10.5)

# Plot 2: True line and data points
axes[1].plot(X, y_true, 'g--', linewidth=2, label='True line (y = 3x + 2)', alpha=0.7)
axes[1].scatter(X, y, color='blue', alpha=0.6, s=50, label='Data points')
axes[1].set_xlabel('X', fontsize=12)
axes[1].set_ylabel('y', fontsize=12)
axes[1].grid(True, alpha=0.3)
axes[1].set_ylim(-5, 35)
axes[1].set_xlim(-0.5, 10.5)

# Plot 3: Both lines and data points
axes[2].scatter(X, y, color='blue', alpha=0.6, s=50, label='Data points')
axes[2].plot(X, y_pred_first, 'r-', linewidth=3, label=f'Fitted line (y = {w}x + {b})')
axes[2].plot(X, y_true, 'g--', linewidth=2, label='True line (y = 3x + 2)', alpha=0.7)
axes[2].set_xlabel('X', fontsize=12)
axes[2].set_ylabel('y', fontsize=12)
axes[2].grid(True, alpha=0.3)
axes[2].set_ylim(-5, 35)
axes[2].set_xlim(-0.5, 10.5)

plt.tight_layout()
plt.show()

plt.tight_layout()
plt.show()

for epoch in range(max(iterations) + 1):
    y_pred = w * X + b
    error = np.mean((y - y_pred) ** 2)
    
    if epoch in iterations:
        saved_states.append({
            'epoch': epoch,
            'w': w,
            'b': b,
            'y_pred': y_pred.copy(),
            'error': error
        })
    
    dw = -2 * np.mean(X * (y - y_pred))
    db = -2 * np.mean(y - y_pred)
    
    w = w - learning_rate * dw
    b = b - learning_rate * db




"""
import matplotlib.pyplot as plt

# Create and save 5 separate images
for i, state in enumerate(saved_states):
    plt.figure(figsize=(8, 6))
    
    # Plot data points
    plt.scatter(X, y, alpha=0.6, s=50, label='Data points', color='blue')
    
    # Plot fitted line
    plt.plot(X, state['y_pred'], 'r-', linewidth=3, label='Fitted line')
    
    # Plot true line
    plt.plot(X, y_true, 'g--', linewidth=2, label='True line (y=3x+2)', alpha=0.7)
    
    plt.title(f'Linear Regression - Iteration {state["epoch"]}\n' + 
              f'Parameters: w={state["w"]:.3f}, b={state["b"]:.3f} | Error={state["error"]:.2f}',
              fontsize=14, fontweight='bold')
    plt.xlabel('X', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.ylim(-5, 35)
    plt.xlim(-0.5, 10.5)
    
    # Save the figure
    filename = f'linear_regression_iteration_{state["epoch"]:04d}.png'
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    print(f"Saved: {filename}")
    plt.close()

print(f"\n All 5 images saved successfully!")
print(f"\nFinal parameters:")
print(f"Slope (w): {saved_states[-1]['w']:.3f} (true value: 3.0)")
print(f"Intercept (b): {saved_states[-1]['b']:.3f} (true value: 2.0)")
"""