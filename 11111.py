feature_columns=['age', 'gender', 'city', 'eb_customer_status', 'current_card_type', 'most_visited_category', 'most_visited_subcategory', 'most_visited_brand', 'preferred_category', 'preferred_subcategory', 'preferred_thirdcategory', 'preferred_brand', 'skin_type', 'makeup_maturity', 'skincare_maturity', 'makeup_price_range', 'skincare_price_range', 'skincare_demand', 'makeup_demand', 'fragrance_demand', 'purchase_recency', 'purchase_frequency', 'purchase_monetary', 'skincare_item', 'makeup_item', 'fragrance_item', 'category', 'subcategory', 'thirdcategory', 'target_gender', 'brand', 'skincare_function_basic', 'makeup_function', 'target_agegroup', 'skintype', 'fragrance_stereotype', 'if_bundle', 'order_cnt', 'conversion']
feat_importance={'brand': 1.0, 'most_visited_brand': 0.8157389635316699, 'most_visited_category': 0.6103646833013435, 'order_cnt': 0.5777351247600768, 'subcategory': 0.5163147792706334, 'most_visited_subcategory': 0.5124760076775432, 'category': 0.3915547024952015, 'thirdcategory': 0.3512476007677543, 'conversion': 0.18234165067178504, 'if_bundle': 0.1381957773512476, 'skincare_function_basic': 0.12667946257197696, 'target_gender': 0.09980806142034548, 'fragrance_stereotype': 0.08061420345489444, 'skincare_item': 0.07485604606525911, 'target_agegroup': 0.05758157389635317, 'current_card_type': 0.05182341650671785, 'preferred_brand': 0.036468330134357005, 'makeup_item': 0.026871401151631478, 'skintype': 0.02111324376199616, 'gender': 0.01727447216890595, 'fragrance_item': 0.01727447216890595, 'makeup_function': 0.01727447216890595, 'skincare_maturity': 0.011516314779270634, 'skincare_price_range': 0.005758157389635317, 'city': 0.003838771593090211, 'preferred_category': 0.003838771593090211, 'preferred_thirdcategory': 0.003838771593090211, 'makeup_maturity': 0.003838771593090211, 'age': 0.0019193857965451055, 'eb_customer_status': 0.0, 'preferred_subcategory': 0.0, 'skin_type': 0.0, 'makeup_price_range': 0.0, 'skincare_demand': 0.0, 'makeup_demand': 0.0, 'fragrance_demand': 0.0, 'purchase_recency': 0.0, 'purchase_frequency': 0.0, 'purchase_monetary': 0.0}

USER_ENCODE_COLS_RANKING = ['gender', 'city', 'eb_customer_status', 'current_card_type', 'most_visited_category',
                            'most_visited_subcategory', 'most_visited_brand', 'preferred_category',
                            'preferred_subcategory',
                            'preferred_thirdcategory', 'preferred_brand', 'skin_type', 'makeup_maturity',
                            'skincare_maturity',
                            'makeup_price_range', 'skincare_price_range', 'skincare_demand', 'makeup_demand',
                            'fragrance_demand',
                            'purchase_monetary']
# print(len(USER_ENCODE_COLS_RANKING))
# feature_importance = {k: v for k, v in feat.items() if
#                           k in USER_ENCODE_COLS_RANKING}
# print(list(feature_importance.keys())[:5])
# def gen_top_tags(feature_importance: dict, k: int = 5):
#     feature_importance = {k: v for k, v in feature_importance.items() if
#                           k in USER_ENCODE_COLS_RANKING}
#     return list(feature_importance.keys())[:k]
FIXED_TAGS=['most_visited_subcategory', 'current_card_type','skincare_demand']
def gen_top_tags(feature_importance: dict, k: int = 6,fixed_tags : bool = True):
    feature_importance = {k: v for k, v in feature_importance.items() if
                          k in USER_ENCODE_COLS_RANKING}
    if fixed_tags:
        for fix_tag in FIXED_TAGS:
            if fix_tag in list(feature_importance.keys())[:k]:
                k+=1
        return list(set(list(feature_importance.keys())[:k]).union(set(FIXED_TAGS)))
    return list(feature_importance.keys())[:k]
