#largest palindrome product

def isPalindrome(n):
    number = str(n)
    left = 0
    right = len(number)-1
    while left <= right:
        if number[left] != number[right]:
            return False
        left += 1
        right -= 1
    return True

 
def LPP(digits):
    best = 0
    n1 = int('9'*digits)
    while n1 > 0:
        n2 = n1
        while n2 > 0:
            product=n1*n2
            if product < best: break
            if isPalindrome(product):
                best = max(best, product)
            n2 -= 1
        n1 -= 1
    return best
        
print(LPP(3))
