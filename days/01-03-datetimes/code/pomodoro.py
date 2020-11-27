from datetime import datetime
from datetime import timedelta
from time import sleep


def main():
    print_header()
    tasks = get_tasks()
    for k, v in tasks.items():
        timer(k, int(v))


def print_header():
    print("---------------------------------------------")
    print("               POMODORO TIMER")
    print("---------------------------------------------")
    print("")


def get_tasks():
    tasklist = {}
    while True:
        task = input("Please enter the task you want to complete: ")
        slices = input("How many pomodoros do you think this task needs? ")
        tasklist.update({task: slices})
        more = input("Do you want to add another task? (y/n)")
        if more == "n":
            break

    return tasklist


def timer(task, pomos):
    pomo = timedelta(minutes=25)
    short_break = timedelta(minutes=5)
    long_break = timedelta(minutes=20)
    break_counter = 0
    end_time = datetime.now() + pomo
    pomos_counter = 0

    while pomos_counter <= pomos:
        print(str(datetime.now().replace(microsecond=0)) + " Lets start working on " + task)
        pomos_counter += 1

        while end_time > datetime.now().replace(microsecond=0):
            sleep(1)

        if break_counter < 3 and pomos_counter != pomos:
            print(str(datetime.now().replace(microsecond=0)) + " Lets take a short break!")
            break_counter += 1
            end_time = datetime.now() + short_break
            while end_time > datetime.now().replace(microsecond=0):
                sleep(1)
        elif pomos_counter != pomos:
            print(str(datetime.now().replace(microsecond=0)) + " Lets take a long break!")
            break_counter = 0
            end_time = datetime.now() + long_break
            while end_time > datetime.now().replace(microsecond=0):
                sleep(1)
        else:
            break

    print(f"You are done with {task}. Congratulations.")


if __name__ == '__main__':
    main()
