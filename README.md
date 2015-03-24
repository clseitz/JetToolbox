# JetToolbox
Python framework for configuration of jet tools via the jet toolbox. 

## Instructions

Check the branch for the correspondent release. This branch (jetToolbox_72X) is for CMSSW_7_2_X, then for example:
```
cmsrel CMSSW_7_2_0
cd CMSSW_7_2_0/src/
git clone https://github.com/cms-jet/JetToolbox -b jetToolbox_72X cmsjet/JetToolbox
scram b -j 18
```
To test the toolbox:
```
cmsRun cmsjet/JetToolbox/test/jetToolbox_cfg.py
```
In that python file you also can see a basic example on how to use the toolbox.
