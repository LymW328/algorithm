a =[('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
#튜플을 요소로 가지는 리스트
print(dict(a))
menu = dict(a)
pcs = menu.values()
pc =(list(pcs))
pc.sort()
print(pc)
hst = pc[-1]
print([k for k, v in menu.items() if v == hst]) #검색해서 찾은 문제, key값으로 value를 찾는 방법!
