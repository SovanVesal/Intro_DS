#Exericse 7 Digit Tool 
def digit_sum(n):
    total_sum=0
    while n>0:
        total_sum = total_sum + n % 10
        n=n//10
        return total_sum

def reverse_number(n):
    reversed_n=0
    while n>0:
        reversed_n = (reversed_n*10)+(n%10)
        n=n//10
        return reversed_n
def is_palindrome(n):
    return n == reverse_number(n)

test_Number=[2026,12312,9875]
for num in test_Number:
    print(f"{num}:Digit Sum = {digit_sum(num)}, reversed = {reverse_number(num)},palindrome = {is_palindrome(num)}")
palindrome_count = 0
for i in range(10, 1000):
    if is_palindrome(i):
        palindrome_count += 1
print(f"Palindromes from 10 to 999: {palindrome_count}")