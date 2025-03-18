global Animal


Animal = ['horse','lion','rabbit','mouse','bird','deer','whale','elephant','kangaroo','tiger']
    
def arrange_descending_order():
    for a in range(len(Animal)):
        for b in range(1,len(Animal)):
            if ord((Animal[b-1])[0]) < ord((Animal[b])[0]):
                temp = Animal[b-1]
                Animal[b-1] = Animal[b]
                Animal[b] = temp
    return print(f'{Animal}\n This is in Descending order.\n')

def arrange_ascending_order():
    for i in range(len(Animal)):
        for j in range(1,len(Animal)):
            if ord((Animal[j-1])[0]) > ord((Animal[j])[0]):
                temp = Animal[j-1]
                Animal[j-1] = Animal[j]
                Animal[j] = temp
    return print(f'{Animal}\n This is in Ascending order.')

arrange_descending_order()
arrange_ascending_order()