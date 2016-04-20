
# coding: utf-8

import scipy.stats
from pandas import DataFrame
import pandas as pd 
# In[10]:

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



def scaleData(theDataFrame):
    # must sort to get index in order
    # I used the sum of everything so that we are comparing real percentages.
    theMin, theMax = theDataFrame.min(), theDataFrame.sum(axis=1) 
 
    for (index, val) in theDataFrame.iteritems():
        theDataFrame[index] = ((val - theMin) / float(theMax - theMin)) * 100
    
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

#Get the description of the column items
dd = pd.read_csv('Data_Describe.csv')
dd.columns = ['dataDecription', 'dataKeys']
dataDescription = {}

for i, row in dd.iterrows():
    #print i, row.dataKeys, row.dataDecription
    dataDescription[dd.dataKeys[i]] = dd.dataDecription[i]
    
print '\n'
del dataDescription['name_2']
del dataDescription['name_1']
del dataDescription['major']
del dataDescription['morecs']
del dataDescription['timestamp']
del dataDescription['consent']
del dataDescription['mtr_2']
del dataDescription['mtr_3']
del dataDescription['mtr_1']
del dataDescription['prcs_3']
del dataDescription['prcs_5']
del dataDescription['prcs_4']
del dataDescription['prcs_2']
del dataDescription['prcs_1']
del dataDescription['reason_class']
del dataDescription['grade']
del dataDescription['gender']
del dataDescription['prepared']


dataDescription['atct_1'] = 'I am good at solving a problem by thinking about similar problems I have solved before.'
dataDescription['atct_7'] = 'I am good at ignoring irrelevant details to solve a problem.'
dataDescription['cltrcmp_2'] = 'I have good cultural competence, or the ability to interact effectively \n with people from diverse backgrounds.'

#for key in dataDescription:
#    print key, dataDescription[key]


def plot_data(ax, x1, x2, plot_params):

    #bars are by default width 0.8, so we'll add 0.5 to the left coordinates
    # so that each bar is centered
    ind = np.arange(plot_params['xmax_gen'])  # the x locations for the groups
    width = 0.5       # the width of the bars

    ax.bar(ind, x1, color = plot_params['x1Color'])
    ax.bar(ind, x2, color = plot_params['x2Color'], alpha=0.7)

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

    # Pad margins so that markers don't get clipped by the axes
    ax.margins(0.1)

    #Set tick colors:
    ax = plt.gca()
    ax.tick_params(axis='x', colors='blue')
    ax.tick_params(axis='y', colors='red')

    #move y-axis ticks to the right
    ax.yaxis.tick_right()


def genPValues(itemDimension, theCategory):
    
    #import scipy.stats
    temp =[]
    for key in itemDimension:
        CS10Temp = []
        CS10Temp.append('cs10'+theCategory+'.'+key+'.values')
        CS61aTemp = []
        CS61aTemp.append('cs61a'+theCategory+'.'+key+'.values')

        CS10FemaleTemp = []
        CS10FemaleTemp.append('cs10'+theCategory+'female'+'.'+key+'.values')
        CS61aFemaleTemp = []
        CS61aFemaleTemp.append('cs61a'+theCategory+'female'+'.'+key+'.values')
        
        CS10MaleTemp = []
        CS10MaleTemp.append('cs10'+theCategory+'male'+'.'+key+'.values')
        CS61aMaleTemp = []
        CS61aMaleTemp.append('cs61a'+theCategory+'male'+'.'+key+'.values')
        
    
        z1, p1 = scipy.stats.mannwhitneyu(eval(CS10Temp[0]),eval(CS61aTemp[0])) 
        p_value1 = p1 * 2
        
        z2, p2 = scipy.stats.mannwhitneyu(eval(CS10FemaleTemp[0]),eval(CS61aFemaleTemp[0])) 
        p_value2 = p2 * 2
        
        z3, p3 = scipy.stats.mannwhitneyu(eval(CS10MaleTemp[0]),eval(CS61aMaleTemp[0])) 
        p_value3 = p3 * 2

        s1 = stars(p1)
        s2 = stars(p2)
        s3 = stars(p3)
        
        f = open('Statistical_Significance.txt', 'wt')
        try:
            print key, '\t', dataDescription[key]
            if p_value1 < 0.05:
                print 'Class', '\t', p_value1, '\t', 'Statistically Significant:',s1 
            if p_value2 < 0.05:
               
                print 'Female', '\t', p_value2, '\t', 'Statistically Significant:', s2
            if p_value3 < 0.05:
               
                print 'Male', '\t', p_value3, '\t', 'Statistically Significant:', s3
            print '\n'
        finally:
            f.close()


