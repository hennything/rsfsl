# Few-Shot Learning in Remote Sensing

## Running Repository
### Dependecies

* numpy
* python 3.8+
* pytorch
* tqdm
* pillow
* scikit-learn
* gpytorch
* pytest
* gputil

## Generating Experiments

Generate experiment scripts for training:
```
python generator.py --imbalanced_supports --results folder <dataset_name> --dataset <dataset_name>
```
Generate experiment scripts for testing:
```
python generator.py --imbalanced_supports --test --results folder <dataset_name> --dataset <dataset_name>
```
Generate experiment scripts for strategies:
```
python generator.py --imbalanced_supports --inference --results folder <dataset_name> --dataset <dataset_name>
```
