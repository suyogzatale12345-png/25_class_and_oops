class Animal:


    name_of_animal  = 'start'
    animal_sound = 'start'

    def __init__(self,nameOfAnimal,AnimalSound):
        
        
        self.name_of_animal = nameOfAnimal
        self.sound = AnimalSound
      
        print('inside classs animal_name =', self.name_of_animal)
        print('inside classs animal_sound =', self.animal_sound)
      


an1 = Animal('Dogs','bark')


print('outside of class animal sound ', an1.animal_sound)
print('outside of class name_of_animal ',an1.name_of_animal)
print('')
print('')
print('')
print('')
print('')
an2 = Animal('cat','meow')
