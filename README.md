# Delete IaC projects

This script will find all IaC projects and delete them

## Requirements

Python version 3.9.5

## Running
```bash
export SNYK_TOKEN=TYPE-TOKEN-SNYK-HERE
git clone https://github.com/Snyk/snyk-demo-todo
pip install -r requirements.txt
python3 index.py ignore-from-cve-in-csv /FULL/PATH/TO/CVEFILE.csv
```
