#import library
import datetime


#function for extract information from txt file with workers
def read_file(path):
    with open(path) as f:
        data = f.readlines()
        return [x.strip() for x in data]

#var with file where our workers and theres' work time
file_path = 'data_for_workers.txt'

def split_time_string(time_string):
    time_string = time_string.split("-")
    return (datetime.datetime.strptime(time_string[0], '%H:%M').time(),
            datetime.datetime.strptime(time_string[1], '%H:%M').time())

#calculate price for everyone for one hour
def calculate_price_for_hour(time_string, work_time, salary_dict):
    time_string = split_time_string(time_string)

    schedule_range_arr = [split_time_string(x) for x in work_time]
    init_time = time_string[0]
    end_time = time_string[1]
    hours_worked = end_time.hour - init_time.hour
    hour_price = 0

    for i in range(len(schedule_range_arr)):
        if init_time >= schedule_range_arr[i][0] and end_time <= schedule_range_arr[i][1]:
            hour_price = float(salary_dict[work_time[i]])
            break

    return (hour_price, hours_worked)

#weekend allowance for salary
weekend_allowance = 5

#arguments for salary
salary_arg = [25, 15, 20]

#time that workers do their work
work_time = ["00:01-09:00", "09:01-18:00", "18:01-23:59"]

#function that calculate sallary for workers
def calculate_salary(workers_data_path, work_time, salary_dict, weekend_allowance):
    data = read_file(workers_data_path)
    for workers in data:
        separated_data = workers.split("=")
        worker_name = separated_data[0]
        employe_salary_arr = separated_data[1].split(",")
        worker_salary = 0
        for salary in employe_salary_arr:
            salary_schedule = salary[2::]
            hours_worked_price = calculate_price_for_hour(salary_schedule,
                                                             work_time, salary_dict)
            if salary[0:2] in ["MO", "TU", "WE", "TH", "FR"]:
                worker_salary += hours_worked_price[0]*hours_worked_price[1]
            else:
                worker_salary += (hours_worked_price[0] +
                                    weekend_allowance)*hours_worked_price[1]

        print("Week salary for {0} is: {1} USD".format(
            worker_name, round(worker_salary)))

def ziper(*args):
    length = min(len(element) for element in args)
    struct_list = [tuple(struct[i] for struct in map(list, args))
        for i in range(length)]
    return struct_list

#Salary list for workers
def create_salary_list(work_time, salary_arg):
    return dict(ziper(work_time, salary_arg))

if __name__ == '__main__':

    salary_dict = create_salary_list(work_time, salary_arg)
    calculate_salary(file_path, work_time, salary_dict, weekend_allowance)
