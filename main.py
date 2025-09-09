import numpy as np
import pandas as pd
from sklearn.datasets import load_iris


def main():
    # 1) Load data
    db = load_iris()
    df = pd.DataFrame(data=db.data, columns=db.feature_names)
    df["target"] = db.target
    num_rows_orig = len(df)

    # 2) Create duplicates in dataset
    num_dup = 40
    random_key = 42
    dup_indices = np.random.default_rng(random_key).choice(df.index, size=num_dup, replace=False)
    df_with_dupes = pd.concat([df, df.loc[dup_indices]], ignore_index=True)

    # 3) Find duplicates with duplicated()
    dup_mask = df_with_dupes.duplicated(keep="first")
    num_rows_before = len(df_with_dupes)
    num_dup_found = dup_mask.sum()

    # 4) Delete duplicates with drop_duplicates()
    df_deduped = df_with_dupes.drop_duplicates(keep="first")
    num_rows_after = len(df_deduped)

    # 5) Check amount of rows before and after
    print("Iris rows (original):", num_rows_orig)
    print("Iris rows after adding duplicates:", num_rows_before)
    print("Number of duplicate rows detected (via duplicated()):", int(num_dup_found))
    print("Rows after drop_duplicates():", num_rows_after)

    # Sanity check
    assert num_rows_after <= num_rows_orig

if __name__ == "__main__":
    main()