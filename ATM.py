# Prompt user for card type
card_type = input("Your Card type: ")
card_type = card_type.strip().title()

if card_type == "Amex" or card_type == "Visa":
    print("Accepted")
else:
    print("declined")
