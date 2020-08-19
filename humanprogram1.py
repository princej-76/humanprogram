import os
import pyttsx3

pyttsx3.speak("welcome to my program")
print("Welcome To My Program") 

print()

print(
"""Press 1 for Numerical Menu
Press 2 for Word Menu
Press 3 for Exit""")

print("Enter your choice: ",end=" ")

c=input()
print()

while True:
	if int (c)==1:
			print("""
Press 1 for Brave Browser
Press 2 for Notepad
Press 3 for Media Player
Press 4 for Gmail
Press 5 for Exit
				""")

			print("Enter your choice: ",end=" ")
			ch2=input()
			print()

			if int (ch2)==1:
				print("Opening Brave")
				pyttsx3.speak("Opening Brave")
				os.system("brave")

			elif int (ch2)==2:
				print("Opening Notepad")
				pyttsx3.speak("Opening Notepad")
				os.system("notepad")

			elif int (ch2)==3:
				print("Opening Media Player")
				pyttsx3.speak("Opening Media Player")
				os.system("wmplayer")

			elif int (ch2)==4:
				print("Opening GMAIL")
				pyttsx3.speak("Opening GMAIL")
				os.system("brave   https://mail.google.com/mail")

			elif int (ch2)==5:
				print("Goodbye................")
				pyttsx3.speak("Goodbye buddy, See you soon")
				break
			
			else:
				print("invalid command")
				pyttsx3.speak("invalid command")
				break	


	elif int (c)==2:
			print("Chat With Me: ", end=" ")
			p=input()

			if (("chrome" in p) or ("google" in p) or ("brave" in p) or ("browser" in p)) and (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p)):
				pyttsx3.speak("starting brave browser")
				os.system("brave")
	
			elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p)) and (("editor" in p) or ("text editor" in p) or ("notepad" in p)):
				pyttsx3.speak("starting notepad")
				os.system("notepad")

			elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p)) and (("wmplayer" in p) or ("player" in p) or ("music" in p)):
				pyttsx3.speak("starting media player")
				os.system("wmplayer")

			elif (("compose" in p) or ("send" in p) or ("write" in p) or ("get" in p)) and (("gmail" in p) or ("email" in p) or ("mail" in p)):
				pyttsx3.speak("opening gmail")
				os.system("brave   https://mail.google.com/mail")
	
			elif (("exit" in p) or ("quit" in p) or ("stop" in p)):
				print("Goodbye................")
				pyttsx3.speak("goodbye buddy, see you soon")
				break
	
			else:
				pyttsx3.speak("invalid command please try again")
				print("Invalid Command")

	elif int (c)==3:
			print("Goodbye...............")
			pyttsx3.speak("goodbye buddy, see you soon")
			exit()

	else:
			print("Invalid input",end=" ")
			pyttsx3.speak("Invalid input, please try again")
			exit()