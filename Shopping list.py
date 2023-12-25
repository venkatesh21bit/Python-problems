shopping_list = []

def show_help():
    print('What should we pick up at the store?')
    print("""
  Enter 'DONE' to stop adding items.
  Enter 'HELP' for additional info.
  Enter 'SHOW' to see your shopping list
  Enter 'remove' to remove an item
  """)


def add_to_list(item):
    shopping_list.append(item)
    print('{} was added to your shopping list!'.format(item))
    print('You have {} items on your list.'.format(len(items)))



def show_list():
    print('My Shopping List:')
    for item in shopping_list:
        print(item)
def to_remove():
    print('Enter the item to be removed')
    shopping_list.remove(input())

show_help()

while True:
    items=list(input())


   
    if shopping_list == 'DONE':
        break
   
    elif shopping_list == 'HELP':
        show_help()
        continue
    
    elif shopping_list == 'SHOW':
        show_list()
        continue
    elif shopping_list =='remove':
        to_remove()
        continue
    

    
    add_to_list(items)

show_list()
