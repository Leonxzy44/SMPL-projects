import turtle

import time 

import winsound





screen = turtle.Screen()
screen.title("Reminder")
screen.bgcolor("#3B3B3B") 

time.sleep(0.5)

print("Welcome to the Retify! This is app for memory storing and taking notes. ")


time.sleep(2.5)

print("Let's start! ")

time.sleep(0.5)

#-------------------------------------------------

first_note = input("Enter your first reminder here: ")
    

time.sleep(0.5)

timeenter = int(input("In what time you want to be reminded? (Options are: 5 minutes, 10 minutes, 15 minutes, 20 minutes, 30 minutes, 60 minutes (Enter a number of minutes!) |:  "))


if timeenter == 5 :

 time.sleep(5 * 60)
 
 for i in range(5): 
  
  print(str(first_note))

  import winsound
import time

for _ in range(2):
    winsound.Beep(1000, 500)
    time.sleep(0.1)  

#-------------------------------------------------

else: 

  if timeenter == 10: 

    time.sleep(10 * 60)

    for i in range(5): 

      print(str(first_note))

      import winsound

    import time 

    for _ in range(2): 
      
      winsound.Beep(1000, 500)
      time.sleep(0.1)

#-------------------------------------------------
    else: 

      if timeenter == 15: 

        time.sleep(15*60)

        for i in range(5): 

          print(str(first_note))

          import winsound

          import time 

          for _ in range(2): 

            winsound.Beep(1000, 500)
            time.sleep(0.1)

#-------------------------------------------------
          else: 

            if timeenter == 20: 

              time.sleep(20*60)

              for i in range(5): 

                print(str(first_note))

                import winsound

                import time 

                for _ in range(2): 

                  winsound.Beep(1000, 500)
                  time.sleep(0.1)
#-------------------------------------------------
                else :

                  if timeenter == 30: 

                    time.sleep(30 * 60)

                    for i in range(5): 

                      print(str(first_note))

                      import winsound

                      import time 

                      for _ in range(2): 

                        winsound.Beep(1000, 500)

                        time.sleep(0.1)


                      else :

                        if timeenter == 60: 

                          time.sleep(60*60)

                          for i in range(5): 

                            print(str(first_note))

                            import winsound

                            import time 

                            for _ in range (2): 

                              winsound.Beep(1000, 500)

                              time.sleep(0.1)

                        

                        else: 

                         print("You entered wrong time, pelase try again! ")
 
                      time.sleep(1.5)

                      recension = int(input("Now, after you tried Reminder, write something about it ------>"))

                      time.sleep(0.5)

                      print("Thank you, see you later! ")

                      

                      

                   



                        








        



           


            
        

















 
