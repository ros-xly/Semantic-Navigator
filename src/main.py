from src.parser.tmdl_parser import parse_tmdl_file

customer_table = parse_tmdl_file(
    "samples/simple_model/tables/Customer.tmdl"
)

print(customer_table)