# class Animal:


#     name_of_animal = ''


#     def __init__(self,nameOfAnimal):
#         print('this is class init method')
#         print('self',self)
#         self.name_of_animal = nameOfAnimal
#         print('animal_name =', self.name_of_animal)


# an1 = Animal('dog')



class Animal:


    name_of_animal  = 'start'
    sound = 'start'

    def __init__(self,nameOfAnimal):
        name_of_animal = 'test'
        print('this is class method')
        print('self',self)
        print('animal_name =', self.name_of_animal)
        print('animal_sound =', self.sound)
        print('name_of_animal local ',name_of_animal)
        self.name_of_animal = nameOfAnimal
        self.sound = 'bark'
        name_of_animal = 'test2'
        print('animal_name =', self.name_of_animal)
        print('animal_sound =', self.sound)
        print('name_of_animal local ',name_of_animal)


an1 = Animal('Dogs')
print('-'*50)
an2 = Animal('cat')





