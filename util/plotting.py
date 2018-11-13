import numpy as np
import matplotlib.pyplot as plt

def plot_annot_count_bar(x_val, y_val, 
                         x_ticks=None, title='', xlabel='', ylabel='', 
                         figsize=(9,6), barcolor='cornflowerblue',
                         ylog=False, ylim=None):
    plt.figure(figsize=figsize, facecolor='white')
    plt.title(title, fontsize=18)
    plt.gca().tick_params(axis = 'both', which = 'major', labelsize = 14)
    plt.xlabel(xlabel, fontsize=18)
    plt.ylabel(ylabel, fontsize=18)
    _ = plt.bar(x_ticks, y_val, log=ylog,
                 color=barcolor,
                 edgecolor='black', linewidth=1.2)
    if ylog == True:
        plt.ylim(0.6, max(y_val) * 10)
    if ylim is not None:
        plt.ylim(ylim[0], ylim[1])
    x_ticks = x_val if x_ticks is None else x_ticks
    plt.xticks(x_val, x_ticks)
    for cur_x,cur_y in zip(x_val,y_val):
        if cur_y == 0 and ylog == True:
            cur_y += 0.6
        # Don't mind this weird coordinate alloction, I'm just being anal with the centering
        plt.text(x = cur_x - 0.3 + 0.1 * (5 - len(str(round(cur_y,4)))), 
                 y = 1.1 * (cur_y) if ylog else cur_y + (max(y_val) - min(y_val)) * 0.01,
                 s = int(cur_y) if ylog else round(cur_y,4), fontsize=12)
        
def plot_annot_count_3bars_vertical(x_val, y_vals,
                          x_ticks=None, title='', xlabel='', ylabel='', legends = ['a','b','c'],
                          figsize=(9,6),ylim=None):
    """
    Plotting 3 vertically stacked bars
    """
    if len(y_vals) != 3 or len(legends) != 3:
        print('3 y values needed')
        return
    plt.figure(figsize=figsize, facecolor='white')
    plt.title(title, fontsize=18)
    plt.gca().tick_params(axis = 'both', which = 'major', labelsize = 14)
    plt.xlabel(xlabel, fontsize=18)
    plt.ylabel(ylabel, fontsize=18)
    
    # configuring the stack value
    stacks = [np.array(y_vals[0]),
              np.array(y_vals[0]) + np.array(y_vals[1]),
              np.array(y_vals[0]) + np.array(y_vals[1]) + np.array(y_vals[2])]
    b0 = plt.bar(x_ticks, y_vals[0],
                 color='cornflowerblue',
                 edgecolor='black', linewidth=1.2)
    b1 = plt.bar(x_ticks, y_vals[1],
                 color='limegreen',
                 bottom=stacks[0],
                 edgecolor='black', linewidth=1.2)
    b2 = plt.bar(x_ticks, y_vals[2],
                 color='tomato',
                 bottom=stacks[1],
                 edgecolor='black', linewidth=1.2)
    if ylim is not None:
        plt.ylim(ylim[0], ylim[1])
    x_ticks = x_val if x_ticks is None else x_ticks
    plt.xticks(x_val, x_ticks)
    plt.legend((b0[0], b1[0], b2[0]), 
               (legends[0], legends[1], legends[2]), 
               fontsize=12, ncol=4, framealpha=0, fancybox=True)
    for y_val,stack in zip(y_vals,stacks):
        for cur_x,cur_y,cur_stack in zip(x_val,y_val,stack):
            if cur_y == 0:
                continue
            # Don't mind this weird coordinate alloction, I'm just being anal with the centering
            plt.text(x = cur_x - 0.25 + 0.05 * (5 - len(str(round(cur_y,4)))), 
                     y = cur_stack + (max(stack) - min(stack)) * 0.01,
                     s = round(cur_y,4), fontsize=12)
            
def plot_annot_count_3bars_horizontal(x_val, y_vals,
                          x_ticks=None, title='', xlabel='', ylabel='', legends = ['a','b','c'],
                          figsize=(9,6), bar_width=0.3, ylim=None):
    """
    Plotting 3 horizontally stacked bars
    """
    if len(y_vals) != 3 or len(legends) != 3:
        print('3 y values needed')
        return
    plt.figure(figsize=figsize, facecolor='white')
    plt.title(title, fontsize=18)
    plt.gca().tick_params(axis = 'both', which = 'major', labelsize = 14)
    plt.xlabel(xlabel, fontsize=18)
    plt.ylabel(ylabel, fontsize=18)
    
    b0 = plt.bar(np.array(x_val) - bar_width, y_vals[0], bar_width,
                 color='cornflowerblue',
                 edgecolor='black', linewidth=1.2)
    b1 = plt.bar(np.array(x_val), y_vals[1], bar_width,
                 color='limegreen',
                 edgecolor='black', linewidth=1.2)
    b2 = plt.bar(np.array(x_val) + bar_width, y_vals[2], bar_width,
                 color='tomato',
                 edgecolor='black', linewidth=1.2)
    if ylim is not None:
        plt.ylim(ylim[0], ylim[1])
    x_ticks = x_val if x_ticks is None else x_ticks
    plt.xticks(x_val, x_ticks)
    plt.legend((b0[0], b1[0], b2[0]), 
               (legends[0], legends[1], legends[2]), 
               fontsize=12, ncol=4, framealpha=0, fancybox=True)
    x_shift = 0
    for y_val in y_vals:
        for cur_x,cur_y in zip(x_val,y_val):
            if cur_y == 0:
                continue
            # Don't mind this weird coordinate alloction, I'm just being anal with the centering
            plt.text(x = cur_x - 0.5 + 0.05 * (5 - len(str(round(cur_y,2)))) + x_shift, 
                     y = cur_y + (max(y_val) - min(y_val)) * 0.01,
                     s = round(cur_y,2), fontsize=12)
        x_shift += bar_width