# Remove_duplicates
Task DA-1-10 for NSU "Project Introduction" course

## Task description
Find and remove duplicate rows.

## Guideline (Original Task Requirements)
1. Create duplicates in the dataset.
2. Find them using duplicated().
3. Remove them using drop_duplicates().
4. Check the number of rows before and after.

## Features
- **Duplicate Detection**: Uses pandas `duplicated()` method to identify duplicate rows
- **Duplicate Removal**: Uses pandas `drop_duplicates()` method to remove duplicates
- **Flexible Options**: Supports different strategies for keeping duplicates ('first', 'last', or removing all)
- **Statistics**: Provides detailed statistics about the cleaning process
- **Test Data Generation**: Includes utility to create sample datasets with duplicates for testing
- **Error Handling**: Comprehensive validation and error handling
- **Demo Functionality**: Complete demonstration using the Iris dataset

## Functions


### `remove_duplicates_from_dataframe(dataframe, keep="first", verbose=False)`
Removes duplicate rows from a pandas DataFrame and returns statistics.

**Parameters:**
- `dataframe` (pd.DataFrame): Input DataFrame to process
- `keep` (str): Which duplicates to keep. Options: 'first', 'last', False
  - `'first'`: Keep first occurrence, remove subsequent duplicates (default)
  - `'last'`: Keep last occurrence, remove previous duplicates
  - `False`: Remove all duplicates
- `verbose` (bool): If True, print detailed statistics

**Returns:**
- `pd.DataFrame`: Cleaned DataFrame with duplicates removed

**Raises:**
- `ValueError`: If input or output parameters are invalid


### `create_sample_duplicates(dataframe, num_duplicates, random_seed=42, replace=False)`
Creates a sample dataset with duplicates for testing purposes.

**Parameters:**
- `dataframe` (pd.DataFrame): Original DataFrame
- `num_duplicates` (int): Number of duplicate rows to create
- `random_seed` (int): Random seed for reproducibility (default: 42)
- `replace` (bool): Whether to allow duplicates when sampling (default: False)

**Returns:**
- `pd.DataFrame`: DataFrame with duplicates added

**Raises:**
- `ValueError`: If num_duplicates is invalid


### `main()`
Demonstrates the duplicate removal functionality using the Iris dataset from scikit-learn.

**Features:**
- Loads the Iris dataset (150 samples, 4 features)
- Creates 40 duplicate rows for demonstration
- Removes duplicates with verbose statistics
- Shows before/after dataset shapes


## Running the Demo
```bash
python duplicate_remover.py
```

## Dependencies
- `numpy`: For random number generation
- `pandas`: For DataFrame operations
- `scikit-learn`: For sample dataset (Iris)

## Installation
```bash
pip install numpy pandas scikit-learn
```

## Implementation Details
The implementation follows pandas best practices:
- Uses `dataframe.duplicated(keep=keep)` to identify duplicates
- Uses `dataframe.drop_duplicates(keep=keep)` to remove them
- Provides comprehensive validation and error handling
- Includes detailed statistics and logging capabilities
- Supports reproducible results through random seed control

## Materials
- [Pandas Duplicates Documentation](https://pandas.pydata.org/docs/user_guide/duplicates.html)
- [NumPy Random Generator](https://numpy.org/doc/stable/reference/random/generator.html)
- [Scikit-learn Iris Dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html)
