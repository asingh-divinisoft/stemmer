
class PorterStemmer:
    def __init__(self):
        self.vowels = ('a', 'e', 'i', 'o', 'u')

    def is_consonant(self, s: str, i: int):
        return not self.is_vowel(s, i)

    def is_vowel(self, s: str, i: int):
        if s[i].lower() in self.vowels:
            return True
        elif s[i].lower() == 'y':
            if self.is_consonant(s, i-1):
                return True
            else:
                return False

    def find_m(self, s):
        i = 0
        m = 0
        while i < len(s)-1:
            if self.is_vowel(s, i) and self.is_consonant(s, i+1):
                m += 1
                i += 2
            else:
                i += 1
        return m

    def contains_vowel(self, s):
        for v in self.vowels:
            if v in s:
                return True

        for i in range(len(s)):
            if s[i] == 'y':
                if self.is_vowel(s, i):
                    return True

        return False

    def ends_in_dub_const(self, s):
        if s[-2].lower() == s[-1].lower():
            if self.is_consonant(s, -1):
                return True

        return False

    def ends_cvc(self, s):
        if self.is_consonant(s, -1):
            if self.is_vowel(s, -2):
                if self.is_consonant(s, -3):
                    if s[-1] not in ('w', 'x', 'y'):
                        return True

        return False

    def step1a(self, s):
        if s[-4:].lower() == 'sses':
            s = s[:-4] + 'ss'
        elif s[-3:].lower() == "ies":
            s = s[:-3] + "i"
        elif s[-2:].lower() == "ss":
            pass
        elif s[-1].lower() == "s":
            s = s[:-1]
        return s

    def step1b(self, s):
        if s[-3:].lower() == 'eed':
            m = self.find_m(s[:-3])
            if m > 0:
                s = s[:-1]
        elif s[-2:].lower() == 'ed':
            if self.contains_vowel(s[:-2]):
                s = s[:-2]
                s = self.step1ba(s)
        elif s[-3:].lower() == 'ing':
            if self.contains_vowel(s[:-3]):
                s = s[:-3]
                s = self.step1ba(s)

        return s

    def step1ba(self, s):
        if s[-2:].lower() == 'at':
            s = s + 'e'
        elif s[-2:].lower() == 'bl':
            s = s + 'e'
        elif s[-2:].lower() == 'iz':
            s = s + 'e'
        elif self.ends_in_dub_const(s) and s[-1].lower() not in ('l', 's', 'z'):
            s = s[:-1]
        elif self.find_m(s) == 1 and self.ends_cvc(s):
            s += 'e'

        return s

    def step1c(self, s):
        if s[-1].lower() == 'y':
            if self.contains_vowel(s[:-1]):
                s = s[:-1] + 'i'

        return s

    def step5a(self, s):
        if s[-1].lower() == 'e':
            m = self.find_m(s[:-1])
            if m > 1:
                s = s[:-1]
            elif m == 1 and not self.ends_cvc(s[:-1]):
                s = s[:-1]

        return s

    def step5b(self, s):
        m = self.find_m(s)
        if m > 1 and self.ends_in_dub_const(s) and s[-1].lower() == 'l':
            s = s[:-1]

        return s

    def step2(self, s):
        if s[-7:] == 'ational':
            m = self.find_m(s[:-7])
            if m > 0:
                s = s[:-5]+"e"
        elif s[-6:] == 'tional':
            m = self.find_m(s[:-6])
            if m > 0:
                s = s[:-2]
        elif s[-4:] == 'enci':
            m = self.find_m(s[:-4])
            if m > 0:
                s = s[:-1]+"e"
        elif s[-4:] == 'anci':
            m = self.find_m(s[:-4])
            if m > 0:
                s = s[:-1]+"e"
        elif s[-4:] == 'izer':
            m = self.find_m(s[:-4])
            if m > 0:
                s = s[:-1]
        elif s[-4:] == 'abli':
            m = self.find_m(s[:-4])
            if m > 0:
                s = s[:-1]+"e"
        elif s[-4:] == 'alli':
            m = self.find_m(s[:-1])
            if m > 0:
                s = s[:-2]
        elif s[-5:] == 'entli':
            m = self.find_m(s[:-5])
            if m > 0:
                s = s[:-2]
        elif s[-3:] == 'eli':
            m = self.find_m(s[:-3])
            if m > 0:
                s = s[:-2]
        elif s[-5:] == 'ousli':
            m = self.find_m(s[:-5])
            if m > 0:
                s = s[:-2]
        elif s[-7:] == 'ization':
            m = self.find_m(s[:-7])
            if m > 0:
                s = s[:-5]+"e"
        elif s[-5:] == 'ation':
            m = self.find_m(s[:-5])
            if m > 0:
                s = s[:-3]+"e"
        elif s[-4:] == 'ator':
            m = self.find_m(s[:-4])
            if m > 0:
                s = s[:-2]+"e"
        elif s[-5:] == 'alism':
            m = self.find_m(s[:-5])
            if m > 0:
                s = s[:-3]
        elif s[-7:] == 'iveness':
            m = self.find_m(s[:-7])
            if m > 0:
                s = s[:-4]
        elif s[-7:] == 'fulness':
            m = self.find_m(s[:-7])
            if m > 0:
                s = s[:-4]
        elif s[-7:] == 'ousness':
            m = self.find_m(s[:-7])
            if m > 0:
                s = s[:-4]
        elif s[-5:] == 'aliti':
            m = self.find_m(s[:-5])
            if m > 0:
                s = s[:-3]
        elif s[-5:] == 'iviti':
            m = self.find_m(s[:-5])
            if m > 0:
                s = s[:-3]+"e"
        elif s[-6:] == 'bliti':
            m = self.find_m(s[:-6])
            if m > 0:
                s = s[:-3]+"e"

        return s


    def step3(self, s):
        if s[-5:] == 'icate':
            m = self.find_m(s[:-5])
            if m > 0:
                s = s[:-3]
        elif s[-5:] == 'ative':
            m = self.find_m(s[:-5])
            if m > 0:
                s = s[:-5]
        elif s[-5:] == 'alize':
            m = self.find_m(s[:-5])
            if m > 0:
                s = s[:-3]
        elif s[-5:] == 'iciti':
            m = self.find_m(s[:-5])
            if m > 0:
                s = s[:-3]
        elif s[-4:] == 'ical':
            m = self.find_m(s[:-4])
            if m > 0:
                s = s[:-2]
        elif s[-3:] == 'ful':
            m = self.find_m(s[:-3])
            if m > 0:
                s = s[:-3]
        elif s[-4:] == 'ness':
            m = self.find_m(s[:-4])
            if m > 0:
                s = s[:-4]

        return s


    def step4(self, s):
        if s[-2:] == 'al':
            m = self.find_m(s[:-2])
            if m > 1:
                s = s[:-2]
        elif s[-4:] == 'ance':
            m = self.find_m(s[:-4])
            if m > 1:
                s = s[:-4]
        elif s[-4:] == 'ence':
            m = self.find_m(s[:-4])
            if m > 1:
                s = s[:-4]
        elif s[-2:] == 'er':
            m = self.find_m(s[:-2])
            if m > 1:
                s = s[:-2]
        elif s[-2:] == 'ic':
            m = self.find_m(s[:-2])
            if m > 1:
                s = s[:-2]
        elif s[-4:] == 'able':
            m = self.find_m(s[:-4])
            if m > 1:
                s = s[:-4]
        elif s[-4:] == 'ible':
            m = self.find_m(s[:-4])
            if m > 1:
                s = s[:-4]
        elif s[-3:] == 'ant':
            m = self.find_m(s[:-3])
            if m > 1:
                s = s[:-3]
        elif s[-5:] == 'ement':
            m = self.find_m(s[:-5])
            if m > 1:
                s = s[:-5]
        elif s[-4:] == 'ment':
            m = self.find_m(s[:-4])
            if m > 1:
                s = s[:-4]
        elif s[-3:] == 'ent':
            m = self.find_m(s[:-3])
            if m > 1:
                s = s[:-3]
        elif s[-3:] == 'ion':
            m = self.find_m(s[:-3])
            if m > 1 and (s[-4]== "s" or s[-4]=="t"):
                s = s[:-3]
        elif s[-2:] == 'ou':
            m = self.find_m(s[:-2])
            if m > 1:
                s = s[:-2]
        elif s[-3:] == 'ism':
            m = self.find_m(s[:-3])
            if m > 1:
                s = s[:-3]
        elif s[-3:] == 'ate':
            m = self.find_m(s[:-3])
            if m > 1:
                s = s[:-3]
        elif s[-3:] == 'iti':
            m = self.find_m(s[:-3])
            if m > 1:
                s = s[:-3]
        elif s[-3:] == 'ous':
            m = self.find_m(s[:-3])
            if m > 1:
                s = s[:-3]
        elif s[-3:] == 'ive':
            m = self.find_m(s[:-3])
            if m > 1:
                s = s[:-3]
        elif s[-3:] == 'ize':
            m = self.find_m(s[:-3])
            if m > 1:
                s = s[:-3]

        return s

    def __call__(self, s: str):
        s = s.strip()
        s = self.step1a(s)
        s = self.step1b(s)
        s = self.step1c(s)
        s = self.step2(s)
        s = self.step3(s)
        s = self.step4(s)
        s = self.step5a(s)
        s = self.step5b(s)
        return s

if __name__ == '__main__':
    stemmer = PorterStemmer()
    print(stemmer("adjustment"))