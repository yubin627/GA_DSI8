# -*- coding: utf-8 -*-

from config import *
import os
import random
import pandas as pd

def Eval(head=False):

    path = os.path.join(LIST_DIR, "Eval/list_eval_partition.txt")
    data = pd.read_csv(path, delim_whitespace=True, skiprows=[0], header=0) 
    if head:
        return data.head(100)
    return data


def Anno(is_train=True, head=False):

    category_path = os.path.join(LIST_DIR, "Anno/list_category_img.txt")
    category_data = pd.read_csv(category_path, delim_whitespace=True, skiprows=[0], header=0)
    category_data = category_data[category_data['category_label'] < 21] #limit to upper wear
    eval_data = Eval(head=head)

    if is_train:
        category_data = pd.merge(category_data, eval_data[eval_data['evaluation_status'] == 'train'], how='inner',
                                 on=['image_name'])
    else:
        category_data = pd.merge(category_data, eval_data[eval_data['evaluation_status'] == 'test'], how='inner',
                                 on=['image_name'])
    category_data.drop('evaluation_status', 1)

    if head:
        return category_data.head(100)
    return category_data
