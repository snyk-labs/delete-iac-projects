import os
import sys
from commands.deleteIacProjects import deleteIacProjects, deleteIacProjectsDryRun
from typing import Annotated, Optional
import typer

# Create typer app
app = typer.Typer()

@app.command(help="Delete all IaC Projects")
def delete_iac_projects(org_ids:Annotated[Optional[str], typer.Argument(..., help="Optional parameter for specifying an org id or a list of org ids.  Here is an example: 12345678-1234-1234-1234-123456789012,12345678-1234-1234-1234-123456789012,12345678-1234-1234-1234-123456789012")] = None):
    deleteIacProjects(org_ids)

@app.command(help="Dry run that will list all IaC Projects that will be deleted")
def delete_iac_projects_dry_run(org_ids:Annotated[Optional[str], typer.Argument(..., help="Optional parameter for specifying an org id or a list of org ids.  Here is an example: 12345678-1234-1234-1234-123456789012,12345678-1234-1234-1234-123456789012,12345678-1234-1234-1234-123456789012")] = None):
    deleteIacProjectsDryRun(org_ids)

if __name__ == "__main__":
    app()