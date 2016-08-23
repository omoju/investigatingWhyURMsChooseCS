    
from __future__ import division
from numpy  import array

import numpy as np
from pylab import *

# Set defaults
# For cute colors

import brewer2mpl
bmap_1 = brewer2mpl.get_map('Set1', 'qualitative', 3) # Red
bmap_2 = brewer2mpl.get_map('RdYlBu', 'diverging', 11) # Blue
bmap_3 = brewer2mpl.get_map('BrBG', 'diverging', 11) # Green
colors_1 = bmap_1.mpl_colors
colors_2 = bmap_2.mpl_colors
colors_3 = bmap_3.mpl_colors


def turnArray(x):
    theList = []
    if 1 in x.index:
        ("")
    else:
        x.set_value(1, 0)

    if 2 in x.index:
        ("")
    else:
        x.set_value(2, 0)

    if 3 in x.index:
        ("")
    else:
        x.set_value(3, 0)

    if 4 in x.index:
        ("")
    else:
        x.set_value(4, 0)

    if 5 in x.index:
        ("")
    else:
        x.set_value(5, 0)
        
    for i in range(1, len(x)+1):
        theList.append(x[i])
    a = array( theList ) 
    return a


def stars(p):
   if p < 0.0001:
       return "****"
   elif (p < 0.001):
       return "***"
   elif (p < 0.01):
       return "**"
   elif (p < 0.05):
       return "*"
   else:
       return "-"
    
 # Customizing the figure
font = {'family' : 'serif',
        'color'  : '#141433',
        'weight' : 'normal',
        'size'   : 12,
        }

params = {
   'axes.labelsize': 8,
   'text.fontsize': 8,
   'legend.fontsize': 10,
   'xtick.labelsize': 10,
   'ytick.labelsize': 10,
   'text.usetex': False,
   'figure.figsize': [5.5, 4.5]
   }
    

plot_params = {
    'xmin_gen' : 0,
    'xmax_gen' : 0,
    'ymin_gen' : 0,
    'ymax_gen' : 0,
    'xlabel' : '',
    'ylabel' : '',
    'title' : '',
    'legend_label': ['',''],
    'x1Color' : 'r',
    'x2Color' : 'b'
}


def scaleData(theDataFrame):
    '''Function normalizes data for each dimension of interest.

    Input:
        theDataFrame: pandas DataFrame
   
    '''
    # must sort to get index in order
    # I used the sum of everything so that we are comparing real percentages.
    theMin, theSum = theDataFrame.min(), theDataFrame.sum() 
 
    for (index, val) in theDataFrame.iteritems():
        theDataFrame[index] = ( val / theSum) * 100    
    # Rounding errors doesn't make everything add up to 100, sometimes its 98, 97 and so on
 
def plot_corr(df, myFileName, size=10):
    '''Function plots a graphical correlation matrix for each pair of columns in the dataframe.

    Input:
        df: pandas DataFrame
        myFileName: the name of the figure to be stored
        size: vertical and horizontal size of the plot
    '''
    
    import matplotlib.pyplot as plt

        
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr)
    
    plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical', fontsize = 15);
    plt.yticks(range(len(corr.columns)), corr.columns, fontsize = 15);
    
    
    fileName = []
    fileName.append(myFileName)
    fig.savefig(fileName[0], dpi=72)
    

def plot_data(ax, x1, x2, plot_params):

    ind = np.arange(plot_params['xmax_gen'])  # the x locations for the groups
    width = 0.35       # the width of the bars

    rects1 = ax.bar(ind, x1, width, color = plot_params['x1Color'])
    rects2 = ax.bar(ind+width, x2, width, color = plot_params['x2Color'])

    # change xlim to set_xlim
    ax.set_xlim(plot_params['xmin_gen'], plot_params['xmax_gen'])
    ax.set_ylim(plot_params['ymin_gen'], plot_params['ymax_gen'])

    #change xticks to set_xticks
    ax.set_xticks(ind+width)
    ax.set_xticklabels( ('Not Really', '', 'Neutral', '', 'Absolutely') )
    ax.set_yticks(np.arange(plot_params['ymin_gen'], plot_params['ymax_gen']+10, 10))
    legend = ax.legend(plot_params['legend_label'], loc=9);
    ax.set_xlabel(plot_params['xlabel'], fontdict=font)
    ax.set_ylabel(plot_params['ylabel'], fontdict=font)
    ax.set_title(plot_params['title'], fontdict=font)
    ax.legend(loc=9)

    def autolabel(rects):
    # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d%%'%int(height), ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    
    # Pad margins so that markers don't get clipped by the axes
    ax.margins(0.1)
 


