from ROOT import *

f = TFile("output.root")

l_obj = ["tauHAD"]

d_hlt = {
    "HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1" : ["hltHpsPFTau27LooseTauWPDeepTau"]
}

d_color = {
    ("HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1","hltHpsPFTauTrack") : kRed,
    ("HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1","hltHpsPFTau27LooseTauWPDeepTau") : kBlue,

}

for var in ["pt","eta"] :
    for obj in l_obj :
        for hlt in d_hlt :
            l_hist = []
            for ref in d_hlt[hlt] :
                h_ = f.Get(f"HLTGenVal/{obj}__{hlt}__{ref}__vs{var}__eff")
                h_.SetStats(0)
                h_.SetTitle("")
                h_.SetLineColor(d_color[(hlt,ref)])
                h_.SetLineWidth(3)
                if var == "pt" : h_.GetXaxis().SetTitle("Gen Tau p_{T} [GeV]")
                elif var == "eta" : h_.GetXaxis().SetTitle("Gen Tau #eta")
                h_.GetYaxis().SetRangeUser(0.0,1.2)
                h_.GetYaxis().SetTitle("Efficiency")
                l_hist.append(h_)
            c = TCanvas("","",1000,1000)
            l = TLegend(0.525,0.775,0.9,0.875)
            l.SetFillStyle(0)
            l.SetBorderSize(0)
            c.cd()
            c.SetGrid()
            for i,h in enumerate(l_hist) :
                if i == 0 : h.Draw("e")
                else : h.Draw("same&e")
                #l.AddEntry(h,f"{d_hlt[hlt][i]}/Gen","l")
                l.AddEntry(h,f"Last Filter/Gen","l")
            l.Draw()
            x1 = 0.15 
            y1 = 0.8
            latex = TLatex()
            latex.SetNDC()
            textSize = 0.625*gStyle.GetPadTopMargin()
            latex.SetTextFont(61)
            latex.SetTextSize(textSize*1.15)
            latex.DrawLatex(x1, y1 ,"CMS") # 0.85

            latex.SetTextFont(52)
            latex.SetTextSize(0.6*textSize)
            latex.DrawLatex(x1, y1-0.06,"Work In Progress")
            latex.DrawLatex(x1, y1-0.09,"Simulation")
            c.SaveAs(f"{hlt}_{obj}_{var}_Eff.png")