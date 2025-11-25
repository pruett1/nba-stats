import kagglehub
import os
import shutil

os.environ['KAGGLEHUB_CACHE'] = '.'

if os.path.isdir('datasets'):
    shutil.rmtree('datasets')

kagglehub.dataset_download("eoinamoore/historical-nba-data-and-player-box-scores")