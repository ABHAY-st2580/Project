from Database import get_connection
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules

def get_data():
    conn = get_connection()

    query = '''
    SELECT s.sale_id,
           si.tile_type,
           si.HL_L_D_F,
           si.tile_name_number
    FROM Sale s
    JOIN Sale_Items si ON s.sale_id = si.sale_id
    WHERE s.Date_ >= DATE_SUB(CURDATE(), INTERVAL 2 MONTH)
    '''

    df = pd.read_sql(query, conn)
    conn.close()

    df['item'] = (
            df['tile_type'].astype(str) + "_" +
            df['tile_name_number'].astype(str) + "_" +
            df['HL_L_D_F'].astype(str)
    )

    transactions = df.groupby('sale_id')['item'].apply(list).tolist()
    return transactions

def encode_transactions(transactions):
    te = TransactionEncoder()
    te_array = te.fit_transform(transactions)
    df = pd.DataFrame(te_array, columns=te.columns_)
    return df

def run_fpgrowth(encoded_df, min_support=0.2, min_confidence=0.6):

    frequent_itemsets = fpgrowth(
        encoded_df,
        min_support=min_support,
        use_colnames=True
    )

    rules = association_rules(
        frequent_itemsets,
        metric="confidence",
        min_threshold=min_confidence
    )

    return frequent_itemsets, rules

