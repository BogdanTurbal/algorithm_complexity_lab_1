import random
import string

def generate_random_string(length=5):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_random_operations(num_operations, max_str_length=15):
    operations = []
    existing_strings = set() 

    for _ in range(num_operations):
        operation_type = random.choices(['+', '-', '?'], weights=[0.8, 0.1, 0.1])[0]

        if operation_type == '+':
            random_str = generate_random_string(random.randint(1, max_str_length))
            operations.append(f"+ {random_str}")
            existing_strings.add(random_str)
        elif operation_type == '-':
            if existing_strings:
                random_str = random.choice(list(existing_strings))
                operations.append(f"- {random_str}")
                existing_strings.remove(random_str)
        elif operation_type == '?':
            if random.random() < 0.5 and existing_strings:
                random_str = random.choice(list(existing_strings))
            else:
                random_str = generate_random_string(random.randint(1, max_str_length))
            operations.append(f"? {random_str}")

    operations.append("#")
    return operations

def write_operations_to_file(filename, num_operations):
    operations = generate_random_operations(num_operations)
    with open(filename, 'w') as f:
        for operation in operations:
            f.write(operation + '\n')

if __name__ == "__main__":
    num_operations = 10**5 
    output_file = "random_operations.txt"
    
    write_operations_to_file(output_file, num_operations)
    print(f"Generated {num_operations} random operations and saved to {output_file}")
