"""
ALGORITHM OVERVIEW: LUHN CHECK (MOD 10)
---------------------------------------
1. Reverse the card number.
2. Sum the digits in odd positions (1st, 3rd, 5th, etc.).
3. For digits in even positions (2nd, 4th, 6th, etc.):
   - Double the digit.
   - If the result is > 9, add its digits together (e.g., 12 becomes 1+2=3).
   - Add the result to the even positions sum.
4. Total Sum = (Odd Positions Sum) + (Even Positions Sum).
5. Result: If Total Sum is divisible by 10, the card is VALID.
"""


# Function to check if the card number is valid using Luhn Algorithm
def verify_card_number(card_number):
    sum_of_odd_digits = 0   # Storage for digits that won't be doubled
    # Reverse the string because the algorithm starts from the right
    card_number_reversed = card_number[::-1]
    # Get digits at positions 1, 3, 5... (index 0, 2, 4...)
    odd_digits = card_number_reversed[::2]
    # Convert each string digit to integer and add to the sum
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0  # Storage for digits that WILL be doubled
    # Get digits at positions 2, 4, 6... (index 1, 3, 5...)
    even_digits = card_number_reversed[1::2]

    for digit in even_digits:
        # Multiply the digit by 2 as per the algorithm
        number = int(digit) * 2
        # If result is 10 or more, sum the two digits (e.g., 12 -> 1+2=3)
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    # Final step: sum everything and check if it's divisible by 10
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

# Main function to run the program
def main():
    card_number = '4111-1111-4555-1141'     # The input card number
    # Remove dashes and spaces to get only numbers
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    # Check the result and print the status
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

# Call the main function to start
main()