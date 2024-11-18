import time

# Simulated OS and BIOS version
os_version = "1.0"
bios_installed = False

# Bootup sequence
def bootup_sequence():
    cores = [
        '[Core 1: Online]',
        '[Core 2: Online]',
        '[Core 3: Online]',
        '[Core 4: Online]'
    ]

    print('Initializing Memory')
    time.sleep(4)
    print('[SnapOS Boot Sequence Initializing...]')
    print('[Loading SnapCore ARC Corsair v1.0...]')

    print('[Initializing Cores...]')
    time.sleep(3)
    for core in cores:
        print(core)

    print('[Loading Memory...]')

    print('[L1 Cache: Active]')
    print('[L2 Cache: Active]')
    time.sleep(2)
    print('[Initializing Registers...]')
    print('[Checking System Integrity...]')
    time.sleep(3)
    print('[System Status: All Systems Nominal]')
    time.sleep(4)
    print('[Launching SnapOS...]')

# Power-off sequence
def power_off_sequence():
    print("\n[Powering down SnapOS...]")
    time.sleep(2)
    print("[Saving session data...]")
    time.sleep(3)
    print("[Deactivating cores...]")
    cores = [
        '[Core 1: Offline]',
        '[Core 2: Offline]',
        '[Core 3: Offline]',
        '[Core 4: Offline]'
    ]
    for core in cores:
        print(core)
    time.sleep(3)
    print("[Releasing memory resources...]")
    time.sleep(2)
    print("[Shutting down system...]")
    time.sleep(4)
    print("[SnapOS has been powered off.]")

# Function to display the OS menu
def display_menu():
    print("\n--- Welcome to SnapCore Dashboard ---")
    print(f"Current Model and OS version: ARC Corsair {os_version}")
    print("1. Check for updates")
    print("2. Display system information")
    print("3. Launch Terminal")
    print("4. Exit")

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

# Function to display system information
def display_system_info():
    print("\n--- System Information ---")
    print(f"OS version: {os_version}")
    print("Device: FlipOS Virtual Machine")
    print("Status: Running smoothly")

# Terminal function with commands: install bios, help, and systemver
def terminal():
    global bios_installed
    
    while True:
        command = input("Noob-Terminal$ ").lower()
        
        if command == "install bios":
            if not bios_installed:
                print("Installing BIOS...")
                time.sleep(3)
                bios_installed = True
                print("BIOS installation successful!")
            else:
                print("BIOS is already installed.")
        
        elif command == "help":
            print("\n--- Help Menu ---")
            print("Available commands:")
            print("install bios - Simulates the installation of BIOS.")
            print("help - Displays this help menu.")
            print("systemver - Displays the current OS version.")
            print("exit - Exits the terminal and returns to the dashboard.")
        
        elif command == "systemver":
            print(f"\n--- System Version ---")
            print(f"Current OS version: {os_version}")
            bios_status = "Installed" if bios_installed else "Not Installed"
            print(f"BIOS status: {bios_status}")
        
        elif command == "exit":
            print("Exiting Noob-Terminal...")
            break  # This exits the terminal and returns to the main program
        
        else:
            print("Invalid command. Type 'help' for a list of available commands.")

# Main function to run the OS
def run_os():
    bootup_sequence()  # Bootup sequence runs before the OS starts
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            check_for_updates()
        elif choice == "2":
            display_system_info()
        elif choice == "3":
            terminal()  # Launch the terminal
        elif choice == "4":
            power_off_sequence()  # Power off sequence when shutting down
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_os();;;