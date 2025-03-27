from math import pi

class Lab6:


    def __init__(self):
        self.harmonic_sum = 0

    def factorial(self, x):

        if x == 0 or x == 1:
            return 1
        return x * self.factorial(x - 1)

    def sine_x(self, x, n):


        term = lambda i, x_rad: ((-1) ** i * x_rad ** (2 * i + 1)) / self.factorial(2 * i + 1)

        x_rad = x * pi / 180
        result = 0
        for i in range(n):
            result += term(i, x_rad)
        return result

    def harmonic(self, n):

        if n == 1:
            self.harmonic_sum = 1
        else:
            self.harmonic(n - 1)
            self.harmonic_sum += 1 / n



if __name__ == "__main__":
    mathSituations = Lab6()

    print("Factorial:")
    print("5! =", mathSituations.factorial(5))
    print("------------------------------")

    print("sin(30) ≈", mathSituations.sine_x(30, 5))

    print("------------------------------")
    mathSituations.harmonic(5)
    print("Harmonic l
