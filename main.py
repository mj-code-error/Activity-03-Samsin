from pickle import TRUE
import Class_stat as stat
import Class_ev as ev


def ContinueOrExit():
    opt = int(input("1 to Continue or 2 to Exit: "))
    if opt == 1: main()
    elif opt == 2: exit()
    else: print("Invalid Input!")


def main():
   counter = False
   base = int(input("Enter Base values: "))
   while counter == False:
       iv = int(input("Enter Individual values: "))
       if iv >= 0 and iv <= 31:
           counter=True
       else:
           print("Invalid Input!")

   counter=False

   while counter == False:
       ev1 = int(input("Enter Effort Values: "))
       if ev1 >=0 and ev1 <= 255:
           counter= True
       else: 
           print("Invalid Input!")

   counter=False
    
   level = int(input("Enter Level Values: ")) 
   nat_num = int(input("1 for Beneficial or 2 for Hindering: "))
   
   if nat_num == 1: 
       nature = 1.1
   else: 0.9

   opt = int(input("1 for Stat or 2 for Ev: "))

   if opt == 1:
       HP = stat.Class_stat.returnHPvalue(base,iv,ev1,level)
       other_stat = stat.Class_stat.returnOtherStatValue(base,iv,ev1,level,nature)
       print("HP:  ",HP)
       print("Other Stats: ", other_stat)
       ContinueOrExit()

   elif opt == 2:
       stat1 = int(input("Enter Stats: "))
       des = ev.Class_ev.returnDvalue(stat1,level,base,iv,ev1)
       evs = ev.Class_ev.returnEvsValue(stat1,level,des)
       print("Desired increase in Stat: ", des)
       print("Effort value Stats: ", evs)
       ContinueOrExit()

   else:
        print("Invalid Input!")


main()