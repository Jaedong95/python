import re 
from gensim.utils import to_unicode 

# 제거할 불필요한 문자들 정의
WIKI_REMOVE_CHARS = re.compile("'+|(=+.{2,30}=+)|__TOC__|(ファイル:).+|:(en|de|it|fr|es|kr|zh|no|fi):|\n", re.UNICODE)
WIKI_SPACE_CHARS = re.compile("(\\s|゙|゚|　)+", re.UNICODE)   
EMAIL_PATTERN = re.compile("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", re.UNICODE)
URL_PATTERN = re.compile("(ftp|http|https)?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", re.UNICODE)
WIKI_REMOVE_TOKEN_CHARS = re.compile("(\\*$|:$|^파일:.+|^;)", re.UNICODE)
MULTIPLE_SPACES = re.compile(' +', re.UNICODE)

def tokenize(content, token_min_len=2, token_max_len=100, lower=True):
    ''' 
    특수문자, 공백, 이메일 주소, 웹 페이지 주소 등을 제거 
    '''
    content = re.sub(EMAIL_PATTERN, ' ', content)  # remove email pattern
    content = re.sub(URL_PATTERN, ' ', content) # remove url pattern
    content = re.sub(WIKI_REMOVE_CHARS, ' ', content)  # remove unnecessary chars
    content = re.sub(WIKI_SPACE_CHARS, ' ', content)   # remove space chars 
    content = re.sub(MULTIPLE_SPACES, ' ', content)   # remove multiple spaces 
    tokens = content.replace(", )", "").split(" ")   
    
    result = []
    for token in tokens:
        if not token.startswith('_'):   # token이 '_'로 시작하지 않으면 
            token_candidate = to_unicode(re.sub(WIKI_REMOVE_TOKEN_CHARS, '', token))
        else:   # token이 '_'로 시작하면 
            token_candidate = ""
        if len(token_candidate) > 0:
            result.append(token_candidate)
    return result