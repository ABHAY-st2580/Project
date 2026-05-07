from django.shortcuts import render
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Sale.models import Sale, SaleItem



def get_data():
    sales = Sale.objects.all()
    transactions = []

    for sale in sales:
        items = SaleItem.objects.filter(sale=sale)

        transaction = []

        for item in items:
            tile_type = item.tile_type or ''
            tile_name = item.tile_name_number or ''
            category = item.tile_type2 or ''

            combined = f"{tile_type}_{tile_name}_{category}".strip("_")

            if combined:
                transaction.append(combined)

        if transaction:
            transactions.append(transaction)

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

@csrf_exempt
def get_recommendations(request):
  if request.method == "POST":
    data = json.loads(request.body)
    min_support = data.get("min_support", 0.2)
    min_confidence = data.get("min_confidence", 0.6)
    try:
        transactions = get_data()
        encoded = encode_transactions(transactions)
        _, rules = run_fpgrowth(encoded, min_support=min_support, min_confidence=min_confidence)

        result = []

        for _, row in rules.iterrows():
            result.append({
                "if_bought": list(row['antecedents']),
                "then_buy": list(row['consequents']),
                "confidence": float(row['confidence'])
            })

        return JsonResponse({"rules": result})

    except Exception as e:
        return JsonResponse({"error": str(e)})
  else:
    return JsonResponse({"error": "Not a post request"})



    