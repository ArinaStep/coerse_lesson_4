# O(M*N)
# def strcounter(s):
#     for sym in set(s): #сортирует чтобы было по 1 элементу
#         count = 0
#         for sub_sym in s:
#             if sym ==sub_sym:
#                 count+=1
#         print(sym,'-', count)
#
# strcounter('aab')
# O(M+N)
# def strcounter(s):
#     syms_counter={}
#     for sym in s:
#         syms_counter[sym]=syms_counter.get(sym,0)+1
#     for sym,count in syms_counter.items():
#         print(sym,'-',count)
# strcounter('aaaaaaaaaaaaaabbbccccccddd')

#Домашнее задание
s=input()
h=len(s)//2
print(s[:h]==s[:len(s)-h-1:-1])
