def count_larger_than_prev(lst):
    counter = 0
    with open(lst, 'r') as numbers:
        contents = numbers.read()
        num_list = contents.splitlines()
        for i in range(1, len(num_list)):
            if int(num_list[i]) > int(num_list[i-1]):
                counter += 1
        print(counter, len(num_list))

filename = "numbers.txt"
count_larger_than_prev(filename)
