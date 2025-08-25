chi_tab = 5.99

def three_digits_poker_test():
    no_of_3_diff_digit = int(input("Enter number of three different digits:"))
    no_of_3_same_digit = int(input("Enter number of all same digits:"))
    no_of_2_same_digit = int(input("Enter number of 2 same digits:"))
    N = no_of_3_diff_digit + no_of_3_same_digit+ no_of_2_same_digit

    expected_freq_3_diff = 0.72 * N
    expected_freq_3_same = 0.01 * N 
    expected_freq_2_same = 0.27 * N 

    calculated_value_3_diff = (no_of_3_diff_digit-expected_freq_3_diff)**2/expected_freq_3_diff;
    calculated_value_3_same = (no_of_3_same_digit-expected_freq_3_same)**2/expected_freq_3_same;
    calculated_value_2_same = (no_of_2_same_digit-expected_freq_2_same)**2/expected_freq_2_same;

    chi_calc = calculated_value_3_diff+calculated_value_3_same+calculated_value_2_same
    if(chi_calc<chi_tab):
        print(f"Chicalc = {chi_calc} < Chitab = {chi_tab} so we accept null hypothesis")
    else:
        print(f"Chicalc = {chi_calc} > Chitab = {chi_tab} so we accept alternate hypothesis")


def four_digits_poker_test():
    no_of_4_diff_digit = int(input("Enter number of 4 different digits:"))
    no_of_1_pair = int(input("Enter number of 1 pair  digits:"))
    no_of_2_pairs = int(input("Enter number of 2 pairs  digits:"))
    no_of_3_same_digit = int(input("Enter number of 3 same digits:"))
    no_of_4_same_digit = int(input("Enter number of 4 same digits:"))
    N = no_of_4_diff_digit+no_of_1_pair+no_of_2_pairs+no_of_3_same_digit+no_of_4_same_digit 

    expected_freq_4_diff = 0.504 * N
    expected_freq_1_pair = 0.432 * N 
    expected_freq_2_pairs = 0.027 * N 
    expected_freq_3_same_digit = 0.036 * N 
    expected_freq_4_same_digit = 0.001 * N 

    calculated_value_4_diff_digit = (no_of_4_diff_digit-expected_freq_4_diff)**2/expected_freq_4_diff;
    calculated_value_1_pair = (no_of_1_pair-expected_freq_1_pair)**2/expected_freq_1_pair;
    calculated_value_2_pairs = (no_of_2_pairs-expected_freq_2_pairs)**2/expected_freq_2_pairs;
    calculated_value_3_same = (no_of_3_same_digit-expected_freq_3_same_digit)**2/expected_freq_3_same_digit;
    calculated_value_4_same = (no_of_4_same_digit-expected_freq_4_same_digit)**2/expected_freq_4_same_digit;

    chi_calc = calculated_value_4_diff_digit+ calculated_value_1_pair + calculated_value_2_pairs +calculated_value_3_same+calculated_value_4_same

    if(chi_calc<chi_tab):
        print(f"Chicalc = {chi_calc} < Chitab = {chi_tab} so we accept null hypothesis")
    else:
        print(f"Chicalc = {chi_calc} > Chitab = {chi_tab} so we accept alternate hypothesis")

    
def main():
    print("Poker test for testing independency of numbers with level of significance 0.05")
    choice = input("Enter a for 3 digit poker test and b for 4 digit poker test:")
    if(choice=="a"):
        three_digits_poker_test()
    elif(choice=="b"):
        four_digits_poker_test()
    else:
        print("Enter correct choice")
main()