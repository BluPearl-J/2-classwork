
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
    case 5:
        print("TONES")
    case 6:
        print("SETTINGS")
    case 7:
        print("CALL DIVERT")
    case 8:
        print("GAMES")
    case 9:
        print("CALCULATOR")
    case 10:
        print("REMINDERS")
    case 11:
        print("CLOCK")
    case 12:
        print("PROFILES")
    case 13:
        print("SIMSERVICES")


                   




            

