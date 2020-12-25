import pandas as pd
import numpy as np
a=[
    [1,2],
    [1,2],
    [1,2],
    [1,2],
    [2,3],
    [2,3],
    [2,4]
]
op=pd.DataFrame(a,columns=['a','b'])
# print(op)
# c=op.groupby('b').count().reset_index().sort_values(by='a',ascending=False)[:1]
# print(c.values[])
from collections import Counter
# from lib.constants import TOPFEATURES
import pandas as pd
import numpy as np
def _gen_top_feature(df: pd.DataFrame, attr: str, index_col: str):
    df = df[[index_col, attr]]
    stat_dic = {}
    stat_dic[attr]={}
    if df.dtypes[attr] == 'object':
        stat_df = df.groupby(attr).count().reset_index().sort_values(by=index_col, ascending=False)[: 1]
        most_value = stat_df[attr].values[0]
        size = stat_df[index_col].values[0]
        stat_dic[attr][most_value] = size
    else:
        stat_dic[attr]['mean'] = np.mean(df[attr])
    return stat_dic
def top_features(group_ret: dict, attrs: list, user_profile: pd.DataFrame):
    user_profile = user_profile[['sephora_user_id']+attrs]
    group_char = {}
    for k, v in group_ret.items():
        group_char['group' + str(k)] = {}
        group_char['group'+str(k)]['group_size'] = len(v)
        ret_df = pd.DataFrame()
        ret_df['sephora_user_id'] = v
        ret_df['gid'] = k
        ret_df = pd.merge(ret_df, user_profile, on='sephora_user_id', how='left')
        group_char['group' + str(k)]['top_features'] = {}
        for attr in attrs:
            attr_ret = _gen_top_feature(ret_df, attr, 'sephora_user_id')
            group_char['group'+str(k)]['top_features'].update(attr_ret)
    dump_json(group_char, TOPFEATURES)

a={'group1': {'group_size': 7050646, 'top_features': [{'most_visited_brand': {'ESTEELAUDER': 1122}}, {'most_visited_subcategory': {'FACECARE': 2730}}, {'online_abv': {'mean': 434.316338541085}}, {'makeup_item': {'mean': 0.7357451176437835}}, {'skincare_item': {'mean': 1.427483059730941}}, {'omni_abv': {'mean': 555.2101247041858}}, {'age': {'mean': 3.851828837129572}}, {'current_card_type': {'WHITE': 5143774}}, {'city_tier': {3.0: 30004}}]}, 'group2': {'group_size': 1302584, 'top_features': [{'most_visited_brand': {'ESTEELAUDER': 18573}}, {'most_visited_subcategory': {'FACECARE': 50480}}, {'online_abv': {'mean': 608.5992954902088}}, {'makeup_item': {'mean': 2.2654198121947866}}, {'skincare_item': {'mean': 5.664673253596811}}, {'omni_abv': {'mean': 719.2483553005462}}, {'age': {'mean': 37.22803378936876}}, {'current_card_type': {'BLACK': 708574}}, {'city_tier': {2.0: 702670}}]}, 'group3': {'group_size': 356958, 'top_features': [{'most_visited_brand': {'LANCOME': 41949}}, {'most_visited_subcategory': {'FACEMAKEUP': 84247}}, {'online_abv': {'mean': 630.6828234996796}}, {'makeup_item': {'mean': 4.638590422279295}}, {'skincare_item': {'mean': 10.154449918758845}}, {'omni_abv': {'mean': 733.6057246363135}}, {'age': {'mean': 30.15334743123176}}, {'current_card_type': {'BLACK': 183856}}, {'city_tier': {2.0: 168211}}]}, 'group4': {'group_size': 4503170, 'top_features': [{'most_visited_brand': {'ESTEELAUDER': 1691}}, {'most_visited_subcategory': {'FACECARE': 4410}}, {'online_abv': {'mean': 479.368316693518}}, {'makeup_item': {'mean': 1.1245421136154827}}, {'skincare_item': {'mean': 2.2018786765144553}}, {'omni_abv': {'mean': 594.6372362335693}}, {'age': {'mean': 30.91667225532236}}, {'current_card_type': {'WHITE': 2065048}}, {'city_tier': {3.0: 214318}}]}, 'group5': {'group_size': 15064570, 'top_features': [{'most_visited_brand': {'ESTEELAUDER': 1084}}, {'most_visited_subcategory': {'FACECARE': 2305}}, {'online_abv': {'mean': 431.684783511433}}, {'makeup_item': {'mean': 0.6278707311482925}}, {'skincare_item': {'mean': 0.8873710749484299}}, {'omni_abv': {'mean': 146.66666666666666}}, {'age': {'mean': 16.13065017682208}}, {'current_card_type': {'PINK': 15064570}}, {'city_tier': {1.0: 47032}}]}, 'group6': {'group_size': 1097852, 'top_features': [{'most_visited_brand': {'ESTEELAUDER': 8310}}, {'most_visited_subcategory': {'FACECARE': 26728}}, {'online_abv': {'mean': 579.3450034824866}}, {'makeup_item': {'mean': 2.8963066242857978}}, {'skincare_item': {'mean': 7.690388252959186}}, {'omni_abv': {'mean': 745.0427140671746}}, {'age': {'mean': 30.820196607180684}}, {'current_card_type': {'BLACK': 737883}}, {'city_tier': {2.0: 96890}}]}}
for key,value in a.items():
    temp={}
    for li in value['top_features']:
        temp.update(li)


    print(temp)

# unq, count = np.unique(df.fillna(-999), return_counts=1)
