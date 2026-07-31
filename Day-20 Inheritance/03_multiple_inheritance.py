# A class inherits from more than one parent class.
class Teacher:

    def teach(self):
        print("Teaching students")

class Singer:

    def sing(self):
        print("Singing songs")

class MusicTeacher(Teacher, Singer):
    pass

person = MusicTeacher()

person.teach()
person.sing()