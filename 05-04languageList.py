# 프로그래밍 언어 리스트에서 첨자로 항목 참조

pl = ['C', 'C++', 'Python', 'Java']
print(pl[0], pl[2])
print()
for _ in range(len(pl)): # range(len(pl))를 사용하면 효율적이다!
    print(pl[_])
