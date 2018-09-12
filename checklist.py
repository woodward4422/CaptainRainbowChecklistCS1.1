print("Hello World")
checklist = list()
print(checklist)
def create(item): 
    checklist.append(item)

def read(index): return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index): checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def test():
    create("purple sox")
    create("red cloak")
    print(read(0))
    print(read(1))
    update(0, "purple socks") 
    destroy(1)
    print(read(checklist.count-1))
    list_all_items()
    select("C")
    list_all_items()
    select("R")
    list_all_items()

def mark_completed(index):
    item = read(index)
    newItem = "√" + item 
    update(index,newItem)

def select(function_code):
     if function_code == "c":
        input_item = user_input("Input item:")
        create(input_item)
    
     elif function_code == "r":
        item_index = user_input("Index Number?")
        read(item_index)

    
    elif function_code == "p":
        list_all_items()
    
    elif function_code == "q":
        return False
    
    elif function_code == "d":
        item_index = user_input("Index Number?")
        destroy(item_index)

        return False

    else:
        print("Unknown Option")
    
    return True
    
def user_input(prompt)
    running = True
    while running: 
        selection = user_input(
            "Press C to add to list, R to Read from list, P to display list, and D to delete from the list ")
        selection.lower()
        running = select(selection)

test()





    
// pop,append,count,extend, remove, reverse
// A stack is a collection of elements such as a list of objects
// dog 
// Index Out Of Bounds 
// Let names = ["Noah","Noah","Noah"]
// names.insert((names.count-1)/2,name)
// names.pop()

// 8