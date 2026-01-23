from FastPUPPI.NtupleProducer.runInputs140X import *
#process.Tracer = cms.Service("Tracer")
process.source = process.source.clone(
    fileNames = cms.untracked.vstring('root://cms-xrd-global.cern.ch//store/mc/Phase2Spring24DIGIRECOMiniAOD/SMS-TStauStau_MStau-200_ctau-10mm_mLSP-1_TuneCP5_14TeV_madgraphMLM-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/PU200_AllTP_140X_mcRun4_realistic_v4-v2/2820000/00179471-60a6-47f1-8c0a-d21dbc6f4baf.root'),
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10))
