from sys import exit

start_text = """
You go to sleep late one night. You wake up in a dimly lit room. There's 3 masks, all hung up seperately on three sepreate hooks.
One of the masks has CHNGE written on it. The other STAY. And the last one reads SEE.
A slim humanoid figure then appears and introduces himself as TME.
TME then tells you that the three masks you see will all effect you differently as you put them on.
TME asks if you would like to remain and play along."""
print(start_text)
t = input("Wold you like to continue?")
if t == "Yes":
    print("I thought as much.")
elif t == "No":
    exit()
else:
    print("Go die in a a hole.")
    exit()
