class Class_stat():
   
    def returnHPvalue(base,iv,evv,level):
        return (((((2* base) + iv + (evv/4))*level))/100) +level +10

    def returnOtherStatValue(base,iv,evv,level,nature):
        return  (((((2* base) + base + iv + (evv/4))* level)/100) +5 )* nature
