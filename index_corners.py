import numpy as np

def index_corners(b):
    shape = b.shape
    mask = np.zeros(shape)

    np.putmask(mask,b!=b[0][0],1)

    ind_lines = []
    for i in range(shape[0]):
       if np.sum(mask[i,:])<=5 and np.sum(mask[i,:])!=0:
           ind_lines.append(i)

    ind_columns = []
    for j in range(shape[1]):
       if np.sum(mask[:,j])<=5 and np.sum(mask[:,j])!=0:
           ind_columns.append(j)

    Max_ind_line = max(ind_lines)
    Min_ind_line = min(ind_lines)
    Max_ind_col = max(ind_columns)
    Min_ind_col = min(ind_columns)
    print(Max_ind_line, Min_ind_line, Max_ind_col, Min_ind_col,"\n")


    return  (Max_ind_line, Min_ind_line, Max_ind_col, Min_ind_col)
