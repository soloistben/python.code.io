class Person(object):
    def __init__(self,name,gender,**kw):
        self.name = name
        self.gender = gender
        for k,v in kw.items():
            setattr(self,k,v)

Lisa = Person('Lisa', 'Female', age=22, course='Python and C++', tall='172')
print(Lisa.name,' is ',Lisa.age)
print('Studying course is ' ,Lisa.course,'And tall',Lisa.tall)