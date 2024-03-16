import os

def create_file(size_in_b, file_name):
    with open(file_name, 'wb') as f:
        f.write(b'\0' * size_in_b)

b = int(input("Enter the size of the file in bytes: "))
mb = int(input("Enter the size of the file in megabytes: "))
gb = int(input("Enter the size of the file in gigabytes: "))

total_size = b + mb * 1024 * 1024 + gb * 1024 * 1024 * 1024

file_name = "test_file.txt"
create_file(total_size, file_name)

print(f"File with size {total_size} bytes created successfully as {file_name}")
