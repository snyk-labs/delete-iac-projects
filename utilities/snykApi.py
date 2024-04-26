import requests
import os

# Global variables
SNYK_TOKEN = os.getenv('SNYK_TOKEN')
restHeaders = {'Content-Type': 'application/vnd.api+json', 'Authorization': f'token {SNYK_TOKEN}'}
v1Headers = {'Content-Type': 'application/json', 'Authorization': f'token {SNYK_TOKEN}'}

# Collect organizations data from SNYK_TOKEN
def get_orgs():
    url = 'https://api.snyk.io/rest/orgs?limit=100&version=2024-01-23'
    hasNextLink = True
    orgData = []

    while hasNextLink:
        # Api call to orgs endpoint
        try:
            orgs = requests.get(url, headers=restHeaders)
            orgData.extend(orgs.json()['data'])
        except:
            print("Organization endpoint call failed.")
        
        # Check if next page exist and set url if it does.  If not, exit and return orgData
        try:
            orgs.json()['links']['next']
            hasNextLink = True
            url = 'https://api.snyk.io/' + orgs.json()['links']['next']
        except:
            hasNextLink = False
            return orgData
        
# Collect iac projects        
def get_iac_project(orgId):
    hasNextLink = True
    projectData = []
    url = f'https://api.snyk.io/rest/orgs/{orgId}/projects?limit=100&version=2024-03-12&types=cloudformationconfig%2Chelmconfig%2Ck8sconfig%2Cterraformconfig%2Cterraformplan'

    while hasNextLink:
        # Api call to projects endpoint
        try:
            projects = requests.get(url, headers=restHeaders)
            projectData.extend(projects.json()['data'])
        except:
            print("Project endpoint call failed.")
            
        # Check if next page exist and set url if it does.  If not, exit and return projectData
        try:
            projects.json()['links']['next']
            hasNextLink = True
            url = 'https://api.snyk.io' + projects.json()['links']['next']
        except:
            hasNextLink = False
            return projectData


def get_targets(orgId):
    hasNextLink = True
    targetsData = []
    url = f'https://api.snyk.io/rest/orgs/{orgId}/targets?version=2024-03-12&limit=100&source_types=cli'

    while hasNextLink:
        # Api call to targets endpoint
        try:
            targetsApi = requests.get(url, headers=restHeaders)
            targets = targetsApi.json()['data']
            targetsData.extend(targets)
        except:
            print("Issues endpoint call failed.")
            print(targetsApi)
            
        # Check if next page exist and set url if it does.  If not, exit and return issuesData
        try:
            targets.json()['links']['next']
            hasNextLink = True
            url = 'https://api.snyk.io' + targets.json()['links']['next']
        except:
            hasNextLink = False
            return targetsData
        
def delete_project(orgId, projectId):
    url = f'https://api.snyk.io/rest/orgs/{orgId}/projects/{projectId}?&version=2024-01-23'

    try:
        delete = requests.delete(url, headers=restHeaders)
        print(f"Response Code: {delete}")
    except:
        print("Delete endpoint call failed.")
        print(f"Response Code: {delete}")
        


        