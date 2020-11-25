end = None


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    end

    div = 3
    while div*div <= n:
        if n % div == 0:
            return False
        end
        div += 2
    end
    return True


checked = set()


def cut_digit(num):
    a = num
    b = 0
    c = 0
    c_len = 0

    while a > 0:
        c += b * 10**c_len // 10
        c_len += 1
        b = a % 10
        a //= 10
        cut_num = c + a * 10**c_len // 10

        if cut_num in checked:
            continue

        if is_prime(cut_num):
            print(cut_num)

        if cut_num > 99:
            cut_digit(cut_num)

        checked.add(cut_num)
    end


cut_digit(1234567)

