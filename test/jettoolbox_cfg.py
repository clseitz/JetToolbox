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

from cmsjet.JetToolbox.jetToolbox_cff import *
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
		fileNames = cms.untracked.vstring('/store/mc/Spring14miniaod/QCD_Pt-300to470_Tune4C_13TeV_pythia8/MINIAODSIM/141029_PU40bx50_castor_PLS170_V6AN2-v1/00000/1A3D915A-CA7F-E411-AFE2-0025905A48D0.root')
		)

