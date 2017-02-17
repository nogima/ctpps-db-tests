import FWCore.ParameterSet.Config as cms

process = cms.Process("ProcessOne")

process.source = cms.Source("EmptyIOVSource",
    timetype = cms.string('runnumber'),
    firstValue = cms.uint64(1),  
    lastValue = cms.uint64(1),   
    interval = cms.uint64(1)
)
#Database output service

process.load("CondCore.CondDB.CondDB_cfi")
# input database (in this case local sqlite file)
process.CondDB.connect = 'sqlite_file:CTPPSDAQMapping_fill_5288.db'  


process.PoolDBESSource = cms.ESSource("PoolDBESSource",
    process.CondDB,
    DumpStat=cms.untracked.bool(True),
    toGet = cms.VPSet(cms.PSet(
        record = cms.string('CTPPSDAQMappingRcd'),
        tag = cms.string("DAQMapping_fill_5288")
    )),
)



process.myprodtest = cms.EDAnalyzer("myCTPPSDAQMappingAnalyzer") 
 
process.p = cms.Path(process.myprodtest)

