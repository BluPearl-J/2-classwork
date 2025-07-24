menu =  """
		1. phoneBook
               2. messages
               3. chat
               4. callRegister
               5. tones
               6. settings
               7. callDivert
               8. games
               9. calculator
               10. reminders
               11. clock
               12. profiles
               13 simservices 
	""";


phoneBookMenu =         """
                               1.search phonebook
                               2.Service NOS
                               3.Addname
                               4.Erase
                               5.Edit
                               6.Assigntone
                               7. Send birthdaycard
                               8. Options
                               9. Speeddials
                               10. Voicetags
                       """

print("PROMPTING YOU ENTER ANY NUMBER 1 TO 13")
print(menu)

nokiaNumbers = int(input("Enter your chosen nokia number: "))

match (nokiaNumbers):
    case 1:
        print("PHONEBOOK")
        print("PROMPTING YOU ENTER ANY PHONE BOOK NUMBER 1 TO 10 TO CHOOSE SERVICE")
        print(phoneBookMenu)

        phoneBookMenuNumbers = int(input("Enter phonebook number: "))

        match phoneBookMenuNumbers:
            case 1:
                print("SEARCHPHONEBOOK")
            case 2:
                print("SERVICENUMBERS of phoneBook")
            case 3:
                print("ADDNAME to phoneBook")
            case 4:
                print("ERASE your phoneBook")
            case 5:
                print("EDIT")
            case 6:
                print("ASSIGNTONES")
            case 7:
                print("SENDBIRTHDAYCARDS")
            case 8:
                print("OPTIONS")
                print("PROMPTING YOU ENTER ANY OPTIONS FROM 1 TO 2 TO CHOOSE SERVICE")
                print(optionsMenu)

                options = int(input("Enter your chosen options number: "))

                match (options):
                    case 1:
                        print("typeOfView")
                    case 2:
                        print("memoryStatus")
            case 9:
                print("SPEEDDIALS")
            case 10:
                print("VOICETAGS")

    case 2:
        print("MESSAGES")
        print("PROMPTING YOU ENTER ANY MESSAGES FROM 1 TO 10 TO CHOOSE SERVICE")
        messageMenu =         """
                                
                               MESSAGES
                               1.write messages
                               2.Inbox
                               3.Outbox
                               4.Picture messages
                               5.Templates
                               6.Smileys
                               7. Message settings
                               8. Info Service
                               9. Voice mailbox number
                               10. Service command editor
                       """
        print(messageMenu)

        message = int(input("Enter your chosen message menu number: "))

        match (message):
            case 1:
                print("Write messages")
            case 2:
                print("Inbox")
            case 3:
                print("Outbox")
            case 4:
                print("Picture messages")
            case 5:
                print("Templates")
            case 6:
                print("Smileys")
            case 7:
                print("Message settings")

                print("PROMPTING YOU ENTER ANY MESSAGE SETTINGS FROM 1 TO 2 TO SELECT SERVICE")
                messageMenu =         """
                                
                               MESSAGE SETTINGS
                               1.SET 1
                               2.COMMON
                       """
                print(messageMenu)
                messageSettings = int(input("Enter your chosen message settings number: "))

                match (messageSettings):
                    case 1:
                        print("SET 1")

                        print("PROMPTING YOU ENTER ANY NUMBER 1 TO 3 TO SELECT SET")
                        setMenu =         """
                                
                               SET 
                               1.MESSAGE CENTRE NUMBER
                               2.MESSAGE SENT AS
                               3.MESSAGE VALIDITY
                       """
                        print(setMenu)
                        set = int(input("Enter your chosen Set number: "))

                        match (set):
                                case 1:
                                   print("message centre number")
                                case 2:
                                   print("message sent as")
                                case 3:
                                   print ("MESSAGE VALIDITY")
                    case 2:
                        print("COMMON")

                        print("PROMPTING YOU ENTER ANY NUMBER 1 TO 3 TO SELECT COMMON")
                        commonMenu =         """
                                
                               2-COMMON 
                               1.DELIVERY REPORTS
                               2.REPLY VIA SAME CENTRE
                               3.CHARACTER SUPPORT
                       """
                        print(commonMenu)
                        common = int(input("Enter your chosen Set number: "))

                        match (common):
                                case 1:
                                   print("Delivery reports")
                                case 2:
                                   print("Reply via same centre")
                                case 3:
                                   print ("Character Support")

                
                

            case 8:
                print("Info service")
            case 9:
                print("Voice mailbox number")
            case 10:
                print("Service command editor")

    case 3:
        print("CHAT")
    case 4:
        print("CALL REGISTER")
        print("PROMPTING YOU SELECT FROM 1 TO 8 TO CHOOSE SERVICE OF CALL REGISTER")
        callRegisterMenu =         """
                                
                               CALL REGISTER
                               1.Missed Calls
                               2.Received Calls
                               3.Dialled Numbers
                               4.Erase recent call lists
                               5.Show Call duration
                               6.Show Call Costs
                               7.Call Cost Settings
                               8. Prepaid Credit
                               
                       """
        print(callRegisterMenu)

        callRegister = int(input("Enter your chosen call Register menu number: "))

        match (callRegister):
            case 1:
                print("MISSEDCALLS")
            case 2:
                print("RECEIVED CALLS")
            case 3:
                print("DIALLED NUMBERS")
            case 4:
                print("ERASE RECENT CALL LISTS")
            case 5:
                print("Show Call duration")

           
                print("PROMPTING YOU ENTER ANY CALL DURATION OPTIONS FROM 1 TO 5 TO CHOOSE SERVICE")
                
                callDurationMenu =         """
                                
                               SHOW CALL DURATION
                               1.Last Call duration
                               2.All calls duration
                               3.Received call duration
                               4.Dialled calls duration
                               5.clear timers
                               
                               
                     """

                print(callDurationMenu)

                callDuration = int(input("select number to show call duration : "))

                match (callDuration):
                    case 1:
                        print("LAST CALL DURATION")
                    case 2:
                        print("ALL CALL DURATION")             
                    case 3:
                        print("RECEIVED CALL DURATION")
                    case 4:
                        print("DIALLED CALL DURATION")
                    case 5:
                        print("CLEAR TIMERS")






            case 6:
                print("Show Call costs")
                print("PROMPT ENTER ANY call cost OPTIONS FROM 1 TO 3 TO CHOOSE SERVICE")
                
                callCostMenu =         """
                                
                               SHOW CALL aCOSTS
                               1.Last Call COST
                               2.All calls cost
                               3.Clear Counters
                               
                               
                               
                     """

                print(callCostMenu)

                callCost = int(input("select number to show call duration : "))

                match (callCost):
                    case 1:
                        print("LAST CALL COST")
                    case 2:
                        print("ALL CALL COST")             
                    case 3:
                        print("CLEAR COUNTERS")
                   









            case 7:
                print("Call COST SETTINGS")




                print("PROMPT ENTER ANY call cost OPTIONS FROM 1 TO 2 TO CHOOSE SERVICE")
                
                callMenu =         """
                                
                               CALL COST SETTINGS
                               1.Call COST LIMIT
                               2.SHOW COSTS IN
                               
                                       
                     """

                print(callMenu)

                call = int(input("select number to show call duration : "))

                match (call):
                    case 1:
                        print("CALL COST LIMIT")
                    case 2:
                        print("SHOW COST IN")             
                   
                   
            case 8:
                print("Prepaid Credit")






    case 5:
   
        

        print("PROMPTING YOU SELECT FROM 1 TO 9 TO CHOOSE SERVICE OF CALL REGISTER")
        tonesMenu =         """
                                
                               TONES
                               1.RINGING TONE
                               2.RINGING VOLUME
                               3.INCOMING CALL ALERT
                               4.COMPOSER
                               5.MESSAGE ALERT TONE
                               6.KEYPAD TONES
                               7.WARNING AND GAME TONES
                               8. VIBRATING ALERT
                               9. SCREENSAVER
                               
                       """
        print(tonesMenu)

        tones = int(input("Enter your chosen TONES menu number: "))

        match (tones):
            case 1:
                print("RINGINGTONES")
            case 2:
                print("RINGING VOLUME")
            case 3:
                print("INCOMING CALL ALERT")
            case 4:
                print("COMPOSER")
            case 5:
                print("MESSAGE ALERT TONE")
            case 6:
                print("KEYPAD TONE")
            case 7:
                print("WARNING TONE")
            case 8:
                print("VIBRATING ALERT")
            case 9:
                print("SCREENSAVER")

           
















    case 6:
        print("SETTINGS")





       
        print("SELECT FROM 1 TO 4 TO CHOOSE SERVICE ")
        settingsMenu =         """
                                
                               SETTINGS
                               1.CALL SETTINGS
                               2.PHONE SETTINGS
                               3.SECURITY SETTINGS
                               4.RESTORE FACTORY SETTTINGS
                               
                                      
                       """
        print(settingsMenu)

        settings = int(input("Enter your chosen CLOCK menu number: "))

        match (settings):
            case 1:
                print("CALL SETTINGS")
                print("PROMPTING YOU ENTER ANY  SETTINGS FROM 1 TO 6 TO SELECT SERVICE")
                callMenu =         """
                                
                               CALL SETTINGS
                               1.Automatic Redial
                               2.Speed dialing
                               3.Call waiting  options
                               4. Own number sending
                               5.Phone line in use
                               6. Automatic answer
                       """
                print(callMenu)
                callSettings = int(input("Enter your chosen message settings number: "))

                match (callSettings):
                    case 1:
                        print("AUTOMATIC REDIAL")
                    case 2:
                        print("SPEED DIALING")
                    case 3  :
                        print("CALL WAITING OPTIONS")
                    case 4:
                        print("OWN NUMBER SENDING")

                    case 5:
                        print("PHONE LINE IN USE")
                    case 6:
                        print("AUTOMATIC ANSWER")


            case 2:
                print("PHONE SETTINGS")


                print("PROMPTING YOU ENTER ANY  SETTINGS FROM 1 TO 6 TO SELECT SERVICE")
                phoneMenu =         """
                                
                               PHONE SETTINGS
                               1.Language
                               2.Cell Info Display
                               3.Welcome note
                               4.Network Selection
                               5.LIGHTS
                               6. Confirm SIM service actions
                       """
                print(phoneMenu)
                phoneSettings = int(input("Enter your chosen message settings number: "))

                match (phoneSettings):
                    case 1:
                        print("LANGUAGE")
                    case 2:
                        print("CELL INFO DISPLAY")
                    case 3  :
                        print("WELCOME NOTE")
                    case 4:
                        print("NETWORK SELECTION")

                    case 5:
                        print("LIGHTS")
                    case 6:
                        print("COFITRM SIM service actions")








            case 3:
                print("SECURITY SETTINGS")


                print("PROMPTING YOU ENTER ANY  SETTINGS FROM 1 TO 6 TO SELECT SERVICE")
                securityMenu =         """
                                
                               SECURITY SETTINGS
                               1.PIN CODE REQUEST
                               2.CALL BARRING SERVICE
                               3.FIXED DIALLING
                               4.CLOSED USER GROUP
                               5.PHONE SECURITY
                               6.CHANGE ACCESS CODES
                       """
                print(securityMenu)
                securitySettings = int(input("Enter your chosen message settings number: "))

                match (securitySettings):
                    case 1:
                        print("PIN CODE REQUEST")
                    case 2:
                        print("CALL BARRING SERVICE")
                    case 3  :
                        print("FIXED DIALLING")
                    case 4:
                        print("CLOSED USER GROUP")

                    case 5:
                        print("PHONE SECURITY")
                    case 6:
                        print("CHANGE ACCESS CODES")





            case 4:
                print("RESTORE FACTORY SETTINGS")
           
    case 7:
        print("CALL DIVERT")
    case 8:
        print("GAMES")
    case 9:
        print("CALCULATOR")
    case 10:
        print("REMINDERS")
    case 11:
       
        print("PROMPTING YOU SELECT FROM 1 TO 6 TO CHOOSE SERVICE OF CLOCK REGISTER")
        clockMenu =         """
                                
                               CLOCK
                               1.ALARM CLOCK
                               2.CLOCK SETTINGS
                               3.DATE SETTINGS
                               4.STOPWATCH
                               5.COUNTDOWNTIMER
                               6.AUTO UPDATE 
                                      
                       """
        print(clockMenu)

        clock = int(input("Enter your chosen CLOCK menu number: "))

        match (clock):
            case 1:
                print("ALARM CLOCK")
            case 2:
                print("CLOCK SETTINGS")
            case 3:
                print("DATE SETTINGS")
            case 4:
                print("STOPWATCH")
            case 5:
                print("COUNTDOWN TIMER")
            case 6:
                print("AUTO UPDATE TIME DATE")
    case 12:
        print("PROFILES")
    case 13:
        print("SIMSERVICES")


                   




                   




                   






            

