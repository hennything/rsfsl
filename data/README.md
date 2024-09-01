## Create from a class subdirectory structure
The images should be contained in class subfolders, and the class subfolders contained in: ```train/```, ```val/``` and ```test/``` folders.
```
.<DATASET>/
└── raw/
    ├── train/
    |
    ├── test/
    |
    └── val/

```
where `<DATASET>` is `ucmerced`.

To create dataset from the subdirectories run:
```
create_cache_from_folders.py `<DATASET>`
```
