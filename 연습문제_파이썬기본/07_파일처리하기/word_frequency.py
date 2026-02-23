import re
from collections import Counter

def analyze_word_frequency(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
                       
            words = re.findall(r'[가-힣\w]+', content)
            
            counts = Counter(words)
            return counts
            
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다. 경로를 확인해주세요.")
        return None


file_name = 'practice.txt' 
word_counts = analyze_word_frequency(file_name)

if word_counts:
    print("단어 빈도 분석 결과:")
    print()  
    
    for word, count in word_counts.most_common():
        print(f"{word}: {count}번")
        print() 