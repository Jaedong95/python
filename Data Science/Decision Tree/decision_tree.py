from typing import List
import math

def entropy(class_probabilites: List[float])  -> float:
    return sum(-p * math.log(p, 2)
               for p in class_probabilites
               if p > 0)


from typing import Any
from collections import Counter

def class_probabilities(labels: List[Any]) -> List[float]:
    total_count = len(labels)
    return [count / total_count
            for count in Counter(labels).values()]

def data_entropy(labels: List[Any]) -> float:
    return entropy(class_probabilities(labels))


def partition_entropy(subsets: List[List[Any]]) -> float:
    total_count = sum(len(subset) for subset in subsets)

    return sum(data_entropy(subset) * len(subset) / total_count
               for subset in subsets)


from typing import NamedTuple, Optional

class Candidate(NamedTuple):
    lang: str
    tweets: bool
    phd: bool
    did_well: bool
    level: Optional[str] = None

inputs = [Candidate('Java', False, False, False, 'Senior'),
          Candidate('Java', False, True, False, 'Senior'),
          Candidate('Python', False, False, True, 'Mid'),
          Candidate('Python', False, False, True, 'Junior'),
          Candidate('R', True, False, True, 'Junior'),
          Candidate('R', True, True, False, 'Junior'),
          Candidate('R', True, True, True, 'Mid'),
          Candidate('Python', False, False, False, 'Senior'),
          Candidate('R', True, False, True, 'Senior'),
          Candidate('Python', True, False, True, 'Junior'),
          Candidate('Python', True, True, True, 'Senior'),
          Candidate('Python', False, True, True, 'Mid'),
          Candidate('Java', True, False, True, 'Mid'),
          Candidate('Python', False, True, False, 'Junior')
          ]

from typing import Dict, TypeVar
from collections import defaultdict

T = TypeVar('T')

def partition_by(inputs: List[T], attribute: str) -> Dict[Any, List[T]]:
    partitions: dict[Any, List[T]] = defaultdict(list)   # partition 이라는 이름의 빈 Dictionary를 만듬
    for input in inputs:
        #print("inputs:", inputs, "input:", input)
        key = getattr(input, attribute)    # input에서, attribute에 해당하는 (level) 값을 key로 설정
        partitions[key].append(input)
    return partitions   # key 값에 따라 파티션이 생성되어 반환됨


def partition_entropy_by(inputs: List[Any], attribute: str, label_attribute: str) -> float:  # label_attribute = 예측하려고 하는 값 (True, False)
    partitions = partition_by(inputs, attribute)

    labels = [[getattr(input, label_attribute) for input in partition]
              for partition in partitions.values()]

    return partition_entropy(labels)
# partition_by에 의해 나눠진 파티션들의 레이블 값의 합을 반환함

for key in ['lang', 'tweets', 'phd','did_well']:
    print(key, partition_entropy_by(inputs, key, 'level'))
print()    # did_well = 1.33, lang = 1.40, tweets = 1.55, phd = 1.57

#senior_inputs = [(input, label)
 #                for input, label in inputs if input['level'] == 'Senior']

#print(inputs)

true_inputs = []
for a in inputs:
    # print(a)
    if a[3] == True:
        true_inputs.append(a)
        #print("true_inputs", true_inputs)
    #print("inputs print: ",a[0])

for key in ['lang', 'tweets', 'phd']:
    print(key, partition_entropy_by(true_inputs, key, 'level'))
print()   # lang = 1.37 tweets = 1.36 phd = 1.27


from typing import NamedTuple, Union, Any

class Leaf(NamedTuple):
    Value: Any

class Split(NamedTuple):
    attribute:str
    subtrees: dict
    default_value: Any = None

DecisionTree = Union[Leaf, Split]

hiring_tree = Split('did_well', {
    True: Split('phd', {
        False:Leaf('Senior'),
        True:Leaf('Junior')
    }),
    False: Split('tweets', {
        False: Leaf('Mid'),
        True: Leaf('Junior')
    })
})

#  나무를 이용한 input의 분류를 수행하는데, input이 기존에 없는 값이라면 none (기본값)으로 분류
def classify(tree: DecisionTree, input: Any) -> Any:
    if isinstance(tree, Leaf):   # tree가 Leafnode 이면 value 반환
        return tree.Value

    subtree_key = getattr(input, tree.attribute)

    if subtree_key not in tree.subtrees:
        return tree.default_value   # none

    subtree = tree.subtrees[subtree_key]
    return classify(subtree, input)


res = classify(hiring_tree, Candidate)
print('classification', res)

def build_tree_id3(inputs: List[Any],
                   split_attributes: List[str],
                   target_attribute: str) -> DecisionTree:

    # target attribute의 값의 종류가 몇 개 있는지 따져봄
    label_counts = Counter(getattr(input, target_attribute)
                           for input in inputs)

    most_common_label = label_counts.most_common(1)[0][0]

    # id3 알고리즘의 특징
    if len(label_counts) == 1: # unique label이 존재한다면
        return Leaf(most_common_label)

    if not split_attributes:   # 더 이상 분할할 attribute가 없다면
        return Leaf(most_common_label)

    def split_entropy(attribute: str) -> float:
        return partition_entropy_by(inputs, attribute, target_attribute)

    # split_entropy가 가장 작게 나오는 attribute를 best_attribute로 설정
    best_attribute = min(split_attributes, key=split_entropy)

    partitions = partition_by(inputs, best_attribute)

    # attribute를 하나 줄어야 하기 때문에, best_attribute가 아닌 attribute들로 새로운 attribute를 구성
    new_attributes = [a for a in split_attributes if a != best_attribute]

    # best_attribute를 통해 만든 partition의 item (집합  - attribute_value와 subset으로 구성) 을 가지고, 다시 subtree를 만듬
    subtrees = {attribute_value : build_tree_id3(subset, new_attributes, target_attribute)
                for attribute_value, subset in partitions.items()}

    return Split(best_attribute, subtrees, default_value=most_common_label)

tree = build_tree_id3(inputs, ['did_well','lang','tweets','phd'], 'level')

print("lang: Java, tweets: True, phd: False, did_well: True 일 때의 분류 결과: ", classify(tree, Candidate('Java', True, False, True)))

print("lang: Python, tweets: False, phd: False, did_well: False 일 때의 분류 결과: ",classify(tree, Candidate('Python', False, False, False)))

