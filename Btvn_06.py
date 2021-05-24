"""Bài 01. Viết hàm
        def max_min(*numbers)
    trả lại cả giá trị max, min của nhiều số được truyền vào
"""
# Bài làm:
"""
def max(*numbers):
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    return max
def min(*numbers):
    min = numbers[0]
    for i in numbers:
        if i < min:
            min = i
    return min
"""
# Bài 2:
"""
Bài 02. Viết hàm
        def reverse_string(str)
    trả lại chuỗi đảo ngược của chuỗi str
"""
# Bài làm:
"""
def reverse_string(str):
    return str[::-1]
print(reverse_string("Python"))
"""
# Bài 3:
"""
Bài 03. Viết hàm
        def is_perfect(n)
    để kiểm tra xem số tự nhiên n có phải là số hoàn hảo hay ko, trả lại True nếu có, False nếu không.
"""
# Bài làm:
"""
def is_perfect(n):
    sum_uoc = 0
    for i in range(1,n,1):
        if n % i == 0:
            sum_uoc += i
    if sum_uoc == n:
        return 'true'
    else:
        return 'false'
print(is_perfect(28))
"""
# Bài 4:
"""
Bài 04. Viết hàm
        def is_prime(n)
    để kiểm tra xem số tự nhiên n có phải số nguyên tố hay không, nếu có thì trả lại True, nếu không thì trả lại False
"""
# Bài làm:
"""
def is_prime(n):
    dem = 0
    for i in (range(1,n+1,1)):
        if n % i == 0:
            dem += 1
    if dem <= 2:
        return "true"
    else:
        return " false"
print(is_prime(7))
"""
# Bài 5:
"""
Bài 05. Viết hàm
        def count_upper_lower(str)
    trả lại số lượng chữ cái viết hoa, số lượng chữ cái viết thường trong chuỗi str
"""
# Bài làm:
"""
def count_upper_lower(str):
    in_hoa = 0
    for n in range(len(str)):
        if 65 <= ord(str[n]) <= 90:
            in_hoa += 1
    return(in_hoa)
print(count_upper_lower('Nguyen Van Tien'))
def count_upper_lower(str):
    thuong = 0
    for n in range(len(str)):
        if 97 <= ord(str[n]) <= 122:
            thuong += 1
    return(thuong)
print(count_upper_lower('Nguyen Van Tien'))
"""
# Bài 6:
"""
Bài 06. Viết hàm
        def is_pangram(str, alphabet)
    đề kiểm tra xem chuỗi str có phải là Pangram không, trả lại True nếu có, False nếu không
Ghi chú: Pangram là chuỗi chứa mỗi chữ cái trong bảng alphabet ít nhất 1 lần
"""
# Bài làm:
"""
def is_pangram(str, alphabet):
    for n in alphabet:
        if n not in str:
            print("đây ko phai chuỗi pangram")
            return "false"
        else:
            return "true"
alphabet = "qwertyuiopasdfghjkzxcvbnm"
str = input("nhập chuỗi kí tự str là:")
print(is_pangram(str,alphabet))
"""
# Bài 7:
"""
Bài 07. 
1. Viết hàm
        def body_mass_index(m, h)
    để tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
2. Viết hàm
        def bmi_information(m, h)
    để đưa ra thông tin về chỉ số BMI cũng như phân loại mức độ gầy - béo của người cân nặng m, chiều cao h
"""
# Bài làm:
"""
m = float(input("nhập m ="))
h = float(input("nhập h ="))
def body_mass_index(m,h):
    BMI = m / (h**2)
    return BMI
s = body_mass_index(m,h)
print(s)
def BMI_information(m,h):
    if s < 18.5:
        return f"Chỉ số BMI của bạn là {s}, cân nặng thấp"
    elif 18.5 <= s <= 24.9:
        return f"chỉ số BMI của bạn là {s}, cân nặng binh thường"
    elif 25 <= s <= 29:
        return f"chỉ số BMI của bạn là {s}, bạn hơi thừa cân"
    else:
        return f"chỉ số cân nặng của bạn là {s}, béo phì"
print(BMI_information(m,h))
"""
# Bài 8:
"""
Bài 08. Viết hàm
        def change_upper_lower(str)
    chuyển toàn bộ các ký tự in hoa sang in thường và in thường thành in hoa trong str
"""
# Bài làm:
"""
str = input("nhập chuỗi các kí tự là:")
def change_upper_lower(str):
    str1 = ""
    for n in range(len(str)):
        if 65 <= ord(str[n]) <= 90:
            str1 += chr(ord(str[n]) +32)
        elif 97 <= ord(str[n]) <= 122:
            str1 += chr(ord(str[n])- 32)
        else:
            str1 += str[n]
    return str1
print(change_upper_lower(str))
"""
# Bài 9:
"""
Bài 09. Viết hàm đệ quy đếm và trả về số lượng chữ số lẻ của số nguyên dương n cho trước.
Ví dụ: Hàm trả về 4 nếu n là 19922610 (do n có 4 số lẻ là 1, 9, 9, 1)
"""
# Bài làm:
"""
n = input("nhập n=")
def he_quy_dem(n):
    'hàm để trả về số lượng chữ số lẻ của sô nguyên dương n cho trước'
    dem = 0
    for m in n:
        if int(m) % 2 == 1:
            dem += 1
    return dem
print(he_quy_dem(n))
"""
"""
Bài 10: Cho dãy số Tribonacci với công thức truy hồi sau:
            F(n) = F(n-1) + F(n-2) + F(n-3),    F(1) = 1, F(2) = 1, F(3) = 2
    Xây dựng 2 hàm để tìm ra số thứ n trong dãy số theo:
        + Hàm Đệ quy
        + Hàm Không đệ quy
"""
# Bài làm:
"""
def tribo(n):
    if n == 0:
        return 0
    elif 0 < n <=2:
        return 1
    else:
        return tribo(n-1) + tribo(n-2) + tribo(n-3)
print(tribo(6))
"""

"""
def tribbo(n):
    f = 0
    a = 1
    b = 1
    c = 2
    i = 4
    while i <= n:
        f = a + b + c
        a = b
        b = c
        c = f
        i += 1
    return f
print(tribbo(7))
"""


