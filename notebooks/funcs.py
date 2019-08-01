from pathlib import Path
import os
import sys
import numpy as np
from matplotlib import pyplot as plt
import lasio
import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor
from sklearn.utils import resample
from sklearn.model_selection import train_test_split
from subprocess import call
import seaborn as sns
import matplotlib.cm as cm
import pickle
from scipy import interpolate
from scipy import stats


def load_obj(dirname,name):
    with open(Path(dirname).joinpath(name + '.pkl').as_posix(), 'rb') as f:
        return pickle.load(f)

def save_obj(dirname,obj,name):
    with open(Path(dirname).joinpath(name + '.pkl').as_posix(), 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)



def export_tree(export_dir,reg,max_depth,predictors,prefix='BagTree_',**kwargs):
    #Export graphs
    from sklearn import tree
    fig_suffix = '{numlevels}lvls_{predictors}.png'.format(numlevels=max_depth,predictors='-'.join(predictors))
    tree.export_graphviz(reg,out_file=export_dir.joinpath('tree.dot').as_posix(),filled=True,rounded=True,**kwargs)
    call(['dot', '-Tpng', export_dir.joinpath('tree.dot').as_posix(), '-o',
    export_dir.joinpath(prefix+fig_suffix).as_posix(), '-Gdpi=150'])
    return

def tds2rho_est(tds,m=.692826,b=-220.28):
    return 1e4*m/(tds-b)

def rho2tds_est(rho,m=.692826,b=-220.28):
    return 1e4*m/rho + b

def cond2rho(cond):
    return 1e4/cond
    
def nested_logicals(df,list_of_conditions,func=np.logical_and):
    '''
    Convenience function to nest numpy logical functions
        Input: 
            df
            list_of_conditions
            func: numpy function to be applied
        Output:
            logical mask for the given dataframe
        '''
    out = np.ones(len(list_of_conditions[0]),dtype=bool)
    for i in range(len(list_of_conditions)):
        out = func(out,list_of_conditions[i])
    return out

def interpIntervals(df,interp_cols,group_cols=['Well','Year'],dept_col='DEPT',interval=.5):
    '''
    Interpolates numerical values to a specified resolution (interval) 
    Meant for use with depth-registered well data
        Input:
            df: DataFrame
            interp_cols: list
            group_cols: list
            dept_col: str
            interval: numeric
        Output:
            DataFrame with interpolated rows
    '''
    frames = []
    for key,group in df.groupby(by=group_cols):

        all_cols = group.columns
        dup_cols=[col for col in all_cols if (col not in (interp_cols+[dept_col]))]

        #interpolation
        x_eval = np.arange(group.loc[:,dept_col].values[0],group.loc[:,dept_col].values[-1]+interval,interval)
        xp = group.loc[:,dept_col].values
        y_eval={}
        for col in interp_cols:
            yp = group.loc[:,col].values
            y_eval[col]=np.interp(x_eval,xp,yp)

        #create new DF
        df_out = pd.DataFrame(columns=all_cols)
        df_out = df_out.append([df.loc[group.index[0],dup_cols]]*len(x_eval))
        for col in interp_cols:
            df_out.loc[:,col] = y_eval[col]
        df_out.loc[:,dept_col] = x_eval

        #concatenate frames
        frames.append(df_out)
    return pd.concat(frames).reset_index(drop=True)

def concat_dfs(dfs):
    dfs = [sc_df_interp,df2]
    new_dfs = []
    maxind= 0

    for df in dfs:
        df_index = df.index.values + maxind + 1
        maxind = np.max(df_index)
        df.loc[:,'new_index'] = df_index
        df.set_index('new_index',inplace=True)
        new_dfs.append(df)
    return pd.concat(new_dfs,axis=0,sort=True)

def update_df2(df):
    return df.reset_index().rename(columns={"level_0": "Well"})

def update_FBS(df,TDS_col,breaks= [0,1000,3000,10000,100000],return_vec=False):
    FBS = 10*np.ones(len(df))
    FBS[df.loc[:,TDS_col].isna()] = np.nan
    breaks = np.r_[breaks,1e10]
    for i in range(len(breaks[:-1])):
        FBS[np.logical_and(df.loc[:,TDS_col] >= breaks[i], df.loc[:,TDS_col] < breaks[i+1])] = i
    if return_vec:
        return FBS
    else:
        return df.assign(FBS=FBS)

def bin_wiggle(vec,binsize=.1):
    return np.random.uniform(vec-binsize/2,vec+binsize/2)

def inverse_transform_sampling(data, n_bins=40, n_samples=100):
    hist, bin_edges = np.histogram(data, bins=n_bins, density=True)
    cum_values = np.zeros(bin_edges.shape)
    cum_values[1:] = np.cumsum(hist*np.diff(bin_edges))
    inv_cdf = interpolate.interp1d(cum_values, bin_edges)
    r = np.random.rand(n_samples)
    return inv_cdf(r)

def rmse(true,pred):
    return np.sqrt(np.mean((true-pred)**2))

def x_y_regression(xin,yin,cin,ax=None,msk=None,plotslp=True,returnslope=False,errtype='normpct',slpname='F',kdeplot=False,plotone2one=False,**kwargs):
    if msk is None:
        x=xin
        y=yin
        c=cin
    else:
        x=xin[msk]
        y=yin[msk]
        c=cin[msk]
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    plt.set_cmap('viridis_r')
    if ax is None:
        f,ax = plt.subplots(1,figsize=(5,4))
    else:
        f = plt.gcf()
    if kdeplot:
        sns.kdeplot(x,y)
    plt.scatter(x,y,c=c,**kwargs)
    if errtype=='normpct':
        err = np.round(np.linalg.norm(x-y)/np.linalg.norm(y)*100,1)
    elif errtype=='RMSE':
        err = rmse(y,x)
    if plotone2one:
        l,r = plt.xlim()
#         one2one = np.linspace(x.min(),x.max())
        one2one = np.linspace(l,r)
        plt.plot(one2one,one2one,'k',label='y=x')
    if plotslp:
        plt.plot(x,slope*x + intercept,':k',label='$L_{2}$ best fit')
        plt.text(0.05,.875,'{} = {:.2f} \n{} = {:.2f}'
                 .format(slpname,slope,errtype,err),transform=ax.transAxes)
    else:
        plt.text(0.05,.95,'{} = {:.2f}'
                 .format(errtype, err),transform=ax.transAxes)
    if returnslope:
        return f,ax,slope,intercept
    else:
        return f,ax



# mask_noclay = np.logical_or(df.loc[:,'lith'].str.contains("C"),df.loc[:,'lith'].isna())
nan_cols = ['FRES','lith','RILD']