# -*- coding: utf-8 -*-
"""
# python hw copy from Han
@ hw6
# 設計一個類別Geometric，用以判斷子類別Circle與Square的顏色
    •若物件為Circle，則設定顏色為綠色，若物件為Square ，則設定顏色為紅色。
    •若物件為Circle，則參數為圓形的半徑，並計算與顯示
         • 圓形的顏色、半徑、直徑、圓周長、面積
    •若物件為Square ，則參數為正方形的邊長，並計算與顯示
         •正方形的顏色、邊長、對角線長、周長、面積

請將程式的流程圖、操作過程與結果寫成實驗報告(以文字為主、圖形為輔)，繳交至Moodle。
"""

class Geometric:
    def __init_(self,color):
        self.color = color
class Circle(Geometric):
    def __init__(self,radius):
        self.color = "green"
        self.radius = radius
        self.diameter = radius*2
        self.circumference = self.diameter*3.1415926
        self.area = radius**2*3.1415926
class Square(Geometric):
    def __init__(self,side_length):
        self.side_length = side_length
        self.color = "red"
        self.diagonal_length= side_length**0.5
        self.perimeter = 4*side_length
        self.area = side_length**2
'''
a = Square(3)
print(a.color)
'''
a = int (input("Which one? 1:circle 2:square "))
if 1 == a:
    b = int (input("radius:"))
    ans = Circle(b)
    print("")
    print(f'color = {ans.color}')
    print(f'radius = {ans.radius}')
    print(f'diameter = {ans.diameter}')
    print(f'circumference = {ans.circumference}')
    print(f'area = {ans.area}')
elif 2 == a:
    b = int (input("input side_length:"))
    ans = Square(b)
    print("")
    print(f'color = {ans.color}')
    print('side_length = %0.3f' %(ans.side_length))
    print(f'diagonal_length = {ans.diagonal_length}')
    print(f'perimeter = {ans.perimeter}')
    print(f'area = {ans.area}')



