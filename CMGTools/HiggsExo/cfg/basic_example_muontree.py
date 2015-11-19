import os
import PhysicsTools.HeppyCore.framework.config as cfg
#from PhysicsTools.Heppy.utils.miniAodFiles import miniAodFiles
from CMGTools.HiggsExo.utils.testSamples import testSamples

# input component 
# several input components (samples to run over) can be declared,
# and added to the list of selected components
inputSample = cfg.Component(
    'test_component',
    files = testSamples(),
    )
inputSample.isMC = True
inputSample.splitFactor = 1 

selectedComponents  = [inputSample]


# import the analyzer
from CMGTools.HiggsExo.examples.SimpleMuonAnalyzer import SimpleMuonAnalyzer
muons = cfg.Analyzer(
    SimpleMuonAnalyzer,
    ptmin = 5.,
    etamaxMu = 2.4
    )

# and the tree
from CMGTools.HiggsExo.examples.SimpleMuonTreeAnalyzer import SimpleMuonTreeAnalyzer
tree = cfg.Analyzer(
    SimpleMuonTreeAnalyzer
    )

# definition of a sequence of analyzers,
# the analyzers will process each event in this order
sequence = cfg.Sequence( [
    muons,
    tree
    ] )

# finalization of the configuration object. 
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence, 
                     services = [],
                     events_class = Events)

print config

