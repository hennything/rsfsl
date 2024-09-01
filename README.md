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
Do this in the root directory.
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
## Running Experiments
To run an experiment go into the folder `<dataset_name>` and into the `baseline` folder. Find the `congig.json` file and copy the relative path as the `<path_to_config_file>`.
```
python src/main.py --args_file <path_to_config_file>
```