def genFigure(key, myFileName, theCategory, theXLabel, x0, x1, myTitle):
    '''
     Function creates a data plot.

        Input:
            key: a string for an instrument like 'blg_1'
            myFileName: the name of the figure to be stored
            theCategory: a string that takes the following values ['_NO_CS', '_CS', '']
            theXLabel: string that should go on the x axis as the label
            x0: datapoints to be plotted represent cs10 information for the dimension and category
            x1: ditto cs61a
            myTitle: the title of our fig
        
        
    '''
    
    params['figure.figsize'] = [6.5, 4.5]

    plt_0_params = {
            'xmin_gen' : 0.0,
            'xmax_gen' : 5.0,
            'ymin_gen' : 0,
            'ymax_gen' : 100,
            'xlabel' : theXLabel[0],
            'ylabel' : 'Scores',
            'title' : '',
            'legend_label': ["CS10", "CS61A"],
            
             # Colors I am playing with seperating the cohorts
            'x1Color' : colors_2[8],
            'x2Color' : colors_2[2] 
            }
    rcParams.update(params)
    fig = figure(dpi=80) # no frame
    ax0 = fig.add_subplot(111)
    fig.suptitle(myTitle, fontdict=font)

    plot_data(ax0, x0, x1, plt_0_params)
    
    fileName = []
    fileName.append(myFileName)
    
    fig.savefig(fileName[0], dpi=72)
    rcParams.update(params)
   


def genGenderFigure(key, myFileName, theCategory, attr, theXLabel, x0, x1, myTitle):
    '''
     Function creates a data plot.

        Input:
            key: a string for an instrument like 'blg_1'
            myFileName: the name of the figure to be stored
            theCategory: a string that takes the following values ['_NO_CS', '_CS', '']
            attr: '_male', '_female', or ''
            theXLabel: string that should go on the x axis as the label
            x0: datapoints to be plotted represent cs10 information for the dimension and category
            x1: ditto cs61a
            myTitle: the title of our fig
        
        
    '''
    params['figure.figsize'] = [6.5, 4.5]
    plt_0_params = {
            'xmin_gen' : 0.0,
            'xmax_gen' : 5.0,
            'ymin_gen' : 0,
            'ymax_gen' : 100,
            'xlabel' : theXLabel[0],
            'ylabel' : 'Scores',
            'title' : '',
            'legend_label': ['CS10', 'CS61A'],
            'x1Color' : colors_1[2],
            'x2Color' : colors_2[0]
        }


    rcParams.update(params)
    fig = figure(dpi=80) # no frame
    ax0 = fig.add_subplot(111)
    fig.suptitle(myTitle, fontdict=font)
    plot_data(ax0, x0, x1, plt_0_params)
        
    fileName = []
    fileName.append(myFileName)
    
    fig.savefig(fileName[0], dpi=72)
    rcParams.update(params)
    

N = 3
x1 = (8, 43, 47)
x2 = (3, 17, 78)
x1Title = 'CS10 Male'
x2Title = 'CS61A Male'
myTitle = ''
myFileName = ''

