import numpy as np
import pandas as pd
from sklearn.datasets import load_iris


def remove_duplicates_from_dataframe(
    dataframe: pd.DataFrame,
    keep: str = "first",
    verbose: bool = False
) -> pd.DataFrame:
    """
    Remove duplicate rows from a pandas DataFrame and return statistics.
    
    Args:
        dataframe (pd.DataFrame): Input DataFrame to process
        keep (str): Which duplicates to keep. Options: 'first', 'last', False
        verbose (bool): If True, print detailed statistics

    Returns:
        pd.DataFrame: cleaned DataFrame
        
    Raises:
        ValueError: If input or output parameters are invalid
    """

    if keep not in ['first', 'last', False]:
        raise ValueError("keep parameter must be 'first', 'last', or False")

    num_rows_original = len(dataframe)
    
    # Find duplicates
    duplicate_mask = dataframe.duplicated(keep=keep)
    num_duplicates_found = duplicate_mask.sum()
    
    # Remove duplicates
    cleaned_df = dataframe.drop_duplicates(keep=keep) 
    num_rows_after = len(cleaned_df)
    
    # Validation
    if num_rows_after > num_rows_original:
        raise ValueError("Number of rows after cleaning cannot be greater than original")
    
    if verbose:
        print("\nDuplicate removal statistics:")
        print(f"Original rows: {num_rows_original}")
        print(f"Duplicates found: {int(num_duplicates_found)}")
        print(f"Rows after cleaning: {num_rows_after}\n")
    
    return cleaned_df


def create_sample_duplicates(
    dataframe: pd.DataFrame,
    num_duplicates: int,
    random_seed: int = 42,
    replace: bool = False
) -> pd.DataFrame:
    """
    Create a sample dataset with duplicates for testing purposes.
    
    Args:
        dataframe (pd.DataFrame): Original DataFrame
        num_duplicates (int): Number of duplicate rows to create
        random_seed (int): Random seed for reproducibility
        replace (bool): Whether to allow duplicates
        
    Returns:
        pd.DataFrame: DataFrame with duplicates added
        
    Raises:
        ValueError: If num_duplicates is invalid
    """
    
    if num_duplicates < 0:
        raise ValueError("Number of duplicates must be non-negative")
    
    if num_duplicates > len(dataframe):
        raise ValueError("Number of duplicates cannot exceed original DataFrame size")
    
    if num_duplicates == 0:
        return dataframe.copy()
    
    # Create duplicates
    rng = np.random.default_rng(random_seed)
    duplicate_indices = rng.choice(dataframe.index, size=num_duplicates, replace=replace)
    df_with_duplicates = pd.concat([dataframe, dataframe.loc[duplicate_indices]], ignore_index=True)
    
    return df_with_duplicates


def main():
    """Demonstrate the duplicate removal functionality using the Iris dataset."""
    
    try:
        # Load sample data
        iris_data = load_iris()
        dataframe = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
        
        print("=== Duplicate Removal Demo ===")
        print(f"Original dataset shape: {dataframe.shape}")
        
        # Create duplicates for demonstration
        df_with_duplicates = create_sample_duplicates(dataframe, num_duplicates=40)
        print(f"Dataset with duplicates shape: {df_with_duplicates.shape}")
        
        # Remove duplicates
        cleaned_df = remove_duplicates_from_dataframe(df_with_duplicates, verbose=True)
        print(f"Cleaned dataset shape: {cleaned_df.shape}")

        print("=== Demo completed successfully! ===")
        
    except Exception as e:
        print(f"Error in main function: {e}")
        raise

if __name__ == "__main__":
    main()