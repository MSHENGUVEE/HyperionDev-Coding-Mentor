def read_number(numeral):
    # Define word representations for numbers
    units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    thousands = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion', 'decillion']

    # Helper function to convert a three-digit number to words
    def convert_three_digits(num):
        words = ''
        hundreds = num // 100
        tens_units = num % 100

        if hundreds > 0:
            words += units[hundreds] + ' hundred '

        if tens_units > 0:
            if tens_units < 10:
                words += units[tens_units]
            elif tens_units < 20:
                words += teens[tens_units % 10]
            else:
                tens_digit = tens[tens_units // 10]
                units_digit = units[tens_units % 10]
                words += tens_digit + '-' + units_digit

        return words.strip()

    # Handle special case for zero
    if numeral == '0':
        return 'zero'

    # Split the numeral into groups of three digits each
    groups = []
    while numeral:
        groups.append(int(numeral[-3:]))
        numeral = numeral[:-3]

    # Convert each group of three digits to words
    words = ''
    for i, group in enumerate(groups):
        group_words = convert_three_digits(group)
        if group_words:
            if i > 0:
                group_words += ' ' + thousands[i]
            words = group_words + ' ' + words

    return words.strip()


# Example usage:
numeral = input("Enter a numeral: ")
read_as_words = read_number(numeral)
print("Number in words:", read_as_words)
