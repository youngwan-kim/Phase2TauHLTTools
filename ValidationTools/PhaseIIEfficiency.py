import FWCore.ParameterSet.Config as cms
import Validation.HLTrigger.hltvalcust as hltvalcust

process_ = cms.Process("HLTGenValSource")
process = hltvalcust.add_hlt_validation_phaseII(process_,"HLTX","")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Core.DQMStore_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")
process.load("DQMServices.Components.MEtoEDMConverter_cff")
from DQMServices.Core.DQMEDHarvester import DQMEDHarvester

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(9000) )

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.source = cms.Source("PoolSource",
    #fileNames = cms.untracked.vstring("root://cmsxrootd.fnal.gov//store/mc/RunIISummer20UL18RECO/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/AODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/00000/B4A06248-D09E-314A-ACD7-F157B86109E6.root")
    fileNames = cms.untracked.vstring(
        "file:/data9/Users/youngwan/work/Phase2HLT/CMSSW_14_1_0_pre5/src/Work/tmp0/output_0.root",
        "file:/data9/Users/youngwan/work/Phase2HLT/CMSSW_14_1_0_pre5/src/Work/tmp0/output_1.root",
        "file:/data9/Users/youngwan/work/Phase2HLT/CMSSW_14_1_0_pre5/src/Work/tmp0/output_2.root",
        "file:/data9/Users/youngwan/work/Phase2HLT/CMSSW_14_1_0_pre5/src/Work/tmp0/output_3.root",
        "file:/data9/Users/youngwan/work/Phase2HLT/CMSSW_14_1_0_pre5/src/Work/tmp0/output_4.root",
        "file:/data9/Users/youngwan/work/Phase2HLT/CMSSW_14_1_0_pre5/src/Work/tmp0/output_5.root",
        "file:/data9/Users/youngwan/work/Phase2HLT/CMSSW_14_1_0_pre5/src/Work/tmp0/output_6.root",
        "file:/data9/Users/youngwan/work/Phase2HLT/CMSSW_14_1_0_pre5/src/Work/tmp0/output_7.root",
        "file:/data9/Users/youngwan/work/Phase2HLT/CMSSW_14_1_0_pre5/src/Work/tmp0/output_8.root",
   )
)

process.harvester = DQMEDHarvester("HLTGenValClient",
    outputFileName = cms.untracked.string('output.root'),
    subDirs        = cms.untracked.vstring("HLTGenVal"),
)

process.outpath = cms.EndPath(process.harvester)
