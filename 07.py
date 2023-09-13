# 함수

def open_account(): #함수를 정의함
    print("새로운 계좌가 생성되었습니다")

open_account()

#전달값과 반환값

def deposit(balance, money): #잔액이 얼마고 입금할 금액이 얼마인지
    print("입금이 완료되었습니다. 잔액은 {0}원입니다".format(balance + money))
    return balance + money #반환... 이게 먼 용도야? 총 금액을 반환해줌..? 리턴을 통해 반환된 금액을 총 발란스에 저장한다...?

def withdraw(balance, money): #출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다".format(balance-money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다".format(balance))
        return balance

def withdraw_night(balance, money) : #저녁 출금 수수료 붙음
    commission = 100
    return commission, balance - money - commission #수수료가 얼마고, 돈이랑 수수료가 빠져나간 이후 금액이 어떤지

balance = 0 #잔액
balance = deposit(balance, 1000)
print(balance) # 이게 총 잔액

balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원입니다".format(commission, balance))


