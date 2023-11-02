import os
from urllib.parse import urlparse


OUTPUT_FILE_NAME = "output.csv"
URL = "https://djinni.co"
JOBS_URL = "https://djinni.co/jobs"

def get_output_paths( filename:str) -> str:
    output_dir = os.path.join(os.getcwd(), urlparse(JOBS_URL).hostname)
    output_path = os.path.join(output_dir, filename)
    return output_path, output_dir
