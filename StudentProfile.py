from Profile import *
class studentprofile(Profile):
    def __init__(self,f_name,l_name,age,phone,address,cgpa,attendance,total_marks,monthly_fee,yearly_fee):
        super().__init__(f_name,l_name,age,phone,address)
        self._cgpa = cgpa
        self._attendance = attendance
        self._total_marks = total_marks
        self._monthly_fee = monthly_fee
        self._yearly_fee = yearly_fee
    
    @property
    def cgpa(self):
        return self._cgpa
    
    @cgpa.setter
    def cgpa(self, new_gpa):
        self._cgpa = new_gpa
    
    @property
    def attendance(self):
        return self._attendance
    
    @attendance.setter
    def attendance(self, new_atn):
        self._attendance = new_atn
    
    @property
    def total_marks(self):
        return self._total_marks

    @total_marks.setter
    def total_marks(self, marks):
        self._total_marks = marks
    
    def cpga_info(self):
        p1 = Profile(self.f_name,self.l_name,self.age,self.phone,self.address)
        return f"CGPA of {p1.full_name()} is {self._cgpa}"
    
    def other_info(self):
        p1 = Profile(self.f_name,self.l_name,self.age,self.phone,self.address)
        return f"Others are {self._attendance} {self._total_marks} and his total info is: {p1.complete_proinfo()}"