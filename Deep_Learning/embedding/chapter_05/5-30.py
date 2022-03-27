'''
ELMo 하이퍼파라미터 설정 
'''
options = {
    'bidirectional': True,
    'char_cnn': {'activation': 'relu',   # 활성함수 종류 
    # 문자 단위 컨볼루션 레이어의 문자별 임베딩 행렬의 차원 수 
                    'embedding': {'dim': 16},  
                    'filters': [[1, 32],
                                [2, 32],
                                [3, 64],
                                [4, 128],
                                [5, 256],
                                [6, 512],
                                [7, 1024]],
                    # 한 토큰에 최대 몇 개의 문자 입력할지 결정 
                    'max_characters_per_token': 30,
                    'n_characters': 261,   # 사용하는 문자 종류 개수 
                    'n_highway': 2},   # 하이웨이 네트워크 적용 횟수 
    'dropout': 0.1,
    'lstm': {
        'cell_clip': 3,   # LSTM 셀의 값 제한 크기 
        'dim': 1024,   # 각 셀의 입출력 벡터 차원 수 
        'n_layers': 2,   # 양방향 레이어 개수 
        'proj_clip': 3,   # LSTM 셀의 값 제한 크기 
        'projection_dim': 128,   # 각 셀의 입출력 벡터 차원 수 
        'use_skip_connections': True},   # 그래디언트 소실 방지 
    'all_clip_norm_val': 10.0,   # 역전파 그래디언트 크기 
    'n_epochs': 10,   # 학습 횟수 
    'n_train_tokens': n_train_tokens,   # 에폭 수를 정할 때 참고하는 크기 
    'batch_size': batch_size,   # 배치 데이터 크기 
    'n_tokens_vocab': vocab.size,   # 어휘집합 크기 
    'unroll_steps': 20,   # 몇 개의 단어 시퀀스 예측할지 설정 
    'n_negative_samples_batch': 8192,   # 한 스텝에서 계산하는 네거티브 샘플 수 
}