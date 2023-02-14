import database
from datetime import datetime, timedelta

query = database.session.query(database.Table)


def menu():

    print("1) Today's tasks")
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Missed tasks")
    print("5) Add a task")
    print("6) Delete a task")
    print("0) Exit")


def options(option):

    if option == '1':
        tasks_for_today(datetime.today())
    elif option == '2':
        tasks_for_this_week()
    elif option == '3':
        all_tasks()
    elif option == '4':
        missed_tasks()
    elif option == '5':
        add_tasks()
    elif option == '6':
        delete_tasks()
    else:
        print("This option doesn't exist!")


def tasks_for_today(today):

    print("Today:", today.day, today.strftime('%b'))
    if query.count() == 0:
        print("Nothing to do!")
    else:
        row = query.filter(database.Table.deadline == today.date())
        a = 0
        for rows in row.all():
            print("{0}. {1}".format((a := a + 1), rows.task))


def tasks_for_this_week():

    c = 0
    while c <= 7:
        count_date = datetime.today().date() + timedelta(days=c)
        row = query.filter(database.Table.deadline == count_date).order_by(database.Table.deadline)
        print()
        print(count_date.strftime('%A'), count_date.day, count_date.strftime('%b') + ":")
        if row.count() == 0:
            print("Nothing to do!")
            print()
        else:
            a = 0
            for i in row.all():
                print('{0}. {1}'.format((a := a + 1), i.task))
                print()
        c += 1


def all_tasks():

    row = query.order_by(database.Table.deadline)
    if row.count() == 0:
        print("There are no tasks at the moment.")
    else:
        print("All tasks:")
        a = 0
        for rows in row.all():
            print("{0}. {1}. {2} {3}".format((a := a + 1), rows.task, rows.deadline.day,
                                             rows.deadline.strftime('%b')))


def missed_tasks():

    print("Missed tasks:")
    row = query.filter(database.Table.deadline <= datetime.today().date())
    if row.count() == 0:
        print("All tasks have been completed!")
    else:
        a = 0
        for rows in row.all():
            print("{0}. {1}. {2} {3}".format((a := a + 1), rows.task, rows.deadline.day,
                                             rows.deadline.strftime('%b')))
    print()


def add_tasks():

    print("Enter a task")
    task = input()
    print("Enter a deadline ")
    deadline = datetime.strptime(input(), '%Y-%m-%d')
    database.session.add(database.Table(task=task, deadline=deadline))
    database.session.commit()
    print("The task has been added!")


def delete_tasks():

    row = query.order_by(database.Table.deadline)
    if row.count() == 0:
        print("Nothing to delete")
    else:
        print("Choose the number of the task you want to delete:")
        a = 0
        for rows in row.all():
            print("{0}. {1}. {2} {3}".format((a := a + 1), rows.task, rows.deadline.day,
                                             rows.deadline.strftime('%b')))
        print()
        specific_row = row[int(input()) - 1]
        database.session.delete(specific_row)
        database.session.commit()
        print("The task has been deleted!")


def exit_program():

    print("Bye!")
    exit()


while True:

    menu()
    options(input())
