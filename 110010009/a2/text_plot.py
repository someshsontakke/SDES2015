import math
import sys
a = math.sin(math.pi/4)
#print a
window_rows = 30
window_columns = 80
    
def plot(x,y):
    l_x = len(x)
    l_y = len(y)
    y_max, y_min = max(y), min(y)
    x_max, x_min = max(x), min(x)
    delta_x = (x_max-x_min)/window_columns
    delta_y = (y_max-y_min)/window_rows
    x_co_ordinates = []
    y_co_ordinates = []
    for i in range(0,l_x):
        x_co_ordinates.append(int((x[i]-x_min)/delta_x))
        y_co_ordinates.append(int((y[i]-y_min)/delta_y))
    for i in range(len(x_co_ordinates)-1,-1,-1):
        for j in range(window_rows-1,-1,-1):
            if (j == y_co_ordinates[i]):
                sys.stdout.write('*')#print "*",
            else:
                sys.stdout.write(' ')#print " ",
        print " "
    #print x_co_ordinates,y_co_ordinates           

if __name__ == "__main__":
    x = []
    y = []
    for i in range(0,window_columns):
        x.append(math.sin(i*math.pi*2/window_columns))
        y.append(math.sin(i*math.pi*2/window_columns))
    #print x,y
    plot(x,y)
