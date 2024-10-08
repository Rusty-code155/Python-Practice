import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
x = np.arange(0, 10)
y = np.random.rand(10)

fig, ax = plt.subplots()
sc = ax.scatter(x, y)

annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                     bbox=dict(boxstyle="round", fc="w"),
                     arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):
    ind = ind["ind"][0]
    pos = sc.get_offsets()[ind]
    annot.xy = pos
    text = f"x: {x[ind]}, y: {y[ind]:.2f}"
    annot.set_text(text)
    annot.get_bbox_patch().set_alpha(0.4)

def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = sc.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)

plt.show()