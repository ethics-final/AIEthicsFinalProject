import pandas as pd

def calc_disparate_impact(df, feature, target):
    '''
    Priviledged group/Favorable outcome = 1
    Unpriviledged group/Unfavorable outcome = 0
    '''
    unpriv_df = df[df[feature] == 0]
    unpriv_group_fav_outcome_rate = unpriv_df[target].sum() / float(unpriv_df.shape[0])
    
    priv_df = df[df[feature] == 1]
    priv_group_fav_outcome_rate = priv_df[target].sum() / float(priv_df.shape[0])
    
    return unpriv_group_fav_outcome_rate / priv_group_fav_outcome_rate


def calc_statistical_parity_difference(df, feature, target):
    unpriv_df = df[df[feature] == 0]
    unpriv_group_fav_outcome_rate = unpriv_df[target].sum() / float(unpriv_df.shape[0])
    
    priv_df = df[df[feature] == 1]
    priv_group_fav_outcome_rate = priv_df[target].sum() / float(priv_df.shape[0])
    
    # TODO: should this be priv - unpriv?
    return unpriv_group_fav_outcome_rate - priv_group_fav_outcome_rate