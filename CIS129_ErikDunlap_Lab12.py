#Erik Dunlap
#CIS129 22853
#Create a pet class

def main():
    '''Helps streamline the Pet class'''
    animal= Pet()
    name= input('Enter your pet\'s name:\n')
    animal.setName= name
    type= input('Enter your pet\'s type:\n')
    animal.setType= type
    age= input('Enter your pet\'s age:\n')
    animal.setAge= age
    print(f'Your pet name: {animal.getName}')
    print(f'Your pet type: {animal.getType}')
    print(f'Your pet age: {animal.getAge}')
    

class Pet:
    '''Creates a pet database'''
    
    def __init__(self, name='Not Given', type='Not Given', age='Not Given'):
        '''Initializes each attribute'''
        self.setName= name #Not empty
        self.setType= type #Not empty
        self.setAge= age #Not negative

    @property
    def getName(self):
        '''Returns the pet's name'''
        return self._name

    @getName.setter
    def setName(self, name):
        '''Sets the name'''
        removedName= list(name)
        copyName= removedName.copy()
        for character in copyName:
            if character== ' ':
                removedName.remove(' ')
        if removedName== []:
            raise ValueError('Pet name must not be empty')
        name= name.strip()
        self._name= name
        

    @property
    def getType(self):
        '''Returns the pet's type'''
        return self._type

    @getType.setter
    def setType(self, type):
        '''Sets the pet's type'''
        removedType= list(type)
        copyType= removedType.copy()
        for character in copyType:
            if character== ' ':
                removedType.remove(' ')
        if removedType== []:
            raise ValueError('Type of pet must not be empty')
        
        self._type= type

    @property
    def getAge(self):
        '''Returns the pet's age'''
        return self._age

    @getAge.setter
    def setAge(self, age):
        '''Sets the pet's age'''
        if not age== 'Not Given':
            while True:
                try:
                    age= int(age)
                except:
                    raise ValueError('Age must be input as a integer')
                if age< 0:
                    raise ValueError('Age must be positive')
                else:
                    break

        self._age= age

main()
