kor = ["사과", "바나나", "오렌지"]
eng = ["apple", "banna", "orange"]

print(list(zip(kor, eng)))          # 통합

mixed = [('사과', 'apple'), ('바나나', 'banna'), ('오렌지', 'orange')]
print(list(zip(*mixed)))            # *을 넣음으로써 분리

kor2, eng2 = zip(*mixed)
print(kor2)
print(eng2)