from CMGTools.VVResonances.analyzers.EventInterpretationBase import *
from CMGTools.VVResonances.tools.Pair import Pair
import itertools

class MultiFinalState( EventInterpretationBase ):
    def __init__(self, cfg_ana, cfg_comp, looperName):
        super(MultiFinalState,self).__init__(cfg_ana, cfg_comp, looperName)

    def process(self, event):
        super(MultiFinalState,self).process(event)

        LNuJJ=[]
        LLJJ =[]
        JJ=[]
        JJNuNu=[]
        TopCR=[]

        if self.doSkim and not self.skim(event.selectedLeptons,event.met):
            return False


        #clean leptons and make jets
        cleanedPackedCandidates = self.removeLeptonFootPrint(event.selectedLeptons,event.packedCandidatesForJets)
        if self.cfg_ana.doCHS:
            cleanedPackedCandidates = filter(lambda x: x.fromPV(0) ,cleanedPackedCandidates)
          
        selectedFatJets = self.makeFatJets(cleanedPackedCandidates)
        if self.isMC:
            self.matchSubJets(selectedFatJets,event.genwzquarks)
               


        #Before the signal selection lets look at the top control region
        #This can have overlap with the signal region    
        if len(event.LNu)>0:
            bestW = max(event.LNu,key = lambda x: x.leg1.pt())
            #find the jets in the opposite hemisphere of the lepton
            oppositeHemishereJets=[]
            for jet in selectedFatJets:
                if jet.pt()>200 and deltaPhi(jet.phi(),bestW.leg1.phi())>3.14/2. and jet.softDropJet.mass()>40 and jet.softDropJet.mass()<130:
                    oppositeHemishereJets.append(jet)

            if len(oppositeHemishereJets)>0:        
                bestJet = max(oppositeHemishereJets,key=lambda x: x.softDropJet.mass())
                VV=Pair(bestW,bestJet)
                selected = {'pair':VV}
                remainingCands =self.removeJetFootPrint([bestJet],cleanedPackedCandidates)
                selected['satelliteJets']=self.makeSatelliteJets(remainingCands)
                self.topology(selected)
                TopCR.append(selected)  
                
                    



        finished= False
        #OK lets start from LL+JJ that has the highest purity
        #take the Z->ll  nearest to the Z mass and the highest pt jets
        if len(event.LL)>0 and not finished:
            bestZ = min(event.LL,key = lambda x: abs(x.M()-91.118))
            for jet in selectedFatJets:
                VV=Pair(bestZ,jet)
                if self.selectPairLL(VV):
                    selected = {'pair':VV}
                    remainingCands =self.removeJetFootPrint([jet],cleanedPackedCandidates)
                    selected['satelliteJets']=self.makeSatelliteJets(remainingCands)
                    #add VBF info
                    self.topology(selected)
                    LLJJ.append(selected)                   
                    finished=True
                    break;
                

        #OK Now the W . Highest Pt lepton + j
        if len(event.LNu)>0 and not finished:
            bestW = max(event.LNu,key = lambda x: x.leg1.pt())
            for jet in selectedFatJets:
                VV=Pair(bestW,jet)
                if self.selectPairLNu(VV):
                    selected = {'pair':VV}
                    remainingCands =self.removeJetFootPrint([jet],cleanedPackedCandidates)
                    selected['satelliteJets']=self.makeSatelliteJets(remainingCands)
                    #add VBF info
                    self.topology(selected)
                    LNuJJ.append(selected)                   
                    finished=True
                    break;



        #Now look for jet+MET
        if len(selectedFatJets)>0 and not finished:
            jet = selectedFatJets[0]
            VV=Pair(event.met,jet)
            if self.selectPairJJNuNu(VV):
                selected = {'pair':VV}
                remainingCands =self.removeJetFootPrint([jet],cleanedPackedCandidates)
                selected['satelliteJets']=self.makeSatelliteJets(remainingCands)
                #add VBF info
                self.topology(selected)
                JJNuNu.append(selected)                   
                finished=True

        #Now look for jet+jet
        if len(selectedFatJets)>1 and not finished:

            jet1 = selectedFatJets[0]
            jet2 = selectedFatJets[1]
            VV=Pair(jet1,jet2)
            if self.selectPairJJ(VV):
                selected = {'pair':VV}
                remainingCands =self.removeJetFootPrint([jet1,jet2],cleanedPackedCandidates)
                selected['satelliteJets']=self.makeSatelliteJets(remainingCands)
                #add VBF info
                self.topology(selected)
                JJ.append(selected)                   
                finished=True
                






        setattr(event,'LNuJJ'+self.cfg_ana.suffix,LNuJJ)
        setattr(event,'JJ'+self.cfg_ana.suffix,JJ)
        setattr(event,'LLJJ'+self.cfg_ana.suffix,LLJJ)
        setattr(event,'JJNuNu'+self.cfg_ana.suffix,JJNuNu)
        setattr(event,'TopCR'+self.cfg_ana.suffix,TopCR)

