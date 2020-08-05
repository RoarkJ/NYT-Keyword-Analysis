import pandas as pd

def count_keywords(year, keywords_category, keyword_list_to_match):
    df=pd.read_csv(f'Data/{year}_dates_and_keyword.csv')
    df.sort_values('publication_date', inplace=True)
    df_to_match_kw=pd.read_csv(keyword_list_to_match)
    keyword_list=[rows['Keyword Names'] for index, rows in df_to_match_kw.iterrows()]
    keyword_match_df=pd.DataFrame(df.loc[df['keywords'].isin(keyword_list)])
    keywords_counts=pd.DataFrame(keyword_match_df['publication_date'].value_counts())
    keywords_counts.rename(columns={'publication_date': 'keywords_count'}, inplace=True)
    keywords_counts.sort_index(inplace=True)
    keywords_counts=keywords_counts.reset_index()
    keywords_counts.rename(columns={'index': 'publication_date'}, inplace=True)
    keywords_counts.to_csv(f'Data/{keywords_category}_{year}_keywords_counts.csv', index=False)