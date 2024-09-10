# Phase2TauHLTTools
Phase2 Tau HLT Tools


Configuration set up 
```
cmsrel CMSSW_14_1_0_pre5
cd CMSSW_14_1_0_pre5/src/
cmsenv && git cms-init
git cms-merge-topic 45355
scram b -j 8
```

First run your HLT path, save the outputs and input into `ValidationTools/PhaseIIEfficiency.py` by editing 

```
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        "file:(your HLT outputs)",
        ...
   )
)
```

Then run `ValidationTools/PhaseIIEfficiency.py` which will give you an output file (`output.root` by default)
Take this as an input into `ValidationTools/EfficiencyPlotter.py` to get the efficiency plots.
The objects are defined in `output.root` which you can use to configure  `ValidationTools/EfficiencyPlotter.py`
