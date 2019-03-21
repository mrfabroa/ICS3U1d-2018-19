

def cigar_party(cigars, is_weekend):
    """
    When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars.
    Return True if the party with the given values is successful, or False otherwise.

    :param cigars: the number of cigars
    :param is_weekend: Boolean to see if it is the weekend
    :return: Boolean
    """


    if (40 <= cigars and cigars <= 60) and not(is_weekend):
        # check non-weekend condition
        return True

    elif is_weekend and cigars > 40:
        # weekend condition
        return True

    else:
        return False

# Call the function to test
print(cigar_party(30, False))
print(cigar_party(50, False))
print(cigar_party(20, True))
print(cigar_party(70, True))
print(cigar_party(90, False))
