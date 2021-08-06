# Travis security Program
"""
When customer enter into the system Travis asks customer for their name.

If the name of customer is mentioned in the saved list of customer then Travis says
"Hello" to the customer and ask them for if they want to live the list.

If the name of customer not mentioned in the list then Travis  says “I don’t think I have met you yet”
And then ask them if they wants to get add into the list 

"""

# Known customer 
known =["Sohel", "Amit", "Somnath", "Aakash", "Shubham", "Satish"]

while True:
    print("*"*117)
    print("\n Hi!! My name is Travis.")
    
    name=input("What is your name?: ").strip().capitalize()
    
    if name in known:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system?(y/n)").strip().lower()

        if remove == "y":
            known.remove(name)
        elif remove == "n" :
            print(" No problem, I didn't want to leave anyway!")
    else :
        print ("Hmmm I don't think I have met you yet {}.".format(name))
        add = input ("Would you like to be added to the system?(y/n)").strip().lower()

        if add == "y" :
            known.append(name)
        elif add == "n":
            print("No warries. see you around!")
        
        
