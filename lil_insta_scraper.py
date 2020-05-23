import requests
import json
import argparse

parser = argparse.ArgumentParser() #simpler
requiered = parser.add_argument_group('requiered arguments')
parser.add_argument('-s', '--sessionid', help="Your session ID, check the GitHub to know how to get it", required=True) #because we will use an account to simplify 
parser.add_argument('-t', '--target', help="The target you want to spy")
#parser.add_argument('-f', '--file', help="A list of username to spy each one") #will be added soon
args = parser.parse_args()
sessionid = args.sessionid
target = args.target

def FakePhoneSession(sessionid, userid, target):
    cookies = {'sessionid': sessionid} # to be connected to our account 
    headers = {'User-Agent': 'Instagram 64.0.0.14.96'} #that's the header the app use
    r = requests.get("https://i.instagram.com/api/v1/users/"+userid+"/info/", headers=headers, cookies=cookies) #building a request as if we were the app
    info = json.loads(r.text)
    targetinfo = info["user"] #we extract the infos we want 
    if "public_email" in targetinfo:
        if targetinfo["public_email"] != "": #to check if there is a mail
            print("{}'s mail is ".format(target) +targetinfo["public_email"]) #extract the mail from the json
        else:
            print("There is no email there.")
    else:
        print("There is no email there.")
    if "public_phone_number" in targetinfo:
        if targetinfo["public_phone_number"] != "": #to check if there is a phone number
            print("{}'s phone number is +".format(target) +targetinfo["public_phone_country_code"]+targetinfo["public_phone_number"]) #extract the phone number from the json
        else:
            print("There is no phone number there.")
    else:
        print("There is no phone number there.")
    if targetinfo["is_private"] == False: #check if the account is public of private
        print("{} account is public.".format(target))
    else:
        print("{} account is private.".format(target))
    if targetinfo["has_anonymous_profile_picture"] == True: #insta tell us if the account got a pp or a default one 
        print("{} has no profile picture.".format(target))
    else:
        print("There is {}'s profile picture:".format(target))
        print(targetinfo["hd_profile_pic_url_info"]["url"]) #insta app can give us an hd version of the profile picture
        wtpp = input("Do you want to download the profile picture ? [y/n] ")
        if wtpp == "y" or wtpp == "Y" or wtpp == "Yes" or wtpp == "yes":
            downloading = requests.get(targetinfo["hd_profile_pic_url_info"]["url"]) #get the url where the pictire is
            file = open("{}_profile_picture.jpg".format(target), "wb") #open a file 
            file.write(downloading.content) # write the profile picture in it 
            file.close #close the file 
    return(targetinfo) #we return the info to use it later
    

def UserID(target):
    r = requests.get("https://www.instagram.com/{}/?__a=1".format(target)) #requests to a graphQL page to get the ID for FakePhoneSession function
    info = json.loads(r.text)
    id = info["logging_page_id"].strip("profilePage_") #extract the ID 
    print("{}'s ID is ".format(target)+ id) #printing it incase you want it
    return(id)


userid = UserID(target) #give a value to userid for the next function
FakePhoneSession(sessionid, userid, target) 