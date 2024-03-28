import os
import sys
import shutil
sys.path.insert(0,'packages')
def create_env(clustername):
    CSP_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    envDir = CSP_BASE+"/environments/"+clustername
    shutil.copytree(CSP_BASE+"/providers/"+"/aws/",envDir)
