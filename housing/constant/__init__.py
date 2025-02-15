import os,sys
from datetime import datetime

ROOT_DIR = os.getcwd()
CONFIG_DIR_NAME = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR_NAME,CONFIG_FILE_NAME)
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
MODEL_FILE_PATH = "model.yaml"

## Constant for Training Pipeline
TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
PIPELINE_NAME = "pipeline_name"
ARTIFACT_DIR = "artifact_dir"

## Data Ingestion Constants:-

DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR_NAME = "data_ingestion"
DATA_INGESTION_DATASET_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = "tgz_download_dir"
DATA_INGESTION_INGESTED_DIR_KEY = "ingested_dir"
DATA_INGESTION_INGESTED_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_INGESTED_TEST_DIR_KEY = "ingested_test_dir"

## Data Validation Constants:-

DATA_VALIDATION_CONFIG_KEY = "data_validation_config"
DATA_VALIDATION_ARTIFACT_DIR_NAME = "data-validation"
DATA_VALIDATION_SCHEMA_DIR_KEY = "schema_dir"
DATA_VALIDATION_SCHEMA_FILE_NAME = "schema_file_name"
DATA_VALIDATION_REPORT_FILE_NAME = "report_file_name"
DATA_VALIDATION_REPORT_PAGE_FILE_NAME = "report_page_file_name"

## Data Transformation Constants:-

DATA_TRANSFORMATION_CONFIG_KEY = "data_transformation_config"
ADD_BEDROOM_PER_ROOM_KEY ="add_bedroom_per_room"
DATA_TRANSFORMATION_ARTIFACT_DIR_NAME = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DIR_NAME_KEY = "transformed_dir"
DATA_TRASFORMATION_TRAIN_DIR_NAME_KEY = "transformed_train_dir"
DATA_TRASFORMATION_TEST_DIR_NAME_KEY = "transformed_test_dir"
DATA_TRANSFORMATION_PREPROCESSING_DIR_KEY = "preprocessing_dir"
DATA_TRANSFORMATION_PREPROCESSING_OBJECT_FILE_NAME_KEY = "preprocessed_object_file_name"

## Schema file constants

COLUMN_TOTAL_ROOMS = "total_rooms"
COLUMN_POPULATION = "population"
COLUMN_HOUSEHOLDS = "households"
COLUMN_TOTAL_BEDROOM = "total_bedrooms"
NUMERICAL_COLUMN_KEY = "numerical_columns"
CATEGORICAL_COLUMN_KEY = "categorical_columns"
TARGET_COLUMN_KEY = "target_column"
DATASET_SCHEMA_COLUMNS_KEY = "columns"

## Model Training Constants :- 
MODEL_TRAINER_CONFIG_ARIFACT_DIR = "model_trainer"
MODEL_TRAINER_CONFIG_KEY = "model_trainer_config"
MODEL_TRAINER_TRAINED_MODEL_DIR_KEY = "trained_model_dir"
MODEL_TRAINER_MODEL_FILE_NAME_KEY = "model_file_name"
MODEL_TRAINER_BASE_ACCURACY_KEY = 0.6

## Model Evaluation Constants :-
MODEL_EVALUATION_ARTIFACT_DIR_NAME = "model_evaluation"
MODEL_EVALUATION_CONFIG_KEY = "model_evaluation_config"
MODEL_EVALUATION_FILE_NAME_KEY = "model_evaluation_file_name"


BEST_MODEL_KEY = "best_model"
HISTORY_KEY = "history"
MODEL_PATH_KEY = "model_path"

EXPERIMENT_DIR_NAME="experiment"
EXPERIMENT_FILE_NAME="experiment.csv"

## Model Pusher Constants :-
MODEL_PUSHER_ARTIFACT_NAME = "model_pusher"
MODEL_PUSHER_CONFIG_KEY = "model_pusher_config"
MODEL_PUSHER_MODEL_EXPORT_DIR_KEY = "model_export_dir"
