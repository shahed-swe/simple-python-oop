from Profile import *
class teacherprofile(Profile):
    def __init__(self,f_name,l_name,age,phone,address,attendance,payAbleAmount):
        super().__init__(f_name,l_name,age,phone,address)
        self._attendance = attendance
        self._payAbleAmount = payAbleAmount
    
    @property
    def attendance(self):
        return self._attendance
    
    @attendance.setter
    def attendance(self, new_atn):
        self._attendance = int(new_atn)
    
    @property
    def payAbleAmount(self):
        return self._payAbleAmount
    
    @payAbleAmount.setter
    def payAbleAmount(self,amnt):
        self._payAbleAmount = int(amnt)
    
    def teachersPaymentInfo(self):
        t1 = Profile(self.f_name,self.l_name,self.age,self.phone,self.address)
        return f"Payable amount of {t1.full_name()} is {self._attendance * self._payAbleAmount}"
    
    def other_info(self):
        t1 = Profile(self.f_name,self.l_name,self.age,self.phone,self.address)
        return f"{t1.complete_proinfo()}"