# 类
class Fraction: 
    def __init__(self,top,bottom): 
        self.num = top 
        self.den = bottom 

    def __add__(self,otherfraction): # 重构类间加法函数
        newnum = self.num*otherfraction.den + self.den*otherfraction.num 
        newden = self.den * otherfraction.den 
        return Fraction(newnum,newden) 
    
    def __str__(self):  # 重构类输出形式函数
        return str(self.num)+"/"+str(self.den) 

f1=Fraction(1,4) 
f2=Fraction(1,2) 
f3 = f1 + f2
print(f3)