import noshmishmosh
import numpy as np

# No.4
all_visitors = noshmishmosh.customer_visits

# No.5
paying_visitors = noshmishmosh.purchasing_customers

# No.6 
total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)
print('Total visitors : ', total_visitor_count)
print('Total payments : ', paying_visitor_count)

# No.7
baseline_percent = paying_visitor_count / total_visitor_count * 100.0
print('Baseline = ', baseline_percent)

# No.9
payment_history = noshmishmosh.money_spent

# No.10
average_payment = np.mean(payment_history)
print('Average payment : ', average_payment)

# No.11
new_customer_needed = np.ceil(1240 / average_payment)
print('New customer needed : ', new_customer_needed)

# No.12
percentage_point_increase = new_customer_needed / total_visitor_count * 100
print('Additional percent of weekly visitors : ', percentage_point_increase)

# No.13
mde = percentage_point_increase / baseline_percent * 100
print('Minimum detectable effect : ', mde)

# No.15
significant_threshold = .10

# No.16
ab_sample_size = 490
