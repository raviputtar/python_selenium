
class TestException:

    def __init__(self):
        self.dictionary={}

    def mydict(self):
        self.dictionary['make']="honda"
        self.dictionary['model']="jazz"
        self.dictionary['year']=2018



tt=TestException()
tt.mydict()
try:
    print(tt.dictionary['color'])
except:
    print("there is no color key for car")
else:
    print("else here")
finally:
    ite=1
    for i in tt.dictionary:
        print("value="+str(ite),tt.dictionary[i])
        ite=ite+1