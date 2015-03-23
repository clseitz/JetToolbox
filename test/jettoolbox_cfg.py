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

from JetToolbox.jetToolbox_cff import *
jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', addSubjets= True ) #, addGroomers = False )
jetToolbox( process, 'ca8', 'ca8JetSubs', 'out', addSubjets=True, addNsub=True, addPruning=True, nfilt=5 , zCut=0.2, addTrimming=True, addCMSTopTagger=True, addHEPTopTagger=True, addMassDrop=True )
jetToolbox( process, 'ca15', 'ca15JetSubs', 'out' )
#jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', addSubjets= True, miniAOD=False ) #, addGroomers = False )
#jetToolbox( process, 'ca8', 'ca8JetSubs', 'out', miniAOD=False, addSubjets=True, addNsub=True, addPruning=True, nfilt=5 , zCut=0.2 , addTrimming=True, addCMSTopTagger=True, addHEPTopTagger=True, addMassDrop=True )
#jetToolbox( process, 'ca15', 'ca15JetSubs', 'out', miniAOD=False )


process.endpath = cms.EndPath(process.out)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )
#process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring('file:example.root') ) 
#from PhysicsTools.PatAlgos.patInputFiles_cff import filesRelValProdTTbarAODSIM
#process.source.fileNames = filesRelValProdTTbarAODSIM

process.source = cms.Source("PoolSource",
		fileNames = cms.untracked.vstring('/store/relval/CMSSW_7_2_2_patch1/RelValTTbar_13/MINIAODSIM/PU50ns_MCRUN2_72_V0-v1/00000/0683685E-8D73-E411-9A7A-0025905A60D0.root')
		)

