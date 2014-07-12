import FWCore.ParameterSet.Config as cms

process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(2))

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/hdfs/store/user/tapas/2012-08-01-CRAB_ZEESkim/skim_10_1_wd2.root'
    )
)

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = "POSTLS161_V12::All"

# unpack raw data
process.load("Configuration.StandardSequences.RawToDigi_cff")

# run trigger primitive generation on unpacked digis, then central L1
process.load("L1Trigger.Configuration.CaloTriggerPrimitives_cff")

process.myProducerLabel = cms.EDProducer('Layer1',
    ecalDigisLabel = cms.InputTag("ecalTriggerPrimitiveDigis"),
    hcalDigisLabel = cms.InputTag("hcalTriggerPrimitiveDigis")
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
)

process.p = cms.Path(
    process.ecalDigis*
    process.hcalDigis*
    process.myProducerLabel)

process.e = cms.EndPath(process.out)
