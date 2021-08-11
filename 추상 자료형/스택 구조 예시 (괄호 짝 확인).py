from collections import deque

def parentheses_checker(string):
    """주어진 문자열 인풋의 모든 괄호가 짝이 있는지 확인해주는 메소드"""

    print(f"테스트하는 문자열: {string}")
    stack = deque() # 사용할 스택 정의

    for i in range(len(string)):    # 여는 괄호가 있는 위치를 스택에 저장한다.      
        if string[i] == "(":
            stack.append(i)
        
        elif string[i] == ")":    # 닫히는 괄호가 나올시
        
            if stack:    # 스택에 열린 괄호 위치 데이터가 있으면 
                stack.pop()    # 삭제하고   
        
            else:    # 아니면 현재 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없다고 출력한다.
                print(f"문자열 {i} 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다.")

    while stack:
        print(f"문자열 {stack.pop()} 번째 위치에 있는 괄호가 닫히지 않았습니다.")

            

case1 = "(1+2)*(3+5)"
case2 = "((3*12)/(41-31))"
case3 = "((1+4)-(3*12)/3"
case4 = "(12-3)*(56/3))"
case5 = ")1+14)/3"
case6 = "(3+15(*3"

parentheses_checker(case1)
parentheses_checker(case2)
parentheses_checker(case3)
parentheses_checker(case4)
parentheses_checker(case5)
parentheses_checker(case6)


출력 예시
테스트하는 문자열: (1+2)*(3+5)
테스트하는 문자열: ((3*12)/(41-31))
테스트하는 문자열: ((1+4)-(3*12)/3
문자열 0 번째 위치에 있는 괄호가 닫히지 않았습니다
테스트하는 문자열: (12-3)*(56/3))
문자열 13 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다
테스트하는 문자열: )1+14)/3
문자열 0 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다
문자열 5 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다
테스트하는 문자열: (3+15(*3
문자열 5 번째 위치에 있는 괄호가 닫히지 않았습니다
문자열 0 번째 위치에 있는 괄호가 닫히지 않았습니다
