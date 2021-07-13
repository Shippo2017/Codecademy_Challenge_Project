import numpy as np
import fetchmaker
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency

rottweiler_tl = fetchmaker.get_tail_length('rottweiler')
print(np.mean(rottweiler_tl))
print(np.std(rottweiler_tl))

# Data to the rescue
whippet_rescue = fetchmaker.get_is_rescue('whippet')
num_whippet_rescues = np.count_nonzero(whippet_rescue)
num_whippets = np.size(whippet_rescue)

print(num_whippet_rescues)
print(num_whippets)

# Use a binomial test to test the number of whippet rescues, against our expected percentage, 8%.
print(binom_test(num_whippet_rescues, num_whippets, 0.08))


# Size does matter
w = fetchmaker.get_weight('whippet')
t = fetchmaker.get_weight('terrier')
p = fetchmaker.get_weight('pitbull')

# Perform a comparative numerical test to determine if there is a significant difference. (Anova)
fstat, pval = f_oneway(w, t, p)
print(format(pval, '0.17f'))
print(fstat, pval)

# Now, perform another test to determine which of the pairs of these dog breeds differ from each other (Chi_Square)
v = np.concatenate([w, t, p])
labels = ['whippet'] * len(w) + ['terrier'] * len(t) + ['pitbull'] * len(p)
print(labels)
print(pairwise_tukeyhsd(v, labels, 0.05))


# Categorical dog test
poodle_colors = fetchmaker.get_color('poodle')
shihtzu_colors = fetchmaker.get_color('shihtzu')

color_table = [
  [np.count_nonzero(poodle_colors == 'black'),np.count_nonzero(shihtzu_colors == 'black')], 
  [np.count_nonzero(poodle_colors == 'brown'),np.count_nonzero(shihtzu_colors == 'brown')], 
  [np.count_nonzero(poodle_colors == 'gold'),np.count_nonzero(shihtzu_colors == 'gold')], 
  [np.count_nonzero(poodle_colors == 'grey'),np.count_nonzero(shihtzu_colors == 'grey')], 
  [np.count_nonzero(poodle_colors == 'white'),np.count_nonzero(shihtzu_colors == 'white')]]
print(color_table)

chi2, pval, dof, expected = chi2_contingency(color_table)
print(chi2, pval, dof, expected)
print(pval)


# Extra
