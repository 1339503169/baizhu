res = []
        print('generate group items')
        for group, users in group_item.group2users.items():
            users_ = list(set(users).intersection(group_item.active_users))
            print('group{} has {} active users'.format(group,len(users_)))
            for icon, items in group_item.icon2items.items():
                print('group', group, 'icon', icon, 'user', len(users_), 'item', len(items))
                # group 0 icon lip_stick user 53213 item 100
                index_df = gen_pred_index(users_, items)
                pred_df = gen_data_set(index_df, group_item.ranking_user_df, group_item.ranking_item_df)
                pred_ret = group_item.model.predict(pred_df)
                pred_ret = pred_ret.sort_values(by=['sephora_user_id', 'prediction'], ascending=[True, False])
                print(pred_ret)
                pred_ret = pred_ret.groupby('sephora_user_id')['op_code'].apply(
                    lambda x: x.tolist()[:group_item.user_item_cnt]).reset_index()
                item_res = []
                for item_ in pred_ret['op_code']:
                    item_res.extend(item_)
                print('total item number', len(item_res), 'unique item number', len(set(item_res)))
                item_cnt = Counter(item_res).most_common(group_item.group_icon_item_cnt)
                top_items = [_[0] for _ in item_cnt]
                top_sku = [group_item.op2sku[op] for op in top_items if op in group_item.op2sku.keys()]
                res.append([group, group_item.icon_name2id[icon], ','.join(top_sku)])
        print('generate default res')
        for icon, item in tqdm(group_item.icon2items.items()):
            print('group', group_item.default_group_id, 'icon', icon)
            sku = [group_item.op2sku[op] for op in item if op in group_item.op2sku.keys()]
            res.append([str(group_item.default_group_id), group_item.icon_name2id[icon], ','.join(sku[:group_item.group_icon_item_cnt])])
        res_df = pd.DataFrame(data=res, columns=['group_id', 'icon_id', 'sku_list'])
        res_df = res_df.astype(dtype={'group_id': int, 'icon_id': int})
        res_df['insert_date'] = date.today()
        print('save res')