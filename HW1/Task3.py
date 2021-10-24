# equations are checked if all points satisfy: y=a*x+b % mod
def check_points_for_equation(a, b, points_list, mod):
    for x, y in points_list:
        if y != (a * x + b) % mod:
            return False
    return True


def get_function_for_points_with_mod(points_list, mod):
    for a in range(mod):
        for b in range(mod):
            if check_points_for_equation(a, b, points_list, mod):
                return a, b
    return None, None


enc_points = [(18, 13), (20, 9), (17, 2), (5, 0), (0, 23), (2, 19), (4, 15)]
print("Our encryption function is: ")
print(get_function_for_points_with_mod(enc_points, 26))

dec_points = [(13, 18), (9, 20), (2, 17), (0, 5), (23, 0), (19, 2), (15, 4)]
print("Our decryption function is: ")
print(get_function_for_points_with_mod(dec_points, 26))
