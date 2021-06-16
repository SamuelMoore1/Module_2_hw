# Import pathlib
from pathlib import Path

#Import fileio
from qualifier.qualifier.utils import fileio

# Import Calculators
from qualifier.qualifier.utils import calculators

# Import Filters
from qualifier.qualifier.filters import credit_score
from qualifier.qualifier.filters import debt_to_income
from qualifier.qualifier.filters import loan_to_value
from qualifier.qualifier.filters import max_loan_size

def test_save_csv():
    qualifying_loans = 'test'
    csvpath = Path("./qualifier/test/qualifying_loans.csv")

    fileio.save_csv(
        csvpath,
        qualifying_loans,
        [
           "lender",
           "max_loan_amount",
           "max_loan_to_value",
           "max_debt_to_income",
           "min_credit_score",
           "interest_rate",
        ]
    )
     # @TODO: Your code here!
    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    bank_data = fileio.load_csv(Path('./Users/samuelmoore/copy_workspace/Module-2 HW/qualifying_loans.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84

    # @TODO: Test the new save_csv code!
    # YOUR CODE HERE!