theXLabel = ['', '']

def genFigure(itemDimension, dataDescription, theCategory, theXLabel):
    
    temp =[]
    for key in itemDimension:
        temp.append('cs10'+theCategory+'male'+'.'+key+'.value_counts()')
        a = eval(temp[0])
        scaleData(a)
        x0_male = turnArray(a)
        temp = []

        temp.append('cs10'+theCategory+'female'+'.'+key+'.value_counts()')
        b = eval(temp[0])
        scaleData(b)
        x0_female = turnArray(b)
        temp = []

        temp.append('cs61a'+theCategory+'male'+'.'+key+'.value_counts()')
        c = eval(temp[0])
        scaleData(c)
        x1_male = turnArray(c)
        temp = []
        
        temp.append('cs61a'+theCategory+'female'+'.'+key+'.value_counts()')
        d = eval(temp[0])
        scaleData(d)
        x1_female = turnArray(d)
        temp = []
        
        
        #update params figure size to accomodate 2 figures
        params['figure.figsize'] = [11, 4.5]

        plt_0_params = {
            'xmin_gen' : 0.0,
            'xmax_gen' : 5.0,
            'ymin_gen' : 0,
            'ymax_gen' : 100,
            'xlabel' : theXLabel[0],
            'ylabel' : 'Percentage of Respondents',
            'title' : '',
            'legend_label': ["Men", "Women"],
            'x1Color' : colors_2[8],
            'x2Color' : colors_1[3]
            }

        plt_1_params = {
            'xmin_gen' : 0.0,
            'xmax_gen' : 5.0,
            'ymin_gen' : 0,
            'ymax_gen' : 100,
            'xlabel' : theXLabel[1],
            'ylabel' : 'Percentage of Respondents',
            'title' : '',
            'legend_label': ["Men", "Women"],
            'x1Color' : colors_2[8],
            'x2Color' : colors_1[3]
            }


        rcParams.update(params)
        fig = figure(dpi=80) # no frame
        ax0 = fig.add_subplot(121)
        ax1 = fig.add_subplot(122)
        #print key, dataDescription[key]
        fig.suptitle(dataDescription[key], fontdict=font)
        
        plot_data(ax0, x0_male, x0_female, plt_0_params)
        plot_data(ax1, x1_male, x1_female, plt_1_params)
        
        CS10temp = []
        CS10temp.append('cs10'+'.'+key+'.values')
        CS61atemp = []
        CS61atemp.append('cs61a'+'.'+key+'.values')
        
        print CS10temp[0],CS61atemp[0]
        #z, p = scipy.stats.mannwhitneyu(cs10.blg_1.values,cs61a.blg_1.values )
    
        z, p = scipy.stats.mannwhitneyu(eval(CS10temp[0]),eval(CS61atemp[0])) 
        p_value = p * 2

        print 'P value is: %.8f'% p_value
        s = stars(p)
        print s
        if p_value < 0.05:
            ax0.annotate('Statistically\nSignificant\n'+s, xy=(0.1, 80), xytext=(0.1, 80))
        
        fileName = []
        fileName.append(key+theCategory+'.pdf')
        fig.savefig(fileName[0], dpi=72)
        rcParams.update(params)

       
    


