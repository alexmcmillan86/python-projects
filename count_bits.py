def count_bits(x: int) -> int:
    if x <= 0:
        print("Usage: Enter a positive integer!")
        return 1
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    print(num_bits)
    return 0


number = int(input("Enter a number: "))
count_bits(number)
