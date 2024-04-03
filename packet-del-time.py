def get_input(prompt, type_, min_=None, max_=None):

    #input validation
    while True:
        try:
            user_input = type_(input(prompt))  # Convert input to the expected type
            # Check if input is less than the minimum allowed value
            if min_ is not None and user_input < min_:
                print(f"Please enter a value no less than {min_}.")
                continue
            # Check if input is greater than the maximum allowed value
            if max_ is not None and user_input > max_:
                print(f"Please enter a value no greater than {max_}.")
                continue
            return user_input
        except ValueError:
            print(f"Invalid input. Please enter a value of type {type_.__name__}.")

def calculate_delivery_times(C, PROP, L, i):
    
    #C: Link bit rate in bits per second
    #PROP: Propagation delay in seconds
    #L: Packet size in bits
    #i: Position of the specific bit
    
    packet_delivery_time = L / C + PROP  # Total time for the packet
    bit_delivery_time = PROP + (i - 1) / C  # Time for the specific bit
    return packet_delivery_time, bit_delivery_time

# Collecting validated input from the user
C = get_input("Enter the link bit rate (C) in bits per second: ", float, min_=0.1)
PROP = get_input("Enter the propagation delay (PROP) in seconds: ", float, min_=0.0)
L = get_input("Enter the packet size (L) in bits: ", int, min_=1)
i = get_input("Enter the bit's position (from 1 to L): ", int, min_=1, max_=L)

# Calculating and displaying the results
packet_time, bit_time = calculate_delivery_times(C, PROP, L, i)
print(f"Packet delivery time: {packet_time} seconds")
print(f"Delivery time for bit {i}: {bit_time} seconds")

input("Press Enter to exit")
