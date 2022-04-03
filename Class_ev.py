class Class_ev():
   
   def returnDvalue(stat1,level,base,iv,ev1):
       return  (((2* base)+ iv + (ev1/4)) * (level/100))

   def returnEvsValue(stat1,level,des):
        return (((((stat1/level) - des) * 400) / level) / 4) * 4
