def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        if (x == 0):
            return True
            
        if (x < 0 or x % 10 == 0):
            return False

        rev = 0
        i = 0
        while (temp>0):
            rev *= 10
            rev += temp % 10
            temp = temp // 10
            i -= 1
        return (rev == x)

def main():
    print (isPalindrome(123))

main()