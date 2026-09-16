import re
import string
from collections import Counter

def basic_clean(s)->str:
    '''去掉字符串首尾空格，并合并连续空白字符'''
    return re.sub(r'\s+', ' ', s).strip()


#传入文件名：filename.txt
def text_split(name):
    '''读取文件并分词，返回英文单词、中文片段、数字和标点 token'''
    try:
        with open(name, "r", encoding = "utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Can't find file: {name}")

    return tokenize(content)


def tokenize(content):
    '''清洗文本并分词'''
    content = basic_clean(char_filter(content))
    return re.findall(r"[A-Za-z]+|[\u4e00-\u9fff]+|\d+|[,.]", content)


def char_filter(text)->str:
    '''删除特殊字符，保留英文、数字、中文、逗号和句号'''
    text = re.sub(r"[^A-Za-z0-9\u4e00-\u9fff,.\s]", " ", text)
    return basic_clean(text)

def char_classify_count(tokens)->None:
    '''统计单词、数字、标点符号和出现至少三次的二词词组'''
    words=nums=punctuations=high_frequency_phrase = 0
    for token in tokens:
        if token.isalpha():
            words+=1
        elif token.isdigit():
            nums+=1
        elif token in string.punctuation:
            punctuations+=1

    count = phrase_store(tokens)
    frequent_phrase = {key:value for key, value in count.items() if value >= 3}

    high_frequency_phrase = len(frequent_phrase.keys())
    print(
        f"\nwords: {words} \n"
        f"numbers: {nums} \n"
        f"punctuations: {punctuations} \n"
        f"high frequency phrase: {high_frequency_phrase}" 
    )
    print("and the high frequency phrase:")
    print(frequent_phrase)

def phrase_store(tokens):
    '''记录同一句子中相邻英文单词组成的二词词组'''
    phrases = []
    sentence_words = []
    for token in tokens:
        if re.fullmatch(r"[A-Za-z]+", token):
            sentence_words.append(token.lower())
        else:
            phrases.extend(
                f"{first} {second}"
                for first, second in zip(sentence_words, sentence_words[1:])
            )
            sentence_words = []

    phrases.extend(
        f"{first} {second}"
        for first, second in zip(sentence_words, sentence_words[1:])
    )

    count = Counter(phrases)
    return count
    

def Tokens2Sentence(tokens):
    '''把 tokens 组成句子列表，每个句子仍由 token 列表组成'''
    sentences = []
    sentence = []

    for token in tokens:
        sentence.append(token)

        if token in ['.', '?', '!']:
            sentences.append(sentence)
            sentence = []

    if sentence:
        sentences.append(sentence)
        
    return sentences

def case_normalization(sentences):
    '''将每句英文单词统一为小写，并把句首英文单词首字母大写'''
    after = []
    for sentence in sentences:
        normalized = []
        first_word = True
        for token in sentence:
            if re.fullmatch(r"[A-Za-z]+", token):
                token = token.lower()
                if first_word:
                    token = token.capitalize()
                    first_word = False
            normalized.append(token)
        after.append(_join_tokens(normalized))

    return after


def _join_tokens(tokens):
    '''以正常的英文标点格式拼接 token'''
    text = ""
    for token in tokens:
        if token in [",", "."]:
            text = text.rstrip() + token
        elif not text:
            text = token
        else:
            text += " " + token
    return text

#tokens
def specify_words(sp_words,tokens):
    '''统计指定关键词或短语在文本中的出现次数，不区分大小写'''
    text = _join_tokens(tokens).lower()

    for sp_word in sp_words:
        keyword = basic_clean(
            re.sub(r"[^A-Za-z0-9\u4e00-\u9fff]+", " ", sp_word)
        ).lower()
        if not keyword:
            continue
        times = text.count(keyword)
        if times:
            print(f"\n{keyword}, times: {times}\n")
        else:
            print(f"\n{keyword} is not in this article.\n")

def compare(str1, str2)->str:
    '''最长公共前缀提取 -- 给定两个额外的文献编号字符串，提取二者的最长公共前缀子串并输出'''
    prefix = ""    

    for i in range(min(len(str1), len(str2))):
        if str1[i] == str2[i]:
            prefix += str1[i]
        else:
            break

    return prefix
