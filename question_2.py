import pandas
import pandas as pd


def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def add_vowels(column_title: str, df_to_calculate):
    df_to_calculate[f'{column_title}_vowel_count'] = df[column_title].apply(count_vowels)
    return (df_to_calculate)


if __name__ == '__main__':
    data = {'Column1': ['apple', 'banana', 'cherry'],
            'Column2': ['dog', 'elephant', 'fish'], }
    df = pd.DataFrame(data)
    vowel_counts_df = add_vowels("Column1", df)
    print(vowel_counts_df)
