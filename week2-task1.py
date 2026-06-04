# this code contains the code to make all elements in list unique.
def unique_list(l):
    final = list(set(l))    #here we are directly coverting the list into the set and again converting it to the list.
    return final

def using_loop(l):
    s = set()
    for items in l:
        set.add(items)
    final = list(s) # We are typecasting the set into list
    return final

l = [int(x) for x in input("Enter integers separated by spaces: ").split()]
final = unique_list(l)
print(final)