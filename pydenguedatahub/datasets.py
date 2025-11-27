# pydenguedatahub/datasets.py

import rpy2.robjects as ro
from rpy2.robjects.conversion import localconverter
from rpy2.robjects import default_converter
import pandas as pd

def _load_dataset(dataset_name: str) -> pd.DataFrame:
    """
    Internal function to load a dataset from the R package 'denguedatahub'
    and convert it to a pandas DataFrame.
    """
    try:
        ro.r('library(denguedatahub)')
        r_df = ro.r(f'denguedatahub::{dataset_name}')
        with localconverter(default_converter):
            pdf = ro.conversion.rpy2py(r_df)
        return pdf
    except Exception as e:
        print(f"Error loading dataset {dataset_name}: {e}")
        return None


# List of all dataset names in 'denguedatahub'
_dataset_names = [
    "americas_annual_data",
    "cdc_casesby_week",
    "cdc_dengue_agesex",
    "cdc_dengue_casesbyjurisdiction",
    "cdc_dengue_countyyear",
    "cdc_local_dengue_cases",
    "cdc_travel_associated_dengue_cases",
    "cdc_usa_dengue_infection",
    "china_annual_data",
    "india_annual_data",
    "korea_dengue",
    "level_of_risk",
    "philippines_daily_data",
    "singapore_weekly_data",
    "sl_annual",
    "sl_dengue_serotype",
    "sl_province_districts",
    "sl_sites",
    "srilanka_weekly_data",
    "taiwan_dengue",
    "world_annual"
]

# Dynamically create a function for each dataset
for name in _dataset_names:
    globals()[name] = lambda n=name: _load_dataset(n)
