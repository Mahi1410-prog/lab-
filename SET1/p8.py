def sort_numbers (numbers, reverse=False):
    return sorted (numbers, reverse=reverse)
my_list = [5,2,9,7,4,1]
print("Ascending Order List: ", sort_numbers (my_list, reverse=False))
print("Descending Order List: ", sort_numbers (my_list, reverse=True))