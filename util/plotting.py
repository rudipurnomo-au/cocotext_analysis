import matplotlib.pyplot as plt

def plot_annot_count_bar(x_val, y_val, x_ticks=None, title='', xlabel='', ylabel='', figsize=(9,6), ylog=False, ylim=None):
    plt.figure(figsize=figsize, facecolor='white')
    plt.title(title, fontsize=18)
    plt.gca().tick_params(axis = 'both', which = 'major', labelsize = 14)
    plt.xlabel(xlabel, fontsize=18)
    plt.ylabel(ylabel, fontsize=18)
    _ = plt.bar(x_ticks, y_val, log=ylog,
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
                 y = 1.1 * (cur_y) if ylog else cur_y + 0.005,
                 s = int(cur_y) if ylog else round(cur_y,4), fontsize=12)