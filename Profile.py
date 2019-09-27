class Profile:
    def __init__(self, f_name,l_name,age,phone,address):
        self._f_name = f_name
        self._l_name = l_name
        self._phone = max(int(phone), 0)
        self._age = max(int(phone), 0)
        self._address = address

    @property
    def f_name(self):
        return self._f_name
    
    @f_name.setter
    def f_name(self, new_name):
        self._f_name = new_name
    
    @property
    def l_name(self):
        return self._l_name
    
    @l_name.setter
    def l_name(self,new_name):
        self._l_name = new_name
        
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,new_age):
        self._age = max(int(new_age), 0)

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, new_phone):
        self._phone = max(int(new_phone), 0)

    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, new_address):
        self._address = new_address


    def complete_proinfo(self):
        return f"{self._f_name} {self._l_name} {self._age} {self._address}"

    def full_name(self):
        return "{} {}".format(self._f_name,self._l_name)

    def normal_details(self):
        return "Adress: {}\nPhone: {}".format(self._address,self._phone)