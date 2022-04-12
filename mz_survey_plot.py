'''
Linear regression with marginal distributions
=============================================

_thumb: .65, .65
'''
import seaborn as sns
sns.set(style='darkgrid')

# tips = sns.load_dataset('tips')
# g = sns.jointplot('total_bill', 'tip', data=tips,
#                   kind='reg', truncate=False,
#                   xlim=(0, 60), ylim=(0, 12),
#                   color='m', height=7)

# data1 = pd.read_csv() #?
data1 = {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'y':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
g = sns.jointplot('x', 'y', data=data1,
                  kind='reg', truncate=False,
                #   xlim=(0, 60), ylim=(0, 12),
                  color='m', height=7)

#TODO use with RT and m/z data