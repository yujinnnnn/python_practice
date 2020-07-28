def solution(n, words):
    before_words = []
    count = 0
    answer = [0, 0]
    for idx, word in enumerate(words):
        count %= n
        if idx >= 1: 
            if (word in before_words) | (before_words[-1][-1] != word[0]): 
                answer = [count + 1, 1 + idx//n]
                break
        count += 1
        before_words.append(word)
    return answer

print(solution(5,['apple', 'egg', 'game', 'elephant', 'tail', 'lane', 'ear', 'row', 'world', 'draft', 'tee', 'equal', 'low', 'weed', 'devil',
         'ladder','rabbit', 'tree', 'enemi', 'yard', 'document', 'tissue', 'error', 'rapid', 'duplicate', 'executive', 'efficient', 'tool']))

# if __name__ == '__main__':
#     words = ['apple', 'egg', 'game', 'elephant', 'tail', 'lane', 'ear', 'row', 'world', 'draft', 'tee', 'equal', 'low', 'weed', 'devil',
#         'ladder','rabbit', 'tree', 'enemy', 'yard', 'document', 'tissue', 'error', 'rapid', 'duplicate', 'executive', 'efficient', 'tool']
#     game_n = input("Enter a number of gamers >> ")
#     print(solution(game_n,apple))