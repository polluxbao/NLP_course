#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 08:47:59 2020

@author: pollux
"""
L = [6, 3, 9, 12, 15, 1, 2]


#L = [6, 3, 9, 12, 15]
T = 21

# 把已知条件 L 排序
L_sort = sorted(L, reverse=True)

# 结果采用集合，可以避免重复结果
L_out = []

# 采用给出列表元素中位置的方式输出结果
def Lout(LL):
    L_ind = []
    for i1 in LL:
        L_ind.append(L.index(i1) + 1)
    print(sorted(L_ind))

# 扫描 L_list 中所有 sum == T 的元素
def ListCount(L_list):
    # sum 结果验证栈 L_count 重置
    L_count = []
    
    # 逐一输入 L_list 中的数字，验证 sum
    for ind in range(len(L_list)):
        L_count.append(L_list[ind])
        
        # 如果 sum 大于目标值，说明刚压入的数字太大了
        # 把 L_count 最后一个入栈的数字弹出
        if sum(L_count) > T:
            L_count.pop()
            next
        
        # 如果 sum 等于目标值
        # 把当前 L_count 的内容压入 L_out 结果栈
        if sum(L_count) == T:
            L_out.append(L_count.copy())
            L_count.pop()
            next
        

while sum(L_sort) > T:
    ListCount(L_sort)
    L_sort = L_sort[1:]

if sum(L_sort) == T:
    L_out.append(L_sort.copy())

# 如果目标和 T值偏小，结果会出现重复
# 把 L_out 结果去重
L_out_new = []
for L_new in L_out:
    if L_new not in L_out_new:
        L_out_new.append(L_new)



# 打印已知条件
print(L)
print('Target sum : ',T)
print('='*20)
print(L_out_new)
print('='*20)
print('Answer :')

# 按照题目要求，打印结果在原列表中的位置
if L_out_new:
    for i in L_out_new:
        Lout(i)
else:
    # 如果没有合适的答案
    print('No Answer!')