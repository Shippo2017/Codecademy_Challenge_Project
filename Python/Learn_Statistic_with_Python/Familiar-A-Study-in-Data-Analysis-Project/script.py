import familiar
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency

vein_pack_lifespans = familiar.lifespans(package='vein')

vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)
print(format(vein_pack_test.pvalue, '0.10f'))
print(vein_pack_test)

if vein_pack_test.pvalue < 0.05:
  print("The Vein pack Is Proven To Make You Live Longer!" + '\n')
else:
  print("The Vein Pack Is Probably Good For You Somehow!" + '\n')


# Upselling Familiar: Pumping Life Into The Company
artery_pack_lifespans = familiar.lifespans(package='artery')

package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print(format(package_comparison_results.pvalue, '0.10f'))
print(package_comparison_results)

if package_comparison_results.pvalue < 0.05:
  print('The Artery Package guarantees even stronger results!\n')
else:
  print('The Artery Package is also a great product!\n')

# Benefitting Everyone: A Familiar Problem
iron_contingency_table = familiar.iron_counts_for_package()

chi2, iron_value, dof, expected = chi2_contingency(iron_contingency_table)
print(format(iron_value, '0.20f'))
print(iron_value)

iron_value = chi2_contingency(iron_contingency_table)
print(iron_value)

if iron_value < 0.05:
  print('The Artery Package is proven to make you healtier!')
else:
  print('While we can\'t say The Artery Package will help you, I bet it\'s Nice')
