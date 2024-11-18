import time

# Simulated OS version
os_version = "1"
system = "NORAD Phantom"

# Function to display the OS menu
def display_menu():
    print("\n--- Welcome to Phantom ---")
    print(f"Current OS version: {os_version}")
    print("1. Check for updates")
    print("2. Display system information")
    print("3. Settings")
    print("4. Shut down")
    print("5. OS specs")
    print('6. restart')



# Function to check for updates
def check_for_updates():
    global os_version
    print("Checking for updates...")
    time.sleep(2)  # Simulate time taken to check for updates
    new_version = "1.1"
    if os_version != new_version:
        os_version = new_version
        print(f"Update found! OS updated to version {os_version}.")
    else:
        print("No updates available. You are already running the latest version.")
        
# idle
def sleep():
        print('System going in sleep mode for thirty seconds')
        time.sleep(30)
        print('Rise and shine!!!!!')
        
        
        
        
        
# restart
def restart():
        print('Restarting System')
        time.sleep(10)
        print('restart Complete')
        
# System specs
system = "PhantomOS"
RAM_Usage = "RAM: <30 megabytes"
CPU_USAGE = "CPU: <5 %"
status = "Idle"
CodeLang = 'Made with Python =)'

# nuclear suite
def nuclear_suite():
    print('-----Welcome to The Phantom Nuclear Suite-----')
    choice = input('Select Nuke: ')
    
    if choice == '0377':
        time.sleep(2)
        print('Nuke sent!')
        time.sleep(10)
        print('TARGET ELIMINATED!')
    elif choice == '2937':
        time.sleep(1)
        print('ICBM sent! I repeat, ICBM SENT!')
        time.sleep(10)
        print('TARGET ELIMINATED!')
    else:
        print('Wrong code')
        print('nuclear lockdown!')
        print('it will take a few seconds to access nukes again')
        time.sleep(5)
        print('Nuclear Lockdown has been lifted')

# Secret code
def Warfare_suite():
    WSM()
    print('Welcome to the warfare suite')#
    choice = input('Awaiting Orders: ')
    
    if choice == 'Activate':
        time.sleep(2)
        print('Suite Activated, Enter your command :)')
    if choice == 'Idle':
        print('Warfare suit on Idle')
    if choice == 'exit suite':
        print('Exiting warfare suite')
    


# Errors
err_1 = "Feature not implement yet. Error Code: 01"
err_2 = "Feature still in development. Error Code: 02"

# Function to display system information
def display_system_info():
    print("\n--- System Information ---")
    print(f"OS version: {os_version}")
    print(system, "From Noob Street Families")
    print("Status: Running smoothly")

# Main function to run the OS
def run_os():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            check_for_updates()
        elif choice == "2":
            display_system_info()
        elif choice == "3":
             print(err_2)
        elif choice == "4":
            print("Shutting down Phantom...")
            time.sleep(3)
            break
        elif choice == "5":
             print(system, RAM_Usage, CPU_USAGE, status, CodeLang)
        elif choice == '1234':
            Warfare_suite()
        elif choice == '0491':
               nuclear_suite()
        elif choice == '6':
                   restart()
        elif choice == 'Sleep':
                   sleep()
                  
                   
            
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    run_os()