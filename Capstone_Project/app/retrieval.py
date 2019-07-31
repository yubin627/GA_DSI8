# -*- coding: utf-8 -*-

import os
import sys
import numpy as np
from scipy.spatial.distance import cdist
from config import *

def read_lines(path):
    with open(path) as fin:
        lines = fin.readlines()[2:]
        lines = list(filter(lambda x: len(x) > 0, lines))
        names = list(map(lambda x: x.strip().split()[0], lines))
    return names

def load_feat_db():
    feat_all = os.path.join(FEATURES_DIR, 'all_feat_pca.npy')
    feat_list = os.path.join(FEATURES_DIR, 'all_feat.list')
    color_feat = os.path.join(FEATURES_DIR, 'all_color_feat.npy')
    if not os.path.isfile(feat_list) or not os.path.isfile(feat_all) or not os.path.isfile(color_feat):
        print("No feature db file! Please run feature_extractor.py first.")
        return
    deep_feats = np.load(feat_all)
    color_feats = np.load(color_feat)
    with open(feat_list) as f:
        labels = list(map(lambda x: x.strip(), f.readlines()))
    return deep_feats, color_feats, labels


def get_top_n(dist, labels, retrieval_top_n):
    ind = np.argpartition(dist, retrieval_top_n)[0:retrieval_top_n]
    ret = list(zip([labels[i] for i in ind], dist[ind]))
    ret = sorted(ret, key=lambda x: x[1], reverse=False)
    return ret


def get_similarity(feature, feats, metric='cosine'):
    dist = cdist(np.expand_dims(feature, axis=0), feats, metric)[0]
    return dist


def get_deep_color_top_n(features, deep_feats, color_feats, labels, retrieval_top_n=5):
    deep_scores = get_similarity(features[0], deep_feats, DISTANCE_METRIC[0])
    color_scores = get_similarity(features[1], color_feats, DISTANCE_METRIC[1])
    results = get_top_n(deep_scores + color_scores * COLOR_WEIGHT, labels, retrieval_top_n)
    return results

def naive_query(features, deep_feats, color_feats, labels, retrieval_top_n=5):
    results = get_deep_color_top_n(features, deep_feats, color_feats, labels, retrieval_top_n)
    return results

def dump_single_feature_npy(img_path):
    deep_feats, color_feats, labels = load_feat_db()
    
    deep_feats = np.array(deep_feats)
    color_feats = np.array(color_feats)
    labels = np.array(labels)

    deep_feat = deep_feats[labels == img_path][0,:]
    color_feat = color_feats[labels == img_path][0,:]

    return deep_feat, color_feat
