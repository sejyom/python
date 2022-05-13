#한 글자 단어와 과일의 정렬

word=list('삶꿈정')
word.extend('복빛')
print('word: ', word)
word.sort() #정렬
print('sort: ', word)

fruit=['복숭아', '자두', '골드키위', '귤']
print('fruit: ', fruit)
fruit.sort(reverse=True)
print('sort: ', fruit)

mix = word+fruit
print('sorted: ', sorted(mix))
print('reverse sorted: ', sorted(mix, reverse=True
