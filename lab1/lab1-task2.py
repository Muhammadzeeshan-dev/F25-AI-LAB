def screen_candidate(marks, docs_submitted, valid_cnic, dues_cleared):
    return "Review" if docs_submitted and valid_cnic and dues_cleared and marks >= 70 else "Hold"

test_runs = [
    ("Ahmad", 85, True, True, True),
    ("Ali", 80, True, False, True),
    ("Ahmed", 75, True, True, False),
    ("Ahsa", 70, True, True, True)
]

for record, marks, docs_submitted, valid_cnic, dues_cleared in test_runs:
    result = screen_candidate(marks, docs_submitted, valid_cnic, dues_cleared)
    
    expected_out = "Hold"
    if marks >= 70 and docs_submitted and valid_cnic and dues_cleared:
        expected_out = "Review"
        
    if valid_cnic == False:
        logic_msg = "CNIC Missing"
    elif dues_cleared == False:
        logic_msg = "Dues Pending"
    else:
        logic_msg = "Criteria Met"
        
    print(record, "|", expected_out, "|", result, "|", logic_msg)