class Time(object):
  """ This is a Time class which is used to display Time"""
  hours=0
  minutes=0
  seconds=0
  
  def add(self,second):
    self.seconds+=second
    addm=int(self.seconds/60)
    self.seconds=self.seconds%60
    self.minutes+=addm
    addh=int(self.minutes/60)
    self.minutes=self.minutes%60
    self.hours+=addh

obj=Time()
x=raw_input('Enter Increment!!')
obj.add(int(x))
print str(obj.hours)+' :'+str(obj.minutes)+' :'+str(obj.seconds)
print obj     