def genderFemaleFigure(itemDimension, dataDescription, theCategory, theXLabel):
    
    temp =[]
    for key in itemDimension:
        temp.append('cs10'+theCategory+'female'+'.'+key+'.value_counts()')
        b = eval(temp[0])
        scaleData(b)
        x0_female = turnArray(b)
        temp = []

        temp.append('cs61a'+theCategory+'female'+'.'+key+'.value_counts()')
        d = eval(temp[0])
        scaleData(d)
        x1_female = turnArray(d)
        temp = []
        
        
        #update params figure size to accomodate 2 figures
        params['figure.figsize'] = [6.5, 4.5]
        plt_0_params = {
            'xmin_gen' : 0.0,
            'xmax_gen' : 5.0,
            'ymin_gen' : 0,
            'ymax_gen' : 100,
            'xlabel' : theXLabel[0],
            'ylabel' : '',
            'title' : '',
            'legend_label': ['CS0', 'CS1'],
            'x1Color' : colors_1[3],
            'x2Color' : colors_2[4]
        }


        rcParams.update(params)
        fig = figure(dpi=80) # no frame
        ax0 = fig.add_subplot(111)
        #print key, dataDescription[key]
        fig.suptitle(dataDescription[key], fontdict=font)
        
        plot_data(ax0, x0_female, x1_female, plt_0_params)
        
        CS10temp = []
        CS10temp.append('cs10'+theCategory+'female'+'.'+key+'.values')
        CS61atemp = []
        CS61atemp.append('cs61a'+theCategory+'female'+'.'+key+'.values')
        
        print CS10temp[0],CS61atemp[0]
        #z, p = scipy.stats.mannwhitneyu(cs10.blg_1.values,cs61a.blg_1.values )
    
        z, p = scipy.stats.mannwhitneyu(eval(CS10temp[0]),eval(CS61atemp[0])) 
        p_value = p * 2

        print 'P value is: %.8f'% p_value
        s = stars(p)
        print s
        if p_value < 0.05:
            ax0.annotate('Statistically\nSignificant\n'+s, xy=(0.1, 80), xytext=(0.1, 80))
        
        fileName = []
        fileName.append(key+'female'+theCategory+'.pdf')
        fig.savefig(fileName[0], dpi=72)
        rcParams.update(params)

       
    



def genderMaleFigure(itemDimension, dataDescription, theCategory, theXLabel):
    
    temp =[]
    for key in itemDimension:
        temp.append('cs10'+theCategory+'male'+'.'+key+'.value_counts()')
        b = eval(temp[0])
        scaleData(b)
        x0_male = turnArray(b)
        temp = []

        temp.append('cs61a'+theCategory+'male'+'.'+key+'.value_counts()')
        d = eval(temp[0])
        scaleData(d)
        x1_male = turnArray(d)
        temp = []
        
        
        #update params figure size to accomodate 2 figures
        params['figure.figsize'] = [6.5, 4.5]
        plt_0_params = {
            'xmin_gen' : 0.0,
            'xmax_gen' : 5.0,
            'ymin_gen' : 0,
            'ymax_gen' : 100,
            'xlabel' : theXLabel[1],
            'ylabel' : '',
            'title' : '',
            'legend_label': ['CS0', 'CS1'],
            'x1Color' : colors_1[0],
            'x2Color' : colors_2[9]
        }


        rcParams.update(params)
        fig = figure(dpi=80) # no frame
        ax0 = fig.add_subplot(111)
        #print key, dataDescription[key]
        fig.suptitle(dataDescription[key], fontdict=font)
        
        plot_data(ax0, x0_male, x1_male, plt_0_params)
        
        CS10temp = []
        CS10temp.append('cs10'+theCategory+'male'+'.'+key+'.values')
        CS61atemp = []
        CS61atemp.append('cs61a'+theCategory+'male'+'.'+key+'.values')
        
        print CS10temp[0],CS61atemp[0]
        #z, p = scipy.stats.mannwhitneyu(cs10.blg_1.values,cs61a.blg_1.values )
    
        z, p = scipy.stats.mannwhitneyu(eval(CS10temp[0]),eval(CS61atemp[0])) 
        p_value = p * 2

        print 'P value is: %.8f'% p_value
        s = stars(p)
        print s
        if p_value < 0.05:
            ax0.annotate('Statistically\nSignificant\n'+s, xy=(0.1, 80), xytext=(0.1, 80))
        
        fileName = []
        fileName.append(key+'male'+theCategory+'.pdf')
        fig.savefig(fileName[0], dpi=72)
        rcParams.update(params)

