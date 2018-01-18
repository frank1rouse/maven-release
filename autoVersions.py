#!/usr//bin/env python

import sys
import os
import re
#
def currentVersion():
        path = os.getcwd()
        file_path = os.path.join(path, "pom.xml")

        if os.path.isfile(file_path):
            version = os.popen("/usr/bin/mvn -q -Dexec.executable=\"echo\" -Dexec.args='${project.version}' --non-recursive exec:exec").readlines()
        else:
            raise Exception("pom.xml file not found - Make sure you run this command at top of repo")
        return version[0].rstrip()

def isSnapshot(version):
    if "SNAPSHOT" in version:
       snapshot = 1
    else:
       snapshot = 0
    return snapshot

def incrementVersion():
    relBranches = ('notstable', 'atterberg', 'beethoven', 'chausson', 'draeseke', 'eisler')
    version = currentVersion()
    snap = isSnapshot(version)
    if snap == 1:
       relVersion = re.sub('\-SNAPSHOT$', '', version)
    else:
       relVersion = version
    major,minor,patch = map(int, relVersion.split("."))
    if snap == 1:
        minor += 1
        newVersion = str(major)+ "." + str(minor) + "." + str(patch)
        newVersion = newVersion + "-SNAPSHOT"
    else:
        major += 1
        minor = patch = 0
        relVersion = str(major)+ "." + str(minor) + "." + str(patch)

        minor += 1
        newVersion = str(major)+ "." + str(minor) + "." + str(patch) + "-SNAPSHOT"

    return(relVersion, newVersion, relBranches[major])

def setVersion(version):
    cmd = "/usr/bin/mvn versions:set -DnewVersion=%s" % version
    os.system(cmd)


# if __name__ == "__main__":
#   relVersion, snapshotVersion, branchName = incrementVersion()
#   print relVersion
#   print snapshotVersion
#   print branchName

  #setVersion(newVersion)
