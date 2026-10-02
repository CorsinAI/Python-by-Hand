class FizzFuzz:
    def main(self):
        for x in range(1,101):
            
            result = ""

            if x % 3 == 0:
                result += "Fizz"
            if x % 5 == 0:
                result += "Buzz"
            if result == "":
                result += str(x)
            if x % 7 == 0:
                result += "Bazz"

            print(result)

fb = FizzFuzz()
fb.main()