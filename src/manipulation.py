import pandas as pd


def manipular_dados():

    df = pd.read_json('clean/data.json', lines=True)

    df_agg = df.groupby('Country').agg(
        sum_price=('price', 'sum'),
        avg_price=('price', 'mean'),
        min_price=('price', 'min'),
        max_price=('price', 'max')
    )

    print(df_agg)

    contagem = df['payment_method'].value_counts()
    print(contagem)

    #print(df)


if __name__ == '__main__':
    manipular_dados()