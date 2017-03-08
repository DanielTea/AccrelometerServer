from collections import deque
from mpld3.plugins import PluginBase
import jinja2
import json

class RealtimePlot(PluginBase):
    """A simple plugin showing how multiple axes can be linked"""

    def __init__(self, axes, max_entries=50):

        self.axis_x = deque(maxlen=max_entries)
        self.axis_y = deque(maxlen=max_entries)
        self.axes = axes
        self.max_entries = max_entries

        self.lineplot, = axes.plot([], [], "ro-")
        self.axes.set_autoscaley_on(True)

    def add(self, x, y):
        self.axis_x.append(x)
        self.axis_y.append(y)
        self.lineplot.set_data(self.axis_x, self.axis_y)
        self.axes.set_xlim(self.axis_x[0], self.axis_x[-1] + 1e-15)
        self.axes.relim();
        self.axes.autoscale_view()  # rescale the y-axis


"""def animate(self, figure, callback, interval=200):
        import matplotlib.animation as animation
        def wrapper(frame_index):
            self.add(*callback(frame_index))
            self.axes.relim();
            self.axes.autoscale_view()  # rescale the y-axis
            return self.lineplot

        animation.FuncAnimation(figure, wrapper, interval=interval)"""