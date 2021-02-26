cordinates = [float(i) for i in input("Enter cordinates :").split()]
a_segment = cordinates[0:4]
b_segment = cordinates[2:6]


# perimeter = 2 * (a_segment + b_segment)
# cordinates = (x1, y1, x2, y2, x3, y3, x4, y4)

def segment_length(lst):
    # lst = [x1, y1, x2, y2]
    # length = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    x = (lst[2] - lst[0])**2
    y = (lst[3] - lst[1])**2
    length = (x + y)**0.5
    return length



print((segment_length(a_segment) + segment_length(b_segment)) * 2)
