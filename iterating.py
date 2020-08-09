#iterating for in loop
def type_items(list):
    for position,item in enumerate(list,1):   #enumerate zwraca index i wartosc danej pozycji, drugi argument zwraca uwagę od jakiej liczby ma zacząć umerować
        print("{}: {}".format(position,item))
        


        
#listy        
groceries = ['roast beef', 'cucumbers', 'lettuce', 'peanut butter', 'bread', 'dog food']



#main program
type_items(groceries)