#create Class
class Employee:

    #Initiating:
    def __init__(self):
        print('Employee created')

    #Calling destructor
    def __del__(self):
        print('Destructor called')

def Create_obj():
        print('Making Object...')
        obj=Employee()
        print('function end...')
        return obj
    
print('Calling create_obj() function...')
obj=Create_obj()
print('Program End...')