import re
from utilities.snykApi import *

def extract_org_ids_from_org_data(orgs_data):
    org_ids = []
    for org_data in orgs_data:
        org_ids.append(org_data['id'])

    return org_ids

def separate_org_ids(org_id_list):
    try:
        org_ids = org_id_list.split(",")
        if validate_org_ids(org_ids):
            return org_ids
        else:
            return False
    except:
        if validate_org_ids(org_ids):
            return org_ids
        else:
            return False

def validate_org_ids(org_id_list):
    pattern = re.compile(r'([\d\w]{8}-[\d\w]{4}-[\d\w]{4}-[\d\w]{4}-[\d\w]{12})')
    for org_id in org_id_list:
        if pattern.fullmatch(org_id) == None:
            return False
    
    return True

def delete_projects(project_data, org_id, dry_run):
    for project in project_data:
        if dry_run:
            print(f"Here is the project ID: {project['id']} and name of the project: {project['attributes']['name']}")
        else:
            print(f"Deleting project ID: {project['id']}")
            delete_project(org_id, project['id'])