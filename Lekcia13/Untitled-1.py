print ("What is your favourite food?")
food = input()
print ("How old are you?")
age = input()
print ("Where are you from?")
country = input()
print ("What is your favourite season?")
season = input()
print ("Do you like Spongebob?")
spongebob = input()
if spongebob == "Yes":
    spongebob2 = ""
else:
    if spongebob == "No":
        spongebob2 = "don´t"
    else:
        spongebob2 = "Error - We don´t know, if you"
print ("Ok! Then you are " + age + " years old, your favourite food is " + food + ", and you like " + season + " and you " + spongebob2 + " like spongebob. Look! You are from " + country + "!")
