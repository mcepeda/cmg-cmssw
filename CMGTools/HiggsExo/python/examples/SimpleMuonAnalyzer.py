# includes to incorporate the framework and already defined variables into your job
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.Heppy.physicsobjects.Lepton import Lepton
from PhysicsTools.Heppy.physicsobjects.Muon import Muon
from PhysicsTools.HeppyCore.utils.deltar import matchObjectCollection

from PhysicsTools.Heppy.analyzers.core.all import *
from PhysicsTools.Heppy.analyzers.objects.all import *
from PhysicsTools.Heppy.analyzers.gen.all import *

from CMGTools.HToZZ4L.tools.DiObject import DiObject
from CMGTools.HToZZ4L.tools.DiObjectPair import DiObjectPair

import os
import itertools
import collections
import ROOT

class SimpleMuonAnalyzer(Analyzer):
    '''Just a simple muon analyzer, to be used in tutorials.'''

    # here you define the objects you will use
    def declareHandles(self):
        super(SimpleMuonAnalyzer, self).declareHandles()
        # Get the muons from the event:
        self.handles['muons'     ] = AutoHandle('slimmedMuons'      , 'std::vector<pat::Muon>'        )


    # main function (looped over the events) 
    def process(self, event):
        super(SimpleMuonAnalyzer, self).readCollections(event.input)
        # creating muon python objects wrapping the EDM muons
        # keeping only the first 4 leading muons
        event.muons = map(Lepton, self.handles['muons'].product())[:4]
        # we can add basic cuts to the muons
        event.muons = [ lepton for lepton in event.muons if (lepton.pt()>self.cfg_ana.ptmin and abs(lepton.eta())<self.cfg_ana.etamaxMu)]  # min pt
        # and make (muon, muon) combinations     
        event.dimuons = self.findOSSFPairs(event.muons)


    # this is a function, to simplify the process 
    def findOSSFPairs(self, leptons):
        '''Make combinatorics and make permulations of two leptons
        '''
        out = []
        for l1, l2 in itertools.permutations(leptons, 2):
            # pdgID is a Monte Carlo code to signify which kind of particle you are dealing with
            # see http://pdg.lbl.gov/mc_particle_id_contents.html 
            # pdgID = 13 means Muon^{-}, pdgID = -13  means Muon^{+}   (11 stands for electrons, 15 for taus)
            # Therefore  by checking that the ID_leg1 + ID_leg2 == 0 you make sure that the object has two leptons 
            # of the same flavour (muon, muon) but opposite charge (+,-):
            if (l1.pdgId()+l2.pdgId())!=0:
                continue;
            if (l1.pdgId()<l2.pdgId())!=0:   # this just orders the two muons by sign to remove permutations (mu1,mu2) == (mu2,mu1) 
                continue;
            twoObject = DiObject(l1, l2)
            out.append(twoObject)
        return out

   