def worstCaseScenario(N, myFileName, x1, x1Title, x2, x2Title, myTitle):
    '''
     Function creates a data plot.

        Input:
            N:
            myFileName: the name of the figure to be stored
            x0: datapoints to be plotted represent cs10 information for the dimension and category
            x1: ditto cs61a
            myTitle: the title of our fig
        
        
    '''
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars

    #update params figure size to accomodate 2 figures
    params['figure.figsize'] = [6.5, 4.5]
    fig = figure(dpi=80) # no frame
    ax0 = fig.add_subplot(111)

    rects1 = ax0.bar(ind, x1, width, color=colors_2[9])
    rects2 = ax0.bar(ind+width, x2, width, color=colors_2[4])

    # change xlim to set_xlim
    ax0.set_ylim(0, 100)

    #change xticks to set_xticks
    ax0.set_xticks(ind+width)
    ax0.set_xticklabels( ('Negatively', 'Neutral', 'Positively') )
    ax0.set_yticks(np.arange(0, 100+10, 10))
    legend = ax0.legend( (rects1[0], rects2[0]), (x1Title, x2Title) , loc=9);
    ax0.set_ylabel('Scores')
    ax0.legend(loc=9)
    ax0.margins(0.1)

    ax0.set_title(myTitle)

    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax0.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d%%'%int(height),
                ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)

    plt.show()

    fileName = []
    fileName.append(myFileName)
    fig.savefig(fileName[0], dpi=72)
    rcParams.update(params)

    
def genPValues(itemDimension, theCategory):
    
    #import scipy.stats
    temp =[]
    for key in itemDimension:
        CS10Temp = []   
        CS10Temp.append('cs10'+theCategory+'.'+key+'.values')
        CS61aTemp = []
        CS61aTemp.append('cs61a'+theCategory+'.'+key+'.values')

        CS10FemaleTemp = []
        CS10FemaleTemp.append('cs10'+theCategory+'_female'+'.'+key+'.values')
        CS61aFemaleTemp = []
        CS61aFemaleTemp.append('cs61a'+theCategory+'_female'+'.'+key+'.values')
        
        CS10MaleTemp = []
        CS10MaleTemp.append('cs10'+theCategory+'_male'+'.'+key+'.values')
        CS61aMaleTemp = []
        CS61aMaleTemp.append('cs61a'+theCategory+'_male'+'.'+key+'.values')
        
    
        z1, p1 = scipy.stats.mannwhitneyu(eval(CS10Temp[0]),eval(CS61aTemp[0])) 
        p_value1 = p1 * 2
        
        z2, p2 = scipy.stats.mannwhitneyu(eval(CS10FemaleTemp[0]),eval(CS61aFemaleTemp[0])) 
        p_value2 = p2 * 2
            
        z3, p3 = scipy.stats.mannwhitneyu(eval(CS10MaleTemp[0]),eval(CS61aMaleTemp[0])) 
        p_value3 = p3 * 2

        s1 = stars(p1)
        s2 = stars(p2)
        s3 = stars(p3)
        
        print 'Test for significance between CS10 and CS61A\n'
        print key, '\t', dataDescription[key]
        if p_value1 < 0.05:
            print 'Class', '\t', '%.8f' % p_value1, '\t', 'Statistically Significant:',s1 
        if p_value2 < 0.05:
            print 'Female', '\t', '%.8f' % p_value2, '\t', 'Statistically Significant:', s2
        if p_value3 < 0.05:
            print 'Male', '\t', '%.8f' % p_value3, '\t', 'Statistically Significant:', s3
        print '\n'
       
        
