import csv
import random
from collections import defaultdict
from typing import Dict
from collections import Counter
from typing import List
from typing import NamedTuple
from scratch.linear_algebra import Vector, distance

class LabeledPoint(NamedTuple):
    point: Vector
    label: str

def raw_majority_vote(labels: List[str]) -> str:
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    return winner

assert raw_majority_vote(['a', 'b', 'c', 'b']) == 'b'

def majority_vote(labels: List[str]) -> str:
    """Assumes that labels are ordered from nearest to farthest."""
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count
                       for count in vote_counts.values()
                       if count == winner_count])

    if num_winners == 1:
        return winner  # unique winner, so return it
    else:
        return majority_vote(labels[:-1])  # try again without the farthest


# Tie, so look at first 4, then 'b'
assert majority_vote(['a', 'b', 'c', 'b', 'a']) == 'b'

def knn_classify(k: int,
                 labeled_points: List[LabeledPoint],
                 new_point: Vector) -> str:   # 5, air_train, air_point 값이 전달됨   (air_point = x값)
    # Order the labeled points from nearest to farthest.
    by_distance = sorted(labeled_points,
                         key=lambda lp: distance(lp.point, new_point))

    # Find the labels for the k closest
    k_nearest_labels = [lp.label for lp in by_distance[:k]]
    # print(majority_vote(k_nearest_labels))   better, good, normal ...
    # and let them vote.
    return majority_vote(k_nearest_labels)


def random_point(dim: int) -> Vector:
    return [random.random() for _ in range(dim)]


def random_distances(dim: int, num_pairs: int) -> List[float]:
    return [distance(random_point(dim), random_point(dim))
            for _ in range(num_pairs)]


def precision(tp: int, fp: int, fn: int, tn: int) -> float:
    return tp / (tp + fp)

assert precision(70, 4930, 13930, 981070) == 0.014

def recall(tp: int, fp: int, fn: int, tn: int) -> float:
    return tp / (tp + fn)

assert recall(70, 4930, 13930, 981070) == 0.005

def f1_score(tp: int, fp: int, fn: int, tn: int) -> float:
    p = precision(tp, fp, fn, tn)
    r = recall(tp, fp, fn, tn)

    return 2 * p * r / (p + r)

def print_precision_recall_f1_score(tp: int, fp:int, fn:int, tn: int, str):
    pre = precision(tp,fp,fn,tn)
    re = recall(tp,fp,fn,tn)
    f1 = f1_score(tp,fp,fn,tn)

    print(str,"의 precision:",pre,"recall:",re,"f1_score:",f1)


def main():
    def parse_air(row: List[str]) -> LabeledPoint:  # LabeledPoint 가 뭐야  - 위에 정의된 클래스 있음 (point = Vector, label = str)
            """
            sepal_length, sepal_width, petal_length, petal_width, class  - class는 우리가 원하는 결과 데이터
            """
            measurements = [float(value) for value in row[5:-1]]
            # class is e.g. "Iris-virginica"; we just want "virginica"
            label = row[-1]
            #print(measurements, label)
            # label 은 virignica 등 과제에서의 better, good, worse와 같은 값을 의미한다.
            return LabeledPoint(measurements, label)  # 배열, string 반환

    with open('./KNN/data2.csv') as f:
        reader = csv.reader(f)
        air_x = []
        air_y = []
        air_data = []
        # parse_air(row) # -> ['20180101','101', ... ,'0.003'] normal
        for i,row in enumerate(reader):
            #print(row)
            if i != 0:
                air_data.append(parse_air(row))
                #air_x.append(row[:-1])
                #air_y.append(row[-1])
        # print(air_x)
        # print(air_y)
        # print(air_data)   제대로 들어감

    points_by_species: Dict[str, List[Vector]] = defaultdict(list)
    for air in air_data:
        points_by_species[air.label].append(air.point)

    import random
    from scratch.machine_learning import split_data

    random.seed(12)
    air_train, air_test = split_data(air_data, 0.70)
    # assert len(iris_train) == 0.7 * 150
    # assert len(iris_test) == 0.3 * 150

    from typing import Tuple

    confusion_matrix: Dict[Tuple[str, str], int] = defaultdict(int)
    num_correct = 0
    num_wrong = 0

    for air in air_test:
       # print("air",air)
        predicted = knn_classify(5, air_train, air.point)
        actual = air.label

        if predicted == actual:    # num_correct = tp
            num_correct += 1
        elif predicted != actual:
            num_wrong += 1

        confusion_matrix[(predicted, actual)] += 1

    assert num_wrong == 3
    assert num_correct == 2258
    assert len(air_test) == 2261

    best_tp = 323; best_tn = 0; best_fp = 1; best_fn = 2261 - 324
    better_tp = 632; better_tn = 1; better_fp = 0; better_fn = 2261 - 633
    good_tp = 441; good_tn = 0; good_fp = 0; good_fn = 2261 - 441
    normal_tp = 318; normal_tn = 0; normal_fp = 0; normal_fn = 2261 - 318
    bad_tp = 405; bad_tn = 0; bad_fp = 0; bad_fn = 2261 - 405
    worse_tp = 106; worse_tn = 0; worse_fp = 0; worse_fn = 2261 - 106
    serious_tp = 33; serious_tn = 0; serious_fp = 2; serious_fn = 2261 - 35
    worst_tp = 0; worst_tn = 2; worst_fp = 0; worst_fn = 2261 - 2

    print_precision_recall_f1_score(best_tp, best_fp, best_fn, best_tn, "best")
    print_precision_recall_f1_score(better_tp, better_fp, better_fn, better_tn, "better")
    print_precision_recall_f1_score(good_tp,good_fp,good_fn,good_tn,"good")
    print_precision_recall_f1_score(normal_tp, normal_fp, normal_fn, normal_tn, "normal")
    print_precision_recall_f1_score(bad_tp, bad_fp, bad_fn, bad_tn, "bad")
    print_precision_recall_f1_score(worse_tp, worse_fp, worse_fn, worse_tn, "worse")
    print_precision_recall_f1_score(serious_tp,serious_fp,serious_fn, serious_tn,"serious")
    print("worst의 tp + fp = 0이기 때문에 precision을 구할 수 없고, recall은 0, f1_score 도 구할 수 없습니다.")

    #print(confusion_matrix)   # {('good','good'):441, ('better','better'): 632 ... ('best', 'better'):1}  - best, better는 실제값과 다르게 예측
    #print(confusion_matrix.get(('good','good')))

    #print(pct_correct, confusion_matrix)

    import tqdm
    dimensions = range(1, 101)

    avg_distances = []
    min_distances = []

    random.seed(0)

    for dim in tqdm.tqdm(dimensions, desc="Curse of Dimensionality"):
        distances = random_distances(dim, 10000)  # 10,000 random pairs
        avg_distances.append(sum(distances) / 10000)  # track the average
        min_distances.append(min(distances))  # track the minimum

    min_avg_ratio = [min_dist / avg_dist
                     for min_dist, avg_dist in zip(min_distances, avg_distances)]

#print("?")
if __name__ == "__main__": main()
#print("!")
