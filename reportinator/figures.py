#using seaborn as stylesheet https://python-graph-gallery.com/106-seaborn-style-on-matplotlib-plot/
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import argparse
import sys
import random
import os
import reportinator.functions as fn
import reportinator

def main(file, lister, index, *args, **kwargs):
    output = ""
    cache_dir=reportinator.cache
    plt.style.use('bmh')
    palette = []
    deep=["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B3","#937860", "#DA8BC3", "#8C8C8C", "#CCB974", "#64B5CD"]
    deep6=["#4C72B0", "#55A868", "#C44E52","#8172B3", "#CCB974", "#64B5CD"]
    muted=["#4878D0", "#EE854A", "#6ACC64", "#D65F5F", "#956CB4","#8C613C", "#DC7EC0", "#797979", "#D5BB67", "#82C6E2"]
    muted6=["#4878D0", "#6ACC64", "#D65F5F","#956CB4", "#D5BB67", "#82C6E2"]
    pastel=["#A1C9F4", "#FFB482", "#8DE5A1", "#FF9F9B", "#D0BBFF","#DEBB9B", "#FAB0E4", "#CFCFCF", "#FFFEA3", "#B9F2F0"]
    pastel6=["#A1C9F4", "#8DE5A1", "#FF9F9B","#D0BBFF", "#FFFEA3", "#B9F2F0"]
    bright=["#023EFF", "#FF7C00", "#1AC938", "#E8000B", "#8B2BE2","#9F4800", "#F14CC1", "#A3A3A3", "#FFC400", "#00D7FF"]
    bright6=["#023EFF", "#1AC938", "#E8000B","#8B2BE2", "#FFC400", "#00D7FF"]
    dark=["#001C7F", "#B1400D", "#12711C", "#8C0800", "#591E71","#592F0D", "#A23582", "#3C3C3C", "#B8850A", "#006374"]
    dark6=["#001C7F", "#12711C", "#8C0800","#591E71", "#B8850A", "#006374"]
    colorblind=["#0173B2", "#DE8F05", "#029E73", "#D55E00", "#CC78BC","#CA9161", "#FBAFE4", "#949494", "#ECE133", "#56B4E9"]
    colorblind6=["#0173B2", "#029E73", "#D55E00","#CC78BC", "#ECE133", "#56B4E9"]
    black=['FFFFFF']

    # CHOOSE PALETTE
    palette=dark

    # parser
    fun = kwargs.get('fit', None)
    n = index
    k = random.randint(0,len(palette)-1)
    #inputs and initializations
    y_name_list=[]
    y_list=[]
    in_file = cache_dir+"/csvs/"+file
    y_list = (lister).split(',')
    y_list = [int(x) - 1 for x in y_list]
    x_index = y_list.pop(0)
    data = pd.read_csv(in_file)
    data = data[:-2]
    x_name = data.columns[x_index]
    for y_index in y_list:
        y_name_list.append(data.columns[y_index])

    #actual plotting and saving in PDF
    def plot(x_name, y_name_list, data, n, k):
        x = data[x_name]
        x = list(map(float, x))
        f = plt.figure()
        plt.rc('text', usetex=False)
        plt.rc('font', family='serif')
        i=0
        markers=['o','+','s','^','x','D','v']
        for y_name in y_name_list:
            y = data[y_name]
            y = list(map(float, y))
            plt.scatter (x,y, marker = markers[i],
                color='#FFA500', label="Observed, for "+y_name)
            # palette[k]
            if not fun:
                cap=False
                pass
            else:
                p,_,cap= fit(x,y, fun)
                fitfig = np.poly1d(p)
                plt.plot(x,fitfig(x), linestyle='dotted',color='#000000',label="Fitted Data")
            k+=1
            # palette[k+1]
            if k>len(palette)-1:
                k-=len(palette)-1
            i+=1
        plt.xlabel(r'%s' % x_name,fontsize = 13)
        plt.ylabel(r'%s'% y_name,fontsize = 13)
        plt.legend()
        if "$" in y_name:
            y_new = y_name.replace("$","")
            y_new = y_new.replace("\\","")
            f.savefig(cache_dir+"/"+y_new.split(" ")[0]+str(n)+".pdf", bbox_inches = 'tight')
        else:
            f.savefig(cache_dir+"/"+y_name.split(" ")[0]+str(n)+".pdf", bbox_inches = 'tight')
        return cap

    file_name = file[:-4]

    def pregraph(name,n,cap):
        if "$" in name:
            name = name.replace("$","")
            name = name.replace("\\","")
        location = "./"+name.split(" ")[0]+str(n)+".pdf"
        tag = name.split(" ")[0]
        tag_new = tag.lower()
        #print (cap)
        if not cap:
            output = '\\begin{figure}[H]'+'\n'+'\\centering'+'\n'+'\\includegraphics[width = \\columnwidth]'+'{'+location+'}'+'\n'+'\\caption{'+tag+'}'+'\n'+'\\label{g:\"'+tag_new+'\"}'+'\n'+'\\end{figure}'
        else:
            output = '\\begin{figure}[H]'+'\n'+'\\centering'+'\n'+'\\includegraphics[width = \\columnwidth]'+'{'+location+'}'+'\n'+'\\caption{'+tag+', '+cap+ '}'+'\n'+'\\label{g:\"'+tag_new+'\"}'+'\n'+'\\end{figure}'
        return output

    def fit(x,y,fun):
        if fun == "lin":
            p, pcov = np.polyfit(x,y,1,cov=True)
            p_sigma = np.sqrt(np.diag(pcov))
            fitfun = fn.lin(p,p_sigma)
            cap= (r'%s' % fitfun)
        elif fun == "pol2":
            p, pcov = np.polyfit(x,y,2,cov=True)
            p_sigma = np.sqrt(np.diag(pcov))
            fitfun = fn.pol2(p,p_sigma)
            cap= (r'%s' % fitfun)
        elif fun == "pol3":
            p, pcov = np.polyfit(x,y,3,cov=True)
            p_sigma = np.sqrt(np.diag(pcov))
            fitfun = fn.pol3(p,p_sigma)
            cap= (r'%s' % fitfun)
        elif fun == "pol4":
            p, pcov = np.polyfit(x,y,4,cov=True)
            p_sigma = np.sqrt(np.diag(pcov))
            fitfun = fn.pol4(p,p_sigma)
            cap= (r'%s' % fitfun)
        elif fun == "pol5":
            p, pcov = np.polyfit(x,y,5,cov=True)
            p_sigma = np.sqrt(np.diag(pcov))
            fitfun = fn.pol5(p,p_sigma)
            cap= (r'%s' % fitfun)
        
        # if fun == "expo":
        #     func.expo()
        # elif fun == "log":
        else:
            output += "Wrong function"
        

        return p,pcov,cap

    cap = plot(x_name, y_name_list, data, n, k)
    return pregraph(y_name_list[-1], n,cap)


if __name__== "__main__":
    section=sys.argv[1]
    print(main(section))
