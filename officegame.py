print "hello, pick a charchter from the list below and I will guess which one it is."

def menu():
    print ("which game do you want to play?\n")
    menu = int(raw_input("1.)Office\n2.)Family\n3.)Wine"))

    if menu == 1:
        officegame()

    if menu == 2:
        familygame()

    if menu == 3:
    	winegame()

    if menu > 3:
       print ("input not accepted")

def officegame():
	print "great, pick a charchter from the list -pam, jim, dwight, kevin, oscar, angela, or michael, or... creed- and I will guess which one it is."
	print ("is your charachter a manager")
	menu2 = int(raw_input("1.)yes\n2.)no\n"))
	if menu2 == 1:
		print ("michael")
	if menu2 == 2:
		print ("is your charachter a creep")
		menu3 = int(raw_input("1.)yes\n2.)no\n"))
		if menu3 == 1:
			print ("creed")
		if menu3 == 2:
			print ("is your charachter a accountant")
			menu4 = int(raw_input("1.)yes\n2.)no\n"))
			if menu4 == 1:
				print ("is your charachter a boy")
				menu5 = int(raw_input("1.)yes\n2.)no\n"))
				if menu5 == 1:
					print ("is your charachter fat")
					menu6 = int(raw_input("1.)yes\n2.)no\n"))
					if menu6 == 1:
						print ("kevin")
					if menu6 == 2:
						print ("oscar")
				if menu5 == 2:
					print ("angela")
			if menu4 == 2:
				print ("your charachter is a salesperson -- is it a boy")
				menu7 = int(raw_input("1.)yes\n2.)no\n"))
				if menu7 == 1:
					print ("does your person wear glasses")
					menu8 = int(raw_input("1.)yes\n2.)no\n"))
					if menu8 == 1:
						print ("dwight")
					if menu8 == 2:
						print ("Jim")
				if menu7 == 2:
					print ("pam")
	else:
		helpGame()
		listOfCharachterss = [peter, mario, dinatale]

def familygame():
	print(bool("Hello"))
	print(3**2)
	fruits = ["apples", "bananas", "pears"]
	for x in fruits:
		print (x)

def winegame():
    print ("ok, lets see what you've gotten yourself into!")
    brothers = ["peter", "Mario", "Vincenzo"]
    for x in brothers:
    	print (x)
menu()



