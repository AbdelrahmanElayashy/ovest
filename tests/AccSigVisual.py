import matplotlib.pyplot as plt
import matplotlib.animation as animation
import smbus
import AccModule

# Parameters
x_len = 300         # Number of points to display
y_range = [-2, 2]  # Range of possible Y values to display

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = list(range(0, 300))
yx = [0] * x_len
yy = [0] * x_len
yz = [0] * x_len
ax.set_ylim(y_range)

# Initialize communication with TMP102
bus = smbus.SMBus(1) 
Device_Address = 0x68   
AccModule.MPU_Init()

# Create a blank line. We will update the line in animate
linex, = ax.plot(xs, yx, label='Acceleration in x-direction')
liney, = ax.plot(xs, yy, label='Acceleration in y-direction')
linez, = ax.plot(xs, yz, label='Acceleration in z-direction')

# Add labels
plt.title('Acceleration over Time')
plt.xlabel('Time Samples')
plt.ylabel('Acceleration (g)')

# This function is called periodically from FuncAnimation
def animate(i, yx, yy, yz):

    # Read temperature (Celsius) from TMP102
    sig = AccModule.get_signals()
    
    # Add y to list
    yx.append(sig[0])
    yy.append(sig[1])
    yz.append(sig[2])

    # Limit y list to set number of items
    yx = yx[-x_len:]
    yy = yy[-x_len:]
    yz = yz[-x_len:]

    # Update line with new Y values
    linex.set_ydata(yx)
    liney.set_ydata(yy)
    linez.set_ydata(yz)

    return linex, liney, linez

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig,
    animate,
    fargs=(yx,yy,yz),
    interval=50,
    blit=True)
plt.legend(loc="upper left")
plt.grid(True)
plt.show()
