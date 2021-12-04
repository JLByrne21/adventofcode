def count_3sets(lst):
    counter = 0
    prev_sum = 0
    with open(lst, 'r') as numbers:
        contents = numbers.read()
        num_list = [int(num) for num in contents.split("\n")]
        for i in range(1, len(num_list)):
            counter += sum(num_list[i : i+3]) > sum(num_list[i-1 : i+2])
                  
        print(counter)

filename = "numbers.txt"
count_3sets(filename)