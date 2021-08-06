# Slicing the User Name and Domain Name from email id 

# email id
email = input ("What is your email id ?:")

#slice user name

user_name = email[:email.index("@")]

#domain name
user_domain = email[email.index("@")+1::1]

#out
string = "Your user name is {} and your domain name is {}"

out=string.format(user_name, user_domain)

print(out)
