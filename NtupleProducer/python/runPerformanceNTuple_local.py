from FastPUPPI.NtupleProducer.runPerformanceNTuple import *
#process.Tracer = cms.Service("Tracer")
process.source = process.source.clone(
    fileNames = cms.untracked.vstring('root://eoscms.cern.ch//eos/cms/store/cmst3/group/l1tr/pviscone/SampleFactory/DoubleElectron_FlatPt_1To100__chain_Phase2Spring24GS-INFP_PU200/SampleFactory/250714_121635/0000/inputs140X_103.root'),
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(20))

noResp()
addGenLep([11,22])
addTkEG()
addHGCalTPs()
addStaEG()
addDecodedTk()
addDecodedCalo()
