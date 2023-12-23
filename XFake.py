import faker 
import argparse 
parser = argparse.ArgumentParser()
parser.add_argument("-l","--language", help="Specify the language country for the generated data")
parser.add_argument("-c", "--country", help="Specify the country for the generated data")

args = parser.parse_args()
c = args.language+'_'+args.country
faker = faker.Faker(c)
fullname = faker.name() 
username = faker.user_name() 
password = faker.password() 
email = faker.email() 
job = faker.job() 
address = faker.address() 
favorite_color = faker.color_name() 
website = faker.domain_name() 
phone_number = faker.phone_number()
pasportnum=  faker.passport_number()
birth_date = faker.date_of_birth()
mobile_number = faker.phone_number()
email = faker.email()
company_name = faker.company()
post_title = faker.job()
postal_address = faker.address()
credit_card_number = faker.credit_card_number()
print("Full Name : {}\n".format(fullname))
print("Username : {}\n".format(username))
print("Password : {}\n".format(password))
print("Email : {}\n".format(email))
print("Job : {}\n".format(job))
print("address : {}\n".format(address.replace("\n" , " - ")))
print("Favrite Color : {}\n".format(favorite_color))
print("Web Site : {}\n".format(website))
print("Birth Date : {}\n".format(birth_date))
print("Mobile Number: {}\n".format(mobile_number))
print("Email : {}\n".format(email))
print("Company Name : {}\n".format(company_name))
print("Post Title : {}\n".format(post_title))
print("Postal Address : {}\n".format(postal_address))
print("Credit Card Number : {}\n".format(credit_card_number))