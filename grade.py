def solution(purchase):
    # 회원 등급제
    # 최근 30일간 구매 금액에 따라서 등급 책정
    # 고객의 2019.01.01 ~ 2019.12.31 기간의 구매 기록이 문자열 형태로 담긴 배열 purchase
    #각 등급별 유지 기간을 순서대로 배열에 담아 return

    answer = []
    day31 = ['01', '03', '05', '07', '08', '10', '12']
    day30 = ['04', '06', '09', '11']
    day28 = ['02']
    record = dict()

    for i in purchase :
        year, month, day = i.split('/') # 년, 월, 일 + 구매 금액으로 나누고
        day, money = day.split() # 일, 구매금액으로 나눠    

        # 구매 기록은 30일간 유지되면서 등급에 확인됨
        # 기간 정리를 간편하게 하기 위해 월 단위를 일 단위로
        if month in day31 :
            day = int(month) * 31 + int(day)
        elif month in day30 :
            day = int(month) * 30 + int(day)
        elif month in day28 :
            day = int(month) * 28 + int(day)
        
        print(year, month, day-31, money)

        # 날짜와 구매 금액을 dict
        record[day-31] = money
    day_check = 0
    current_money = 0

    bronze = 0
    silver = 0
    gold = 0
    platinum = 0
    diamond = 0

    arr = [0 for _ in range(365)]
    for i in range(365) :
        if i in record :
            for j in range(30) :
                if i+j >= 365 :
                    break
                arr[i+j-1] = int(arr[i+j-1]) + int(record[i])
                

        if int(arr[i]) < 10000 : 
            bronze += 1
        elif int(arr[i]) < 20000 : 
            silver += 1
        elif int(arr[i]) < 50000 : 
            gold += 1
        elif int(arr[i]) < 100000 : 
            platinum += 1
        elif int(arr[i]) >= 100000 : 
            diamond += 1
        
    answer.append(bronze)
    answer.append(silver)
    answer.append(gold)
    answer.append(platinum)
    answer.append(diamond)


        
    print(arr)


    return answer


if __name__ == "__main__" :
    purchase1 = ["2019/01/01 5000", "2019/01/20 15000", "2019/02/09 90000"]
    
    print(solution(purchase1))
    purchase2 = ["2019/01/30 5000", "2019/04/05 10000", "2019/06/10 20000", "2019/08/15 50000", "2019/12/01 100000"]
    
    print(solution(purchase2))
