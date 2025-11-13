from core import contact_manager





print(f"WelCome to Contact Manager App")
running_program = True
while running_program:
    mode = input("For following operation enter respective key \n s = Show All \n n = Adding New Contact \n u = Updating previous one  \n d = Deleting Contact \n")
    result = contact_manager.command(mode)
    if result == "exit":
        running_program = False
        
