import multiprocessing
import datetime

def read_info(name):
    all_data=[]
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                all_data.append(line)
    return all_data

filenames = [f'./file {number}.txt' for number in range(1, 5)]

#Линейный
# start = datetime.datetime.now()
# read_info(filenames[0])
# read_info(filenames[1])
# read_info(filenames[2])
# read_info(filenames[3])
# end = datetime.datetime.now()
# print(end-start)


# Многопроцессорный
if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end-start)

