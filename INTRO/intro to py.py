prompt="how has your day been ?"
prompt+="enter'quit'to end of program"
active=True
while active:
 message=input(prompt)
 if message=='quit':
   active=False
 else:
  print(message)