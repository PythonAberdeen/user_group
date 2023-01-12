possibles = [0, 1, 2]
start_list = [2, 2, 0, 1, 1, 0, 0, 1, 0, 1]

def get_next_number(n, m):
    if n == m:
        return n
    else:
        l=[n, m]
        out=[x for x in possibles if x not in l]
        return out[0]

def next_line(previous_line):
    l=[]
    for i in range(0, len(previous_line)-1):
        l.append(get_next_number(previous_line[i], previous_line[i+1]))
    return l

def generate_triangle(current_list):
    list_of_lists = []
    list_of_lists.append(current_list)
    while len(current_list)>1:
        current_list=next_line(current_list)
        list_of_lists.append(current_list)
    return list_of_lists

def get_last_number(current_list):
    while len(current_list)>1:
        current_list=next_line(current_list)
    return current_list[0]

def print_triangle(full_triangle):
    i=0
    for l in full_triangle:
        leading_whitespace=" " * i
        formatted_line=" ".join(str(x) for x in l)
        output_string=leading_whitespace+formatted_line
        print(output_string)
        i=i+1

def main():
    full_triangle = generate_triangle(start_list)
    #print(full_triangle)
    print_triangle(full_triangle)
    #print(get_last_number(start_list))

if __name__ == '__main__':
    main()