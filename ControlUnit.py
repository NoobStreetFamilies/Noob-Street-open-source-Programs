# ALU Class
class ALU:
    def add(self, a, b):
        return a + b

# Register File Class
class RegisterFile:
    def __init__(self, size):
        self.registers = [0] * size

    def load(self, register_index, value):
        if 0 <= register_index < len(self.registers):
            self.registers[register_index] = value

    def read(self, register_index):
        if 0 <= register_index < len(self.registers):
            return self.registers[register_index]
        return 0

# Control Unit Class
class ControlUnit:
    def __init__(self, alu, register_file, instructions, data_memory):
        self.alu = alu
        self.register_file = register_file
        self.instructions = instructions
        self.data_memory = data_memory
        self.program_counter = 0

    def fetch(self):
        if self.program_counter < len(self.instructions):
            instruction = self.instructions[self.program_counter]
            print(f"Fetched instruction: {instruction}")
            self.program_counter += 1
            return instruction
        return None

    def decode_execute(self, instruction):
        if isinstance(instruction, str):
            parts = instruction.split()
            opcode = parts[0]

            if opcode == "LOAD":
                reg_index = int(parts[1])
                value = int(parts[2])
                self.register_file.load(reg_index, value)

            elif opcode == "ADD":
                reg_dest = int(parts[1])
                reg_src1 = int(parts[2])
                reg_src2 = int(parts[3])
                result = self.alu.add(self.register_file.read(reg_src1), self.register_file.read(reg_src2))
                self.register_file.load(reg_dest, result)

            elif opcode == "STORE":
                reg_index = int(parts[1])
                memory_address = int(parts[2])
                if memory_address < len(self.data_memory):
                    self.data_memory[memory_address] = self.register_file.read(reg_index)
                    print(f"Stored value {self.data_memory[memory_address]} at memory address {memory_address}")
                else:
                    print(f"Memory address {memory_address} out of bounds")

    def run(self):
        while True:
            instruction = self.fetch()
            if instruction is None:
                break
            self.decode_execute(instruction)

# Example usage

alu = ALU()
register_file = RegisterFile(8)
instructions = ["LOAD 0 10", "LOAD 1 20", "ADD 2 0 1", "STORE 2 5"]
data_memory = [0] * 10  # Separate data memory

control_unit = ControlUnit(alu, register_file, instructions, data_memory)
control_unit.run()

print("Register 2 (should be 30):", register_file.read(2))
print("Memory at address 5 (should be 30):", data_memory[5] if len(data_memory) > 5 else "No value at address 5")