from PhysicsTools.Heppy.utils.cmsswRelease import cmsswRelease, releaseNumber

def testSamples():
    files = [
       '/store/mc/RunIISpring15MiniAODv2/GluGluHToZZTo4L_M125_13TeV_powheg_JHUgen_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/00289B81-C56D-E511-8C21-0025905C2CBC.root',
       '/store/mc/RunIISpring15MiniAODv2/GluGluHToZZTo4L_M125_13TeV_powheg_JHUgen_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/043DD08D-C56D-E511-9693-008CFA110C84.root',
       '/store/mc/RunIISpring15MiniAODv2/GluGluHToZZTo4L_M125_13TeV_powheg_JHUgen_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/2E642290-C56D-E511-AD68-008CFA110C88.root',
       '/store/mc/RunIISpring15MiniAODv2/GluGluHToZZTo4L_M125_13TeV_powheg_JHUgen_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/506AF391-C56D-E511-93A9-008CFA197A20.root',
       '/store/mc/RunIISpring15MiniAODv2/GluGluHToZZTo4L_M125_13TeV_powheg_JHUgen_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/5479D48E-C56D-E511-9B32-008CFA197DB8.root',
       '/store/mc/RunIISpring15MiniAODv2/GluGluHToZZTo4L_M125_13TeV_powheg_JHUgen_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/5E355593-C56D-E511-B25C-008CFA166188.root',
       '/store/mc/RunIISpring15MiniAODv2/GluGluHToZZTo4L_M125_13TeV_powheg_JHUgen_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/A0A56882-C56D-E511-85BF-0025905C3E36.root',
       '/store/mc/RunIISpring15MiniAODv2/GluGluHToZZTo4L_M125_13TeV_powheg_JHUgen_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/A4788386-C56D-E511-ACCA-008CFA00FF80.root',
       '/store/mc/RunIISpring15MiniAODv2/GluGluHToZZTo4L_M125_13TeV_powheg_JHUgen_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/B4135294-C56D-E511-A8DC-008CFA166188.root',
       '/store/mc/RunIISpring15MiniAODv2/GluGluHToZZTo4L_M125_13TeV_powheg_JHUgen_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/C46F3793-C56D-E511-93D4-008CFA166188.root',
       '/store/mc/RunIISpring15MiniAODv2/GluGluHToZZTo4L_M125_13TeV_powheg_JHUgen_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/C49DE48A-C56D-E511-B654-008CFA1660A8.root',
       '/store/mc/RunIISpring15MiniAODv2/GluGluHToZZTo4L_M125_13TeV_powheg_JHUgen_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/D4A39D8E-C56D-E511-A8E8-008CFA110C68.root']
    eosfiles = [''.join(['root://eoscms//eos/cms', lfn]) for lfn in files]
    return eosfiles


if __name__ == '__main__':
    print testSamples()

