import matplotlib.pyplot as plt

# Take speed input
speed = float(input("Enter step size (e.g., 0.5): "))

# Initial position
x, y = 5, 5

# Create figure and axis
fig, ax = plt.subplots()

# Create circle
circle = plt.Circle((x, y), 0.5, color='blue')
ax.add_patch(circle)

# Set limits and properties
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.set_title("Use Arrow Keys to Move the Circle")

# Key press event function
def on_key(event):
    global x, y

    if event.key == 'up':
        y += speed
    elif event.key == 'down':
        y -= speed
    elif event.key == 'left':
        x -= speed
    elif event.key == 'right':
        x += speed

    # Keep inside bounds
    x = max(0.5, min(x, 9.5))
    y = max(0.5, min(y, 9.5))

    # Update circle position
    circle.center = (x, y)
    fig.canvas.draw_idle()

# Connect key event
fig.canvas.mpl_connect('key_press_event', on_key)

# Show plot
plt.show()