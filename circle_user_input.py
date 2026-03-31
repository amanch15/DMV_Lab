import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def get_float(prompt, default):
    val = input(prompt)
    try:
        return float(val) if val.strip() != "" else default
    except:
        return default

x = get_float("Enter initial X position (0-10): ", 5)
y = get_float("Enter initial Y position (0-10): ", 5)
speed = get_float("Enter speed: ", 0.2)
dx, dy = 0, 0

fig, ax = plt.subplots()
circle = plt.Circle((x, y), 0.5, color='blue')
ax.add_patch(circle)

ax.set_xlim(0, 15)
ax.set_ylim(0, 15)
ax.set_aspect('equal')
ax.set_xticks(range(0, 16))
ax.set_yticks(range(0, 16))
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
plt.grid(True)

def on_key(event):
    global dx, dy
    if event.key == 'up':
        dx, dy = 0, speed
    elif event.key == 'down':
        dx, dy = 0, -speed
    elif event.key == 'left':
        dx, dy = -speed, 0
    elif event.key == 'right':
        dx, dy = speed, 0

def update(frame):
    global x, y
    x += dx
    y += dy
    # Keep the circle within the plot boundaries
    x = max(0.5, min(x, 14.5))
    y = max(0.5, min(y, 14.5))
    
    circle.center = (x, y)
    return circle,

fig.canvas.mpl_connect('key_press_event', on_key)
ani = FuncAnimation(fig, update, interval=30)

plt.show()