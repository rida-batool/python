


def countDuplicatesDict(arrayin):
    checkDuplicate = {}
    for number in arrayin:

        if number not in checkDuplicate:
            checkDuplicate[number] = 1
        
        elif  (checkDuplicate[number] > 1):
            checkDuplicate[number] = checkDuplicate[number] + 1
    
        else:
            print("duplicate is", number)    
            checkDuplicate[number] = checkDuplicate[number] + 1  


countDuplicatesDict([0,1,1,12,2,2,33,4,5,5,5,6,6])          