# take a single line of an expression and calculate it

def calculateExpression(expression):
    try:
        result = eval(expression)
        return result           
    except Exception as e:
        return f"Error in calculation: {e}"
    



while True:
        try:
            expr = input("Enter a mathematical expression to calculate: ")
            print("Result:", calculateExpression(expr)) 
        except ValueError:
            print("Invalid input. Please enter a numeric expression.")

        restart = input("Do you want to calculate another expression? (yes/no): ").strip().lower()
        if restart != 'yes':
            break           