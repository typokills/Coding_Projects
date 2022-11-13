# from multiprocessing import Pool
# import time
# tasks = (["A",5],['B',2],['C','1'],['D',3])

# def tasks_exec(tasks_data):
#   print(f'Processes{tasks_data[0]} waiting {tasks_data[1]} seconds')
#   time.sleep(int(tasks_data[1]))
#   print(f'Process {tasks_data[0]} finished')

# def pool_func():
#   p = Pool(2)
#   p.map(tasks_exec,tasks)

# if __name__ == '__main__':
#   pool_func()


from multiprocessing import Process
import sys

rocket = 0

def func1():
    global rocket
    print ('start func1')
    while rocket < sys.maxsize:
        rocket += 1
        print(rocket)
    print ('end func1')

def func2():
    global rocket
    print ('start func2')
    while rocket < sys.maxsize:
        rocket += 1
        print(rocket)
    print ('end func2')

if __name__=='__main__':
    p1 = Process(target=func1)
    p1.start()
    p2 = Process(target=func2)
    p2.start()