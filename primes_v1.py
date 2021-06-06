import time

stop_number = int(input("Enter the number you want to stop calculating at: "))
is_prime = True
start_time = time.time()
calculated_primes = []

for number in range(1, stop_number + 1):
    is_prime = True
    for procedures in range(1, len(calculated_primes)):
        if number % procedures == 0 and procedures != 1:
            is_prime = False
            break

    if number != 1 and is_prime:
        print(number)
        calculated_primes.append(number)

print(f"Calculation complete in {time.time() - start_time} seconds.")
