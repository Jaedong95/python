'''
ELMo 입력 ID 시퀀스 만들기 
'''
import numpy as np 

class UnicodeCharsVocabulary(Vocabulary):
    def __init__(self, filename, max_word_length, **kwargs):
        super(UnicodeCharsVocabulary, self).__init__(filename, **kwargs)
        self._max_word_length = max_word_length
        self.bos_char = 256 # <begin sentence>
        self.eos_char = 257 # <end sentence>
        self.bow_char = 258 # <begin word> 
        self.eow_char = 259 # <end word> 
        self.pad_char = 260 # <padding> 
    
    def _convert_word_to_char_ids(self, word):
        code = np.zeros([self.max_word_length], dtype=np.int32)
        code[:] = self.pad_char 
        word_encoded = word.encode('utf-8', 'ignore')[:(self.max_word_length-2)]
        code[0] = self.bow_char
        for k, chr_id in enumerate(word_encoded, start=1):
            code[k] = chr_id 
        code[len(word_encoded) + 1] = self.eow_char
        return code 