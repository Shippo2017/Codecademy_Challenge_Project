import numpy as np

# Bayes' Theorem
# p(A|B) = P(knows the material | answers correctly)


# # probability the student knows the material
# p(A) = P(knows the material) = 60% = 0.6
p_knows_the_material = 0.6

# p(B) = P(answers correctly) = 0.59

# # given the student knows the material, probability she answers correctly
# P(B|A) = P(answers correctly | knows the material) = 1 - 0.15 = 0.85
P_given_answer_correctly_knows_the_material = 1 - 0.15

P_given_answer_correctly_not_know_the_material = 0.2
p_not_know_the_material = 0.4

# # probability of any student answering correctly P(B)
# P(answers correctly | knows the material) * P(knows the material) or (+) P(answers correctly | does not knows the material) * P(does not knows the material) = 0.59
p_answer_correctly = (P_given_answer_correctly_knows_the_material * p_knows_the_material) + \
                    (P_given_answer_correctly_not_know_the_material * p_not_know_the_material)
print(p_answer_correctly)

#P(A|B) = P(B|A) * P(A) / P(B) = 0.85 * 0.6 / 0.59
p_knows_material_given_answer_correctly = (P_given_answer_correctly_knows_the_material * p_knows_the_material) / p_answer_correctly
print('The Probability that she really knows the material :')
print(p_knows_material_given_answer_correctly)