def genPValues_2(itemDimension):
    '''
    I am using this function to test for statistical significance between students with prior exposure 
    and students without prior exposure

    ''' 
    temp =[]
    for key in itemDimension:
        CS10_CS_Temp = []   
        CS10_CS_Temp.append('cs10_CS'+'.'+key+'.values')
        CS61a_CS_Temp = []
        CS61a_CS_Temp.append('cs61a_CS'+'.'+key+'.values')
        
        CS10_NO_CS_Temp = []   
        CS10_NO_CS_Temp.append('cs10_NO_CS'+'.'+key+'.values')
        CS61a_NO_CS_Temp = []
        CS61a_NO_CS_Temp.append('cs61a_NO_CS'+'.'+key+'.values')
        
        CS10_CS_FemaleTemp = []
        CS10_CS_FemaleTemp.append('cs10_CS_female'+'.'+key+'.values')
        CS61a_CS_FemaleTemp = []
        CS61a_CS_FemaleTemp.append('cs61a_CS_female'+'.'+key+'.values')
        
        CS10_NO_CS_FemaleTemp = []
        CS10_NO_CS_FemaleTemp.append('cs10_NO_CS_female'+'.'+key+'.values')
        CS61a_NO_CS_FemaleTemp = []
        CS61a_NO_CS_FemaleTemp.append('cs61a_NO_CS_female'+'.'+key+'.values')
        
        CS10_CS_MaleTemp = []
        CS10_CS_MaleTemp.append('cs10_CS_male'+'.'+key+'.values')
        CS61a_CS_MaleTemp = []
        CS61a_CS_MaleTemp.append('cs61a_CS_male'+'.'+key+'.values')
        
        CS10_NO_CS_MaleTemp = []
        CS10_NO_CS_MaleTemp.append('cs10_NO_CS_male'+'.'+key+'.values')
        CS61a_NO_CS_MaleTemp = []
        CS61a_NO_CS_MaleTemp.append('cs61a_NO_CS_male'+'.'+key+'.values')
    
        z_CS, p_CS = scipy.stats.mannwhitneyu(eval(CS10_CS_Temp[0]),eval(CS61a_CS_Temp[0])) 
        p_value1 = p_CS * 2
        z_NO_CS, p_NO_CS = scipy.stats.mannwhitneyu(eval(CS10_NO_CS_Temp[0]),eval(CS61a_NO_CS_Temp[0])) 
        p_value2 = p_NO_CS * 2
        
        z_CSfemale, p_CSfemale = scipy.stats.mannwhitneyu(eval(CS10_CS_FemaleTemp[0]),
                                                          eval(CS61a_CS_FemaleTemp[0])) 
        p_value3 = p_CSfemale * 2
        z_NO_CSfemale, p_NO_CSfemale = scipy.stats.mannwhitneyu(eval(CS10_NO_CS_FemaleTemp[0]),
                                                                eval(CS61a_NO_CS_FemaleTemp[0])) 
        p_value4 = p_NO_CSfemale * 2
        
        z_CSmale, p_CSmale = scipy.stats.mannwhitneyu(eval(CS10_CS_MaleTemp[0]),
                                                      eval(CS61a_CS_MaleTemp[0])) 
        p_value5 = p_CSmale * 2
        z_NO_CSmale, p_NO_CSmale = scipy.stats.mannwhitneyu(eval(CS10_NO_CS_MaleTemp[0]),
                                                            eval(CS61a_NO_CS_MaleTemp[0])) 
        p_value6 = p_NO_CSmale * 2
    

        s1 = stars(p_CS)
        s2 = stars(p_NO_CS)
        s3 = stars(p_CSfemale)
        s4 = stars(p_NO_CSfemale)
        s5 = stars(p_CSmale)
        s6 = stars(p_NO_CSmale)
        
        
       
        print 'Test for significance between CS10 and CS61A\n'
        print key, '\t', dataDescription[key]
        if p_value1 < 0.05:
            print 'Prior CS Class', '\t', '%.5f' % p_value1, '\t', 'Statistically Significant:',s1 
        if p_value2 < 0.05:   
            print 'NoPrior CS Class', '\t', '%.5f' % p_value2, '\t', 'Statistically Significant:', s2
        if p_value3 < 0.05:
            print 'Prior CS Female', '\t', '%.5f' % p_value3, '\t', 'Statistically Significant:', s3
        if p_value4 < 0.05:
            print 'No Prior CS Female', '\t', '%.5f' % p_value4, '\t', 'Statistically Significant:', s4
        if p_value5 < 0.05:
            print 'Prior CS Male', '\t', '%.5f' % p_value5, '\t', 'Statistically Significant:', s5
        if p_value6 < 0.05:
            print 'No Prior CS Male', '\t', '%.5f' % p_value6, '\t', 'Statistically Significant:', s6
        print '\n'
       