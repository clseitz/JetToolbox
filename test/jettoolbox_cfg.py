import FWCore.ParameterSet.Config as cms

process = cms.Process('jetToolbox')
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.Geometry_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'PLS170_V7AN1::All'

process.load('FWCore.MessageLogger.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 10
process.MessageLogger.suppressWarning = cms.untracked.vstring('ecalLaserCorrFilter','manystripclus53X','toomanystripclus53X')
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.options.allowUnscheduled = cms.untracked.bool(True)

from JMEAnalysis.JetToolbox.jetToolbox_cff import *
jetToolbox( process, 'ak4', 'ak4JetSubs', 'out', minPt=10., addNsub=True, addPruning=True, nfilt=5 , zCut=0.2 ,addTrimming=True, addFiltering=True)


#process.out = cms.OutputModule("PoolOutputModule",
#                               fileName = cms.untracked.string('test.root'),
#                               outputCommands = cms.untracked.vstring(['keep *'])
#                               )

process.endpath = cms.EndPath(process.out)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('/store/mc/Spring14miniaod/QCD_Pt-300to470_Tune4C_13TeV_pythia8/MINIAODSIM/141029_PU40bx50_castor_PLS170_V6AN2-v1/00000/1A3D915A-CA7F-E411-AFE2-0025905A48D0.root')
           
                            )

