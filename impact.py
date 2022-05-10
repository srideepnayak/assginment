from itertools import product

def university(n):
    # Check for corner case
    if n<4:
        return 'Total number of days can not be less than 4'
    no_of_way_to_attend = 0
    miss_ceremony = 0
    
    #Find all possible ways once ca
    truth_table = list(product(('0','1'), repeat=n))
    tt=[''.join(i) for i in truth_table]
    for i in tt:
        if '0000' not in i:
            no_of_way_to_attend += 1
            if i[-1] == '0':
                miss_ceremony += 1
    probability_to_miss = miss_ceremony / no_of_way_to_attend
                
    return str(miss_ceremony) + '/' + str(no_of_way_to_attend)

if __name__ == '__main__':
    print(university(10))
