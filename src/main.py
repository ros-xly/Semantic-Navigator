import sys

sys.path.append(
    r"C:\Users\ros.crossley\OneDrive - MMCG\Documents\Github Projects\Semantic-Navigator\src"
)

from parser.tmdl_parser import parse_tmdl_file

customer_table = parse_tmdl_file(
    r"C:\Users\ros.crossley\OneDrive - MMCG\Documents\Github Projects\Semantic-Navigator\samples\simple_model\tables\Customer.tmdl"
)

print(customer_table)
