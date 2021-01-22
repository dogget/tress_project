import numpy as np

def cornersOffset(b):
    print('работает index_corners,\n')
    shape = b.shape
    mask = np.zeros(shape)

    np.putmask(mask, b != b[0][0], 1)

    ind_lines = []
    for i in range(shape[0]):
       if np.sum(mask[i,:]) > 0:
           ind_lines.append(i)
           break
       
    for i in range(shape[0]):
       if np.sum(mask[shape[0] - i,:]) > 0:
           ind_lines.append(i)
           break

    ind_columns = []
    for j in range(shape[1]):
       if np.sum(mask[:,j]) > 0:
           ind_columns.append(j)
           break
           
    for j in range(shape[1]):
       if np.sum(mask[:, shape[1] - j]) > 0:
           ind_columns.append(j)
           break
    
    print('ind_lines',  ind_lines,"\n")
    print('ind_columns',ind_columns,"\n")

    max_line = max(ind_lines)
    min_line = min(ind_lines)
    max_col = max(ind_columns)
    min_col = min(ind_columns)
    print(max_line, min_line, max_col, min_col,"\n")

    return  (max_line, min_line, max_col, min_col)
