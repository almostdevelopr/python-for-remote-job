todos = []

while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input()
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                item = item.capitalize()
                print(f'{index + 1} -{item}')
        case 'edit':
            existing_todo_index = int(input('Number of todo to edit: '))
            edited_todo = input('Edit your todo now: ')
            todos[existing_todo_index-1] = edited_todo
        case 'complete':
            number = int(input('Number of todo to complete: '))
            todos.pop(number - 1)
        case 'exit':
            break
print('Bye!')
