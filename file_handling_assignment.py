try:
  with open('Week_5\my_file.txt', 'r') as file:
   contents= file.read()
   file.close()
   print (contents)




except FileNotFoundError:
    # Handle the case when the file is not found
    print(f"Error: File {'my_file.txt'} not found.")

except PermissionError:
    # Handle the case when there's a permission error
    print(f"Error: Permission denied for file '{'my_file.txt'}.")

except Exception as e:
    # Handle any other unexpected exceptions
    print(f"An error occurred: {e}")

finally:
    # This block will always execute, regardless of whether an exception occurred or not
    print("Finally block executed.")

with open('Week_5\my_file.txt', 'a') as file:
  file.writelines(['\n2 bugattis', '\n4 BMWs'])
  file.close()

