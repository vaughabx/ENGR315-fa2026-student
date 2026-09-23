import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """
    # Initialize variables
    a = 1.0
    b = 1.0 / math.sqrt(2)
    t = 1.0 / 4.0
    p = 1.0

    # Iterate until the desired error is achieved
    while True:
        a_next = (a + b) / 2
        b = math.sqrt(a * b)
        t -= p * (a - a_next) ** 2
        a = a_next
        p *= 2

        # Calculate the approximation of PI
        pi_approximation = (a + b) ** 2 / (4 * t)

        # Check if the approximation meets the target error
        if abs(math.pi - pi_approximation) < target_error:
            return pi_approximation

desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
