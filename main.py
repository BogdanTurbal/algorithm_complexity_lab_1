import sys

class PolynomialHashing:
    def __init__(self, p=31, m=10**9 + 9, table_size=10**6):
        self.p = p 
        self.m = m  
        self.table_size = table_size
        self.hash_table = [[] for _ in range(table_size)] 

    def compute_hash(self, s: str) -> int:
        hash_value = 0
        p_pow = 1
        for char in s:
            hash_value = (hash_value + (ord(char) - ord('a') + 1) * p_pow) % self.m
            p_pow = (p_pow * self.p) % self.m
        return hash_value

    def get_index(self, s: str) -> int:
        return self.compute_hash(s) % self.table_size

    def add_string(self, s: str):
        idx = self.get_index(s)
        if s not in self.hash_table[idx]:
            self.hash_table[idx].append(s)

    def remove_string(self, s: str):
        idx = self.get_index(s)
        if s in self.hash_table[idx]:
            self.hash_table[idx].remove(s)

    def check_string(self, s: str) -> bool:
        idx = self.get_index(s)
        return s in self.hash_table[idx]

    def find_palindromes(self):
        palindromes_len_1 = []
        palindromes_len_gt_1 = []
        for chain in self.hash_table:
            for s in chain:
                if self.check_palindrome(s):
                    if len(s) == 1:
                        palindromes_len_1.append(s)
                    else:
                        palindromes_len_gt_1.append(s)
        return palindromes_len_1, palindromes_len_gt_1

    def check_palindrome(self, s: str) -> bool:
        return self.compute_hash(s) == self.compute_hash(s[::-1])


def process_operation_in_real_time(poly_hash, operation):
    op, value = operation.split()

    if op == '+':
        poly_hash.add_string(value)
    elif op == '-':
        poly_hash.remove_string(value)
    elif op == '?':
        exists = poly_hash.check_string(value)
        print("yes" if exists else "no")


def process_operations(operations, t=False):
    poly_hash = PolynomialHashing()
    results = []
    
    for operation in operations:
        if operation == "#":
            break
        op, value = operation.split()
        
        if op == '+':
            poly_hash.add_string(value)
        elif op == '-':
            poly_hash.remove_string(value)
        elif op == '?':
            exists = poly_hash.check_string(value)
            if t:
                print("yes" if exists else "no")
            results.append("yes" if exists else "no")
    
    palindromes_len_1, palindromes_len_gt_1 = poly_hash.find_palindromes()
    results.append(f"Palindromes of length 1: {len(palindromes_len_1)}")
    results.append(f"Palindromes: {', '.join(palindromes_len_1)}")
    results.append(f"Palindromes of length > 1: {len(palindromes_len_gt_1)}")
    results.append(f"Palindromes: {', '.join(palindromes_len_gt_1)}")
    
    return results


def real_time_terminal(poly_hash):
    """Process operations in real-time as they are entered."""
    print("Enter operations (end with #):")
    while True:
        operation = input().strip()
        if operation == "#":
            break
        process_operation_in_real_time(poly_hash, operation)

    # After the input ends with '#', show the palindrome counts and the palindromes themselves
    palindromes_len_1, palindromes_len_gt_1 = poly_hash.find_palindromes()
    print(f"Palindromes of length 1: {len(palindromes_len_1)}")
    if palindromes_len_1:
        print(f"Palindromes: {', '.join(palindromes_len_1)}")
    
    print(f"Palindromes of length > 1: {len(palindromes_len_gt_1)}")
    if palindromes_len_gt_1:
        print(f"Palindromes: {', '.join(palindromes_len_gt_1)}")


def read_from_file():
    with open('random_operations.txt', 'r') as f:
        operations = f.read().strip().splitlines()
    return operations


def write_output_to_file(output):
    with open('output.txt', 'w') as f:
        for line in output:
            f.write(line + '\n')


def main():
    source = input("Read from terminal or file (t/f)? ").strip().lower()
    poly_hash = PolynomialHashing()

    if source == 't':
        real_time_terminal(poly_hash)
    elif source == 'f':
        operations = read_from_file()
        output = process_operations(operations)
        write_output_to_file(output)
        print("Output written to output.txt")
    else:
        print("Invalid input. Please choose 't' for terminal or 'f' for file.")


if __name__ == "__main__":
    main()
