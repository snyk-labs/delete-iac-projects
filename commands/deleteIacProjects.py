import sys
from utilities.snykApi import *
from utilities.utility import *

def deleteIacProjects(*args):
     # Pull orgs data
    if args[0] != None:
        orgIds = separate_org_ids(args[0])
        # Exit program if any of the ids are invalid
        if orgIds == False:
            print("Invalid IDs, please check and input valid IDs")
            sys.exit()
        
    else:
        orgsData = get_orgs()
        orgIds = extract_org_ids_from_org_data(orgsData)

    for orgId in orgIds:
        project_data = get_iac_project(orgId)
        delete_projects(project_data, orgId, False)

    

def deleteIacProjectsDryRun(*args):
    if args[0] != None:
        orgIds = separate_org_ids(args[0])
        # Exit program if any of the ids are invalid
        if orgIds == False:
            print("Invalid IDs, please check and input valid IDs")
            sys.exit()
    else:
        orgsData = get_orgs()
        orgIds = extract_org_ids_from_org_data(orgsData)

    
    for orgId in orgIds:
        project_data = get_iac_project(orgId)
        delete_projects(project_data, orgId, True)

    