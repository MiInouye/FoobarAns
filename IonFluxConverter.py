def converter_checker(top, converter):
    prev_node = -1
    curr_node = top
    node_ct = top #number of nodes for the subtree
    # print("first  node_ct: " +str(node_ct) + " converter " + str(converter) + " curr_node " + str(curr_node))
    if curr_node == converter:
        # print(" curr_node == converter  converter " + str(converter) + " curr_node " + str(curr_node))
        return prev_node
    prev_node = curr_node
    while node_ct > 1:
        # print("node_ct: " +str(node_ct) + " converter " + str(converter) + " curr_node " + str(curr_node))
        node_ct = node_ct >> 1
        l = curr_node - node_ct - 1
        # print("l: " +str(l))
        r = curr_node - 1
        # print("r: " +str(r))
        if converter == l or converter == r:
            # print("if converter == l or converter == r  prev node :" + str(prev_node))
            return prev_node
        if converter < l:
            curr_node = l
        elif converter > l:
            curr_node = r
        prev_node = curr_node
    return -1

def solution(h, q):
    # 
    if h == 1:
        #print("h = 1")
        return [-1] * len(q)
    maxNode = 2 ** h - 1
    
    return [converter_checker(maxNode, converter) for converter in q]

def main():
    print("ans :" + str(solution(5, [19, 14, 28])))
    print("correct : 21,15,29")
    print("ans :" + str(solution(3, [7, 3, 5, 1])))
    print("correct : -1,7,6,3")
if __name__ == "__main__":
    main()