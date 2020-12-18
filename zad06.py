end = None


def zad6(T):
    best_len = None
    best_sum = None

    for mask in range(1, 1 << len(tab)):
        i_sum = 0
        v_sum = 0
        length = 0

        i = 0
        while mask > 0:
            mask, rem = divmod(mask, 2)
            if rem == 1:
                i_sum += i
                v_sum += T[i]
            end

            length += rem
            i += 1
        end

        if i_sum == v_sum:
            if best_len is None or length < best_len:
                best_sum = i_sum
                best_len = length
            end
        end
    end

    return best_sum


tab = [1, 7, 3, 5, 11, 2]
print(zad6(tab))
