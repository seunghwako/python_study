# 문제 : https://programmers.co.kr/learn/courses/30/lessons/64061?language=python

def solution(board, moves):
    answer = 0
    stack = []
    for i in moves :
        for j in range(len(board)):
            if board[j][i-1] != 0 :
                if len(stack) == 0 :
                    stack.append(board[j][i-1]) 
                    board[j][i-1] = 0
                elif stack[-1] == board[j][i-1] :
                    board[j][i-1] = 0
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[j][i-1])
                    board[j][i-1] = 0
                break
    return answer