def multiplication_table_pretty(num, up_to=10):
    print(f"--- Multiplication Table for {num} ---")
    for i in range(1, up_to + 1):
        print(f"| {num} x {i:2} | {num * i:3} |")
    print("-" * 30)


number = int(input("Enter the number for the multiplication table: "))
limit = int(input("Enter how far you want the table to go: "))
multiplication_table_pretty(number, limit)
