class CardValidator:
    
    def validate(card_number):
        digits = [int(ch) for ch in card_number if ch.isdigit()]
        if len(digits) < 2:
            return False
        check_digit = digits.pop()
        digits.reverse()
        for i in range(len(digits)):
            if i % 2 == 0:
                doubled = digits[i] * 2
                digits[i] = doubled - 9 if doubled > 9 else doubled
        total = sum(digits) + check_digit
        return total % 10 == 0

if __name__ == "__main__":
    card_input = input("Enter your card number: ")
    print("Card is valid." if CardValidator.validate(card_input) else "Card is invalid.")
