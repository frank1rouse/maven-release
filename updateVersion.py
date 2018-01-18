#!/usr//bin/env python

import sys
import os
import re

def currentVersion():
    version = os.popen("/usr/bin/mvn -q -Dexec.executable=\"echo\" -Dexec.args='${project.version}' --non-recursive exec:exec").readlines()
    return version[0].rstrip()

def isSnapshot(version):
    if "SNAPSHOT" in version:
       snapshot = 1
    else:
       snapshot = 0
    return snapshot

def incrementVersion(m):
    version = currentVersion()
    snap = isSnapshot(version)
    if snap == 1:
       myVersion = re.sub('\-SNAPSHOT$', '', version)
    else:
       myVersion = version
    major,minor,patch = map(int, myVersion.split("."))
    if m == "major":
       major += 1
       minor = patch = 0
    if m == "minor":
       minor += 1
    if m == "patch":
       patch += 1
    newVersion = str(major)+ "." + str(minor) + "." + str(patch)
    if snap == 1:
       newVersion = newVersion + "-SNAPSHOT"
    return(newVersion)

    print(myVersion, newVersion)

if __name__ == "__main__":
  incrementVersion("patch")
