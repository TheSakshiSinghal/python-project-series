def print_menu():
    print('\nTodo List Menu:')
    print('1. View Tasks')
    print('2. Add a Task')
    print('3. Remove a Task')
    print('4. Exit')


def get_choice():
    while True:
        choice = input('Enter your choice: ').strip()  # Strip whitespace
        valid_choices = ('1', '2', '3', '4')
        if choice not in valid_choices:
            print('Invalid choice. Please enter 1, 2, 3, or 4.')
            continue
        else:
            return choice


def display_tasks(tasks):
    if not tasks:
        print('No tasks in the list.')
        return
    
    for index, task in enumerate(tasks, start=1):
        print(f'{index}. {task}')


def add_task(tasks):
    while True:
        task = input('Enter a new task: ').strip()
        if len(task) != 0:
            tasks.append(task)
            print(f'Task "{task}" added successfully.')
            break
        else:
            print('Invalid task! Please enter a valid task.')


def remove_task(tasks):
    display_tasks(tasks)

    if not tasks:
        return  # No tasks to remove

    while True:
        try:
            task_number = int(input('Enter the task number to remove: ').strip())
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f'Task "{removed_task}" removed successfully.')
                break
            else:
                print('Invalid task number. Please try again.')
        except ValueError:
            print('Invalid input! Please enter a number.')


def main():
    tasks = []

    while True:
        print_menu()

        choice = get_choice()

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print('Thank you for using the Todo List application. Goodbye!')
            break


if __name__ == '__main__':
    main()
