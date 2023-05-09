prompt = "Enter a todos:"
todos = []
while True:
    todo = input(prompt)
    if todo == 'exit':
        break
    # title() method capitalizes each word in a sentence
    todos.append(todo.title())

print('Your todos for today are:')
for todo in range(len(todos)):
    print(todos[todo])
