# zip 함수 테스트하기
# 여러개의 순회가능한 객체를 인자로 받고 각 객체가 담고있는 원소를 튜플형태로 차례로 접근할 수 있눈 반복자 반환

numbers = [1, 2, 3]
letters = ['A', 'B', 'C']

for pair in zip(numbers, letters) :
    print(pair)
print()

for number, upper, lower in zip("12345", "ABCDE", "abcde"):
    print(number, upper, lower)
print()    

# 문자열과 배열의 혼합 가능
# 각 객체를 묶지만 가장 짧은 길이의 객체 위주로 나타낼 수 있다.
# letter의 길이는 3, "12345"의 길이는 5, "abcdefg"의 길이는 7인데 실제 표현되는 형태는 letter의 길이인 3만큼만 표현됨
for number, upper, lower in zip("12345", letters, "abcdefg") :
    print(number, upper, lower)
print()

# dict 사전 만들기
test_dict = dict(zip(numbers, letters))
print(test_dict)

# 문자열과 배열 혼합 가능. 하지만 길이는 짧은 쪽으로 맞춰지고, 남는 문자열 or 배열은 버려진다
long_letters = "abcdefg"
tdict = dict(zip(numbers, long_letters))
print(tdict)

 