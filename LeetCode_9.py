def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        if (x<0):
            return False
        rev = 0
        i = 0
        while (temp>0):
            rev += (temp % 10) * (10 ** i)
            temp = temp // 10
            i += 1
        return (rev == x)

def main():
    print (isPalindrome(121))

main()