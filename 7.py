# 7. Assuming that we have some email addresses in the "username@companyname.com" 
# format, write a program to print the company name of a given email address. Both user 
# names and company names are composed of letters only. 

srt_name=input("enter a mail address:: ")

result=srt_name.split("@")
user_name=result[0].upper()
company_name=result[1].split(".")[0].upper()

print(f"user_name:: {user_name},company_name:: {company_name}")
