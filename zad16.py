from meszstack import meszgen


def wyraz(s1, s2=""):

    # counts vowels in string
    def vowels(text):
        count = 0
        for letter in text:
            for a in "aeiouy":
                if letter is a:
                    count += 1
        return count

    # return (sum of ascii char's dec value, vowels in string)
    def weight(text):
        asc_sum = 0
        for a in text:
            asc_sum += ord(a)
        return asc_sum, vowels(text)

    s1_weight = weight(s1)
    s2_weight = weight(s2)

    if s1_weight[1] > 0:  # if vowels exist in s1
        if s2_weight[1] < s1_weight[1]:  # if s2 has less vowels than s1 we cannot make a subset that has the same number of vowels
            return False

    for subset in meszgen(s2):
        text = ""
        for n in subset:
            text += s2[n]
        if weight(text) == s1_weight:
            return True

    return False


print(wyraz("testxdd", "alahehe"))
