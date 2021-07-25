"""

Collect information from user:

Here in this project I had collected the information from different peoples asking them few questions
To do this I have used the input function to ask question and variables to store the information.
Then by using print function I have printed the information in one message.


"""

# name
name = input ("what is your name? :")

#age
age = input ("How old are you? :")

#city
city = input ("Which city do you live in? :")

#love
love = input ("What do You love doing? :")

#output
string = "Your name is {} and you are {} years old. You live in {} and you love {}."
output = string.format(name, age, city, love)

#print
print(output)
