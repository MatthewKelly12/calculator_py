class Calculator():
    """Performs the four basic mathematical operations

    Methods:
     add(number, number)
     subtract(number, number)
     multiply(number, number)
     divide(number,number)
    """

    def add(self, firstOperand, secondOperand):
        """Adds two numbers together

        Arguments:
          firstOperand - Any number
          secondOperand - An number
        """

        return firstOperand + secondOperand

    def subtract(self, num1, num2):
        """Subtracts two numbers together

        Arguments:
          num1 - Any number
          num2 - An number
        """

        return num1 - num2

    def multiply(self, num1, num2):
        """ Multiplies two numbers together

            Arguments:
                num1 - any number
                num2 - any number
        """

        return num1 * num2

    def divide(self, num1, num2):
        """ Divides two numbers

            Arguments:
                num1 - any number
                num2 - any number
        """

        return num1/num2