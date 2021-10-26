# Summer/Winter Coding(2019)
# https://programmers.co.kr/learn/courses/30/lessons/62048
import math

"""
가로 길이가 w, 세로 길이가 h인 직사각형
대각선 꼭지점을 잇는 방식으로 잘라서 직각삼각형 2개로 나눈다
1cm, 1cm 격자 타일로 나눴을 때, 잘랐다면 사용할 수 있는 정사각형의 개수는?
"""



def solution(w,h):
    
    # 전체 정사각형의 개수는 w*h
    # 이후, 대각선으로 잘라서 사용할 수 없는 정사각형의 개수를 구한 뒤
    # 그 값을 빼면 된다?
    # 좌표식에서, 최대공약수는 대각선으로 가르는 직선이 만나는 점의 수.
    # 한 점당 잘라지는 사각형의 수는 (w//g) + (h//g) - 1. g는 최대공약수
    # 즉, 잘라지는 사각형의 개수는 ((w//g) + (h//g) - 1) * g = w + h - g
    # 최대공약수가 1이면 잘라지는 사각형의 개수는 w+h-1 
    divide = math.gcd(w, h)
    return (w*h) - (w+h - divide)









if __name__ == "__main__" :
    w = 8
    h = 12
    print(solution(w, h)) 
    # result = 80