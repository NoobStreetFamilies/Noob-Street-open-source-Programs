import cmd

class SimpleCMD(cmd.Cmd):
    intro = 'Welcome to the Simple CMD prototype. Type help or ? to list commands.\n'
    prompt = '(cmd) '
    
    # Basic command
    def do_greet(self, arg):
        'Greet the user'
        print(f"Hello, {arg}!")

    # Command to exit the CLI
    def do_exit(self, arg):
        'Exit the command prompt'
        print('Goodbye!')
        return True

    # Handling unrecognized commands
    def default(self, line):
        print(f"Unrecognized command: {line}")

if __name__ == '__main__':
    SimpleCMD().cmdloop()