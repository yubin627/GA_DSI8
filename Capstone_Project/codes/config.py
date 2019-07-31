# -*- coding: utf-8 -*-
# output folder path is defined within the notebeooks
# double-confirm the directory before running the notebook

GPU_ID = 0
TRAIN_BATCH_SIZE = 32
TEST_BATCH_SIZE = 32
TRIPLET_BATCH_SIZE = 32
EXTRACT_BATCH_SIZE = 128
TEST_BATCH_COUNT = 30
NUM_WORKERS = 4
LR = 0.0001
MOMENTUM = 0.5
EPOCH = 10
DUMPED_MODEL = "/floyd/input/models/model_10_final.pth.tar"

LOG_INTERVAL = 100
DUMP_INTERVAL = 500
TEST_INTERVAL = 100

DATASET_BASE = "/floyd/input/raw_deepfashion_dataset/raw_deepfashion_dataset" 
FEATURES_DIR = '/floyd/input/features_pca'
KMEANS_DIR = '/floyd/input/kmeans'
OUTPUT_DIR = 'output/'

#INSHOP_DATASET_PRESENT = 0.8
IMG_SIZE = 256
CROP_SIZE = 224
INTER_DIM = 512
CATEGORIES = 20
N_CLUSTERS = 100
COLOR_TOP_N = 10
TRIPLET_WEIGHT = 2.0
COLOR_WEIGHT = 0.1
DISTANCE_METRIC = ('euclidean','euclidean')
FREEZE_PARAM = True
