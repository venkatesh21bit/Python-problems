
phone_directory = {}


def add_contact(name, number):
  
    if name in phone_directory:
        print(f"{name} is already in the directory.")
    else:
        
        phone_directory[name] = number
        print(f"{name} has been added to the directory.")


def search_contact(name):
  
    if name in phone_directory:
        
        print(f"{name}'s number is {phone_directory[name]}.")
    else:
      
        print(f"{name} is not in the directory.")

def delete_contact(name):
   
    if name in phone_directory:
        
        phone_directory.pop(name)
        print(f"{name} has been deleted from the directory.")
    else:
        
        print(f"{name} is not in the directory.")

n=int(input('how many numbers do you want to enter'))
for i in range(n):
    user_input=input('Enter the name and number')
    name,number=user_input.split(':')
    phone_directory[name]=number
print(phone_directory)
