from art import logo
print(logo)

# Calculator

# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

# Operations Dictionary
operations = {
  "+": add, 
  "-": subtract,
  "*": multiply,
  "/": divide,
}
def calculator():
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
  
  while should_continue:
    
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation = operations[operation_symbol]
    answer = calculation(num1, num2)
  
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation.: ").lower() == "y":
      num1 = answer
    else:
      should_continue = False
      calculator() # if the should_continue = False condition didn't exist, this would become an infinite loop.
      
calculator()