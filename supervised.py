from pymongo import MongoClient



client = MongoClient()
db = client.train_db
coll = db['approved']



dv_key='Loan_Status'
iv_key_001 = 'ApplicantIncome'
iv_key_002 = 'Married'
iv_key_003 = 'Credit_History'

app_income_low_range = 2000

#first find all past applicants with credit history =1
items_ch_is_one = coll.find({'Credit_History':1,"Married":"Yes","ApplicantIncome":{"$gt":2000}})

total_matched_items=0
total_approved=0

for item in items_ch_is_one:
	total_matched_items=total_matched_items+1
	print("lid:%s married:%s income:%d loanstatus:%s"
%(item['Loan_ID'],item['Married'],item['ApplicantIncome'],item['Loan_Status']))
        if item['Loan_Status']=='Y':
		total_approved=total_approved+1

print("approved:%d total:%d"%(total_approved,total_matched_items))


predic_ratio = (float(total_approved)/float(total_matched_items))*100
print("prediction accuracy:%f"%predic_ratio)



