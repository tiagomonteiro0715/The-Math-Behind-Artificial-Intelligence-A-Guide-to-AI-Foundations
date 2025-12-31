import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def f(x):
    return np.sin(x) + 1.5

a, b = 0, np.pi
x_smooth = np.linspace(a, b, 500)
true_integral = -np.cos(np.pi) + np.cos(0) + 1.5 * np.pi

n_rectangles = [2, 4, 8, 16, 32, 64, 128, 256]

for idx, n in enumerate(n_rectangles):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot curve
    ax.plot(x_smooth, f(x_smooth), 'b-', lw=2, label='f(x) = sin(x) + 1.5')
    
    dx = (b - a) / n
    riemann_sum = 0
    
    for i in range(n):
        x_left = a + i * dx
        height = f(x_left)
        riemann_sum += height * dx
        rect = Rectangle((x_left, 0), dx, height,
                         facecolor='skyblue', edgecolor='navy',
                         alpha=0.7, linewidth=0.5)
        ax.add_patch(rect)
    
    error = abs(true_integral - riemann_sum)
    ax.set_xlim(a - 0.2, b + 0.2)
    ax.set_ylim(0, 3)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title(f'n = {n} rectangles  |  Approx: {riemann_sum:.4f}  |  Error: {error:.4f}')
    ax.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig(f'riemann_{idx+1}_{n}_rectangles.png', dpi=150)
    plt.close()
    print(f"Saved: riemann_{idx+1}_{n}_rectangles.png")

print("\nDone! 8 images saved.")