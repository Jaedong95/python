'''KcBERT 모델 Multi-GPU 사용하여 Testing 하기 '''
import os
import re
import numpy as np
import time 
from tqdm import tqdm
import tensorflow as tf
from transformers import *
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import pandas as pd
import matplotlib.pyplot as plt

def time_check_s():
    start = time.time()

    return start 

def time_check_e(time_s):
    print('time:', time.time() - time_s)
   

def default_setting():
    tf.random.set_seed(1234)
    np.random.seed(1234)


def args_setting():
    BATCH_SIZE = 64
    NUM_EPOCHS = 8
    VALID_SPLIT = 0.2
    MAX_LEN = 39 # EDA에서 추출된 Max Length
    
    return BATCH_SIZE, NUM_EPOCHS, VALID_SPLIT, MAX_LEN

def path_setting():
    DATA_IN_PATH = 'data_in/'
    DATA_OUT_PATH = "data_out/"
    DATA_TEST_PATH = os.path.join(DATA_IN_PATH, 'test.csv')
    ckpt_name = "bert_ckpt/v3"
    checkpoint_path = os.path.join(ckpt_name, 'bert_tensor-0003.ckpt')
    checkpoint_dir = os.path.dirname(checkpoint_path)

    return DATA_IN_PATH, DATA_OUT_PATH, DATA_TEST_PATH, checkpoint_path, checkpoint_dir 

def load_tokenizer():
    tokenizer = BertTokenizer.from_pretrained("bert-base-multilingual-cased", cache_dir='bert_ckpt', do_lower_case=False)
    
    return tokenizer

def bert_tokenizer(sent, tokenizer, MAX_LEN):
    encoded_dict = tokenizer.encode_plus(
        text = sent,
        add_special_tokens = True, # Add '[CLS]' and '[SEP]'
        max_length = MAX_LEN,           # Pad & truncate all sentences.
        pad_to_max_length = True,
        return_attention_mask = True   # Construct attn. masks.  
    )
    
    input_id = encoded_dict['input_ids']
    attention_mask = encoded_dict['attention_mask'] # And its attention mask (simply differentiates padding from non-padding).
    token_type_id = encoded_dict['token_type_ids'] # differentiate two sentences
    
    return input_id, attention_mask, token_type_id

class TFBertClassifier(tf.keras.Model):
    def __init__(self, model_name, dir_path, num_class):
        super(TFBertClassifier, self).__init__()

        self.bert = TFBertModel.from_pretrained(model_name, cache_dir=dir_path)
        self.dropout = tf.keras.layers.Dropout(self.bert.config.hidden_dropout_prob)
        self.classifier = tf.keras.layers.Dense(num_class, 
                                                kernel_initializer=tf.keras.initializers.TruncatedNormal(self.bert.config.initializer_range), 
                                                name="classifier",activation='sigmoid')
        
    def call(self, inputs, attention_mask=None, token_type_ids=None, training=False):
        #outputs 값: # sequence_output, pooled_output, (hidden_states), (attentions)
        outputs = self.bert(inputs, attention_mask=attention_mask, token_type_ids=token_type_ids)
        pooled_output = outputs[1] 
        pooled_output = self.dropout(pooled_output, training=training)
        logits = self.classifier(pooled_output)

        print(logits)
        return logits


def get_categories():
    categories = ['부정','긍정']
    
    return categories

def md_test(b_size, checkpoint_path, data_out_path, data_test_path, max_length, tokenizer):
    test_data = pd.read_csv(data_test_path, header = 0)
    test_data = test_data.dropna()
    test_data.head()

    input_ids = []
    attention_masks = []
    token_type_ids = []
    test_data_labels = []

    for test_sent, test_label in tqdm(zip(test_data["document"], test_data["label"]), total=len(test_data)):
        try:
            input_id, attention_mask, token_type_id = bert_tokenizer(test_sent, tokenizer, max_length)
            input_ids.append(input_id)
            attention_masks.append(attention_mask)
            token_type_ids.append(token_type_id)
            test_data_labels.append(test_label)

        except Exception as e:
            print(e)
            print(test_sent)
            pass
        
    test_md_input_ids = np.array(input_ids, dtype=int)
    test_md_attention_masks = np.array(attention_masks, dtype=int)
    test_md_type_ids = np.array(token_type_ids, dtype=int)
    test_md_inputs = (test_md_input_ids, test_md_attention_masks, test_md_type_ids)
    test_data_labels = np.asarray(test_data_labels, dtype=np.int32) #레이블 토크나이징 리스트

    '''
    Max length = 39
    input_id = test_md_input_ids[1]
    attention_mask = test_md_attention_masks[1]
    token_type_id = test_md_type_ids[1]

    print(input_id)
    print(attention_mask)
    print(token_type_id)
    print(tokenizer.decode(input_id))
    print("# sents: {}, # labels: {}".format(len(test_md_input_ids), len(test_data_labels)))
    '''
    # Multi-GPU 사용 
    strategy = tf.distribute.MirroredStrategy()
    
    with strategy.scope():
        md_model = TFBertClassifier(model_name='bert-base-multilingual-cased',
                                    dir_path='bert_ckpt', num_class=2)
        optimizer = tf.keras.optimizers.Adam(3e-5)
        loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
        metric = tf.keras.metrics.SparseCategoricalAccuracy('accuracy')
        md_model.compile(optimizer=optimizer, loss=loss, metrics=[metric])
        md_model.load_weights(checkpoint_path)
    
    results = md_model.evaluate(test_md_inputs, test_data_labels, batch_size=b_size)
    pre = md_model.predict(test_md_inputs)
    
    md_p = []; score = []; md_categories = []
    md_categories = get_categories()

    for i, p in enumerate(pre):
        max_p = max(p)
        y = p.argmax()
        md_p.append(md_categories[y])
        score.append(round(max_p * 100,2))
      
    test_data['predict'] = md_p
    test_data['score'] = score 
    test_data.to_csv(os.path.join(data_out_path,'csv','senti_mul_v11.csv'),index=False, encoding='utf-8-sig')
    print(test_data.head())
    print("test loss, test acc: ", results)


if __name__ == '__main__':
    time_s = time_check_s()
    default_setting()

    b_size, num_epochs, val_split, max_length = args_setting()
    data_in_path, data_out_path, data_test_path, ckpt_path, ckpt_dir = path_setting()
    tokenizer = load_tokenizer()
    md_test(b_size,ckpt_path, data_out_path, data_test_path, max_length, tokenizer)

    time_check_e(time_s)