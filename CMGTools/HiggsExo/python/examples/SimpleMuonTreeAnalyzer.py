# include the main tree class from Heppy
from PhysicsTools.Heppy.analyzers.core.TreeAnalyzerNumpy import TreeAnalyzerNumpy


class SimpleMuonTreeAnalyzer(TreeAnalyzerNumpy):
   
    # "book" the histograms you want to fill 
    def beginLoop(self, setup):
        super(SimpleMuonTreeAnalyzer, self).beginLoop(setup)

        # You can just book histograms one by one:
        self.tree.var('count_muons')

        # or group them to make the code cleaner:
        self.bookmuon('muon1')
        self.bookmuon('muon2')
        self.bookmuon('muon3')
        self.bookmuon('muon4')
        self.bookdimuon('dimuon1')
        self.bookdimuon('dimuon2')

 

    # main program: loop over the events and fill the histograms
    def process(self, event):

        # Fill the histograms, one by one
        self.tree.fill('count_muons',len(event.muons)) 

        # or though functions to simplify
        if len(event.muons)>0:
            self.fillmuon('muon1', event.muons[0])
        if len(event.muons)>1:
            self.fillmuon('muon2', event.muons[1])
        if len(event.muons)>2:
            self.fillmuon('muon3', event.muons[2])
        if len(event.muons)>3:
            self.fillmuon('muon4', event.muons[3])

        if len(event.dimuons)>0:
            self.filldimuon('dimuon1', event.dimuons[0])
        if len(event.dimuons)>1:
            self.filldimuon('dimuon2', event.dimuons[1])

        self.tree.tree.Fill()


    def bookmuon(self, name):
        self.tree.var('{name}_pt'.format(name=name) )
        self.tree.var('{name}_eta'.format(name=name) )
        self.tree.var('{name}_phi'.format(name=name) )
   
    # book dimuon and book muon could be very different if needed
    def bookdimuon(self, name):
        self.tree.var('{name}_pt'.format(name=name) )
        self.tree.var('{name}_mass'.format(name=name) )

    # here you fill the histograms 
    def fillmuon(self, name, muon):
        if muon:
            self.tree.fill('{name}_pt'.format(name=name), muon.pt())
            self.tree.fill('{name}_eta'.format(name=name), muon.eta())
            self.tree.fill('{name}_phi'.format(name=name), muon.phi())

    def filldimuon(self, name, dimuon):
        if dimuon:
            self.tree.fill('{name}_pt'.format(name=name), dimuon.pt())
            self.tree.fill('{name}_mass'.format(name=name), dimuon.mass())


 
