todos = []

while True:
    user_action = input('Type add, show, edit or exit: ')
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input()
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                item = item.capitalize()
                print(index, '-', item)
        case 'edit':
            existing_todo_index = int(input('Number of todo to edit: '))
            edited_todo = input('Edit your todo now: ')
            todos[existing_todo_index-1] = edited_todo
        case 'exit':
            break
print('Bye!')
