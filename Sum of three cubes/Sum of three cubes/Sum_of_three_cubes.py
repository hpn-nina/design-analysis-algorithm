def try_cubes(num, x_scalar, y_scalar):
    for x in [x_scalar, x_scalar * -1]:
        for y in [y_scalar, y_scalar * -1]:
                z = (num - x ** 3 - y ** 3)**(1/3)
                if (x ** 3) + (y ** 3) + (z ** 3) == num and z == int(z.real) and z!=0 :
                    return [x, y, int(z.real)]
    return None
def gen_cubes(num):
    if num % 9 != 4 and num % 9 !=5 and abs(num) < 3*pow(10000,2):
        for x in range(1,300):
            for y in range(1,300):
                    res = try_cubes(num, x, y)
                    if res is not None:
                        return res
    return [0,0,0]
def main():
    num=int(input())
    cubes=gen_cubes(num)
    print(cubes[0],cubes[1],cubes[2])
if __name__=='__main__':
    main()