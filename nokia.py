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
                       """;



print ("PROMPTING YOU ENTER ANY NUMBER 1 TO 13");

print (menu);

nokiaNumbers = int( input ("Enter your chosen nokia number"));

match (nokiaNumbers):
                   case 1: print("PHONEBOOK");



print ("PROMPTING YOU ENTER ANY PHONE BOOK NUMBER 1 TO 10 TO CHOOSE SERVICE");


print(phoneBookMenu);



phoneBookMenuNumbers = int( input ("Enter phonebook number"));


match (phoneBookMenuNumbers):
                    case 1:
                        print("SEARCHPHONEBOOK");
                      
                    case 2:
                        print("SERVICENUMBERS of phoneBook");
                       
                    case 3:
                        print("ADDNAME to phoneBook");
                        
                    case 4:
                        print("ERASE your phoneBook");
                       
                    case 5:
                        print("EDIT ");
                       
                    case 6:
                        print("ASSIGNTONES");
                        
                    case 7:
                        print("SENDBIRTHDAYCARDS");
                        
                    case 8:
                        print("OPTIONS");

                    case _:
                       print("phoneBookError");
print ("PROMPTING YOU ENTER ANY OPTIONS FROM 1 TO 2 TO CHOOSE SERVICE");

optionsMenu =         """
                               1.Type of view
                               2.memoryStatus
                       """;

print (optionsMenu);

options = int( input ("Enter your chosen nokia number"));
                  
match (options):
  
                    case 1:
                      print("typeOfView");
                
                    case 2:
                      print("memoryStatus");
                    case _:
                       print("error");


            

