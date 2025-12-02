#!/usr/bin/env python3

import os

def get_q_format():
    while True:
        try:
            user_input = input("Enter Q format: Q").strip()
            if user_input.lower() in ["q", "quit", "exit"]:
                return None
            
            parts = user_input.replace(",", ".").split(".")
            
            if len(parts) != 2:
                print("Error: Wrong format")
                continue
                
            integer_bits = int(parts[0].strip())
            fractional_bits = int(parts[1].strip())

            if integer_bits < 0 or fractional_bits < 0:
                print("Error: Both numbers in Q format must be non-negative")
                continue

            return integer_bits, fractional_bits

        except ValueError:
            print("Error: Wrong format")
        except KeyboardInterrupt:
            print("\nProgram ended by user")
            return None

def swap_and_inc(val):
    low_byte = val & 0xFF
    high_byte = (val >> 8) & 0xFF
    swapped = (low_byte << 8) | high_byte
    return swapped + 1

def main():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    print("----------- ZDS Project 2. Solver -----------")
    print("// Author: github.com/vertyks")
    print("// Description: Start program on every page in LMS\n//\t it will solve every option in the test step by step.\n\n")

    q_format = get_q_format()
    if q_format is None:
        return

    integer_bits, fractional_bits = q_format
    scale_factor = 2 ** fractional_bits
    
    real_nums = []
    raw_ints = []

    for i in range(2):
        while True:
            try:
                raw_input = input(f"Write a {i+1}. real number (use dot): ").strip()
                real_val = float(raw_input)
                real_nums.append(real_val)
                
                abs_val = abs(real_val)
                fixed_point_val = round(abs_val * scale_factor)
                
                if real_val < 0:
                    transformed_val = swap_and_inc(fixed_point_val)
                    print(f"\t{i+1}) Hex format of {raw_input}: 0x{transformed_val:04X}")
                    raw_ints.append(-fixed_point_val) 
                else:
                    print(f"\t{i+1}) Hex format of {raw_input}: 0x{fixed_point_val:04X}")
                    raw_ints.append(fixed_point_val)
                break
            except ValueError:
                print("Error: Invalid number format")
            except KeyboardInterrupt:
                return

    raw_sum = round(real_nums[0] * scale_factor) + round(real_nums[1] * scale_factor)
    raw_diff = round(real_nums[0] * scale_factor) - round(real_nums[1] * scale_factor)

    print(f"\t3) Summary of two real numbers: 0x{raw_sum & 0xFFFF:04X}")
    print(f"\t4) Difference of two real numbers: 0x{raw_diff & 0xFFFF:04X}")
    
    final_sum_real = raw_sum / scale_factor
    final_diff_real = raw_diff / scale_factor

    print(f"\t5) Result after summing two real numbers: {round(final_sum_real, 2)}")
    print(f"\t6) Result after differencing two real numbers: {round(final_diff_real, 2)}")

if __name__ == "__main__":
    main()