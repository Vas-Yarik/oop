filename = input('Enter the file name: ')
print()
try:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    print(content)
except FileNotFoundError as e:
    print(f"Ошибка: {e}")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")

