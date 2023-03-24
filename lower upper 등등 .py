python = "Python is Amazing"
print(python.lower()) #소문자
print(python.upper()) #대문자
print(python[0].isupper()) #isupper = is upper
print(len(python)) #길이 나오는거
print(python.replace("Python", "Java")) 
#Python 이라는 문자를 찾아서 Java 라는 문자로 변경.

index = python.index("n") 
#n 이라는 (첫번째) 글자가 몇번째에 있는지 
print(index)

index = python.index("n", index + 1)
#n 이라는 (첫번째 보다 뒤에) 글자가 몇번째에 있는지
print(index)

#print(python.find("Java"))  #find 는 Java 라는게 없으면 -1 반환
#print(python.index("Java")) #index 는 없으면 오류나서 뒤에 구문도 막힘
print("hi")

print(python.count("n"))

