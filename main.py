prompt = "Enter a todo:"
todos = []
while True:
    todo = input(prompt)
    if todo == 'exit':
        break
    todos.append(todo.capitalize())

print('Your todos for today are:')
for todo in range(len(todos)):
    print(todos[todo])
