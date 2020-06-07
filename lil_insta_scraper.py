import requests
import json
import argparse
import webbrowser
import os

parser = argparse.ArgumentParser() #simpler
requiered = parser.add_argument_group('requiered arguments')
parser.add_argument('-s', '--sessionid', help="Your session ID, check the GitHub to know how to get it", required=True) 
parser.add_argument('-t', '--target', help="The target you want to spy")
parser.add_argument('-f', '--file', help="A list of username to spy each one")
args = parser.parse_args()
sessionid = args.sessionid
file = args.file

def FakePhoneSession(sessionid, userid, target):
    cookies = {'sessionid': sessionid} # to be connected to our account 
    headers = {'User-Agent': 'Instagram 64.0.0.14.96'} #that's the header the app use
    r = requests.get("https://i.instagram.com/api/v1/users/"+userid+"/info/", headers=headers, cookies=cookies) #building a request as if we were the app
    info = json.loads(r.text)
    targetinfo = info["user"] #we extract the infos we want 
    return targetinfo

def mailextraction(targetinfo):
    if "public_email" in targetinfo and targetinfo["public_email"] != "": #checking if it's empty
        mail = targetinfo["public_email"]
    else:
        mail = "NULL"
    return mail

def phoneextraction(targetinfo):
    if "public_phone_number" in targetinfo and targetinfo["public_phone_number"] != "":
        phone = "+"+targetinfo["public_phone_country_code"]+targetinfo["public_phone_number"] #checkink & 
    else:
        phone = "NULL"
    return phone

def privateaccount(targetinfo):
    if targetinfo["is_private"] == False: #checking if private
        private = False
    else:
        private = True
    return private

def profilpic(targetinfo):
    if targetinfo["has_anonymous_profile_picture"] == True: #people without profile picture
        profilepicture = "NULL"
    else:
        profilepicture = targetinfo["hd_profile_pic_url_info"]["url"] #instagram give us the HD picture
    return profilepicture

def UserID(target):
    r = requests.get("https://www.instagram.com/{}/?__a=1".format(target)) #requests to a graphQL page to get the ID for FakePhoneSession function
    info = json.loads(r.text)
    id = info["logging_page_id"].strip("profilePage_") #extract the ID 
    print("{}'s ID is ".format(target)+ id) #printing it incase you want it
    fullname = info["graphql"]["user"]["full_name"] #just reading the value 
    following = info["graphql"]["user"]["edge_follow"]["count"]
    followers = info["graphql"]["user"]["edge_followed_by"]["count"]
    print("Full name: ", fullname)
    print("Following: ", following)
    print("Followers: ", followers)
    print("Biography: {}".format(info["graphql"]["user"]["biography"]))
    return(id)

def wirtingfile(target, userid, email, phone, private, profpc, name):
    os.system("mkdir {}".format(target)) #create a dir to stock infos
    f = open("{}/{}.txt".format(target, name), "w") #opening the dir & create the file we want
    f.write('''{}'s ID is {}:
    email: {}
    phone: {}
    private: {}
    profile picture: {}'''.format(target, userid, email, phone, private, profpc)) #writing the infos

def useprofilepic(profilepicture, target):
    a = input("Do you want to see {}'s profile pricture ? [y/n] ".format(target))
    if a == "Y" or a == "y" or a =="Yes" or a == "YES" or a == "yes":
        webbrowser.open_new(profilepicture)
    b = input("Do you want to download {}'s profile picture ? [y/n] ".format(target))
    if b == "Y" or b == "y" or b =="Yes" or b == "YES" or b == "yes":
        r = requests.get(profilepicture)
        pp = open("{}/{}_profile_picture.jpg".format(target, target), "wb")
        pp.write(r.content)
        pp.close

def filereading(file):
    g = open(file)
    lines = g.readlines()
    for line in lines:
        target = line.replace("\n", "")
        userid = UserID(target) 
        targetinfo = FakePhoneSession(sessionid, userid, target) 
        email = mailextraction(targetinfo)
        phone = phoneextraction(targetinfo)
        private = privateaccount(targetinfo)
        profpc = profilpic(targetinfo)
        print('''{}'s ID is {}:
            email: {}
            phone: {}
            private: {}'''.format(target, userid, email, phone, private))
        c = input("Do you want to export the information ? [y/n] ") 
        if c == "Y" or c == "y" or c =="Yes" or c == "YES" or c == "yes":
            name = input("Name the output file: ")
            wirtingfile(target, userid, email, phone, private, profpc, name) #functions that are used to export infos 
            useprofilepic(profpc, target)
        else:
            useprofilepic(profpc, target)
    g.close()

if file:
    filereading(file)
else:
    target = args.target
    userid = UserID(target) #give a value to userid for the next function
    targetinfo = FakePhoneSession(sessionid, userid, target) 
    email = mailextraction(targetinfo)
    phone = phoneextraction(targetinfo)
    private = privateaccount(targetinfo)
    profpc = profilpic(targetinfo)
    print('''{}'s ID is {}:
        email: {}
        phone: {}
        private: {}'''.format(target, userid, email, phone, private))
    c = input("Do you want to export the information ? [y/n] ") 
    if c == "Y" or c == "y" or c =="Yes" or c == "YES" or c == "yes":
        name = input("Name the output file: ")
        wirtingfile(target, userid, email, phone, private, profpc, name) #functions that are used to export infos 
        useprofilepic(profpc, target)
    else:
        useprofilepic(profpc, target)
