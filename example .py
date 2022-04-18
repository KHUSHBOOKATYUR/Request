# import requests
# res = requests.get('https://google.com/')
# print("Response of https://google.com/:")
# print(res.status_code)
# res = requests.get('https://amazon.com/')
# print("Response of https://amazon.com/:")
# print(res.status_code)
# res = requests.get('https://w3resource.com/')
# print("Response of https://w3resource.com/:")
# print(res.status_code)
# print("\nMethods and attributes available to objects on successful\nrequest of https://w3resource.com:\n")
# print(dir(res))  

# import requests
# res = requests.get('https://google.com/')
# print("Response of https://google.com/:")
# print(res.status_code)
# res = requests.get('https://amazon.com/')
# print("Response of https://amazon.com/:")
# print(res.status_code)
# res = requests.get('https://w3resource.com/')
# print("Response of https://w3resource.com/:")
# print(res.status_code)
# print("\nMethods and attributes available to objects on successful\nrequest of https://w3resource.com:\n")
# print(dir(res))  



# import requests
# url = 'http://httpbin.org/cookies'
# my_cookies = dict(cookies_are='Cookies parameter use to send cookies to the server')
# r = requests.get(url, cookies = my_cookies)
# print(r.text)


# import requests
# print("timeout = 0.001")
# try:
#     r = requests.get('https://github.com/', timeout = 0.001)
#     print(r.text)
# except requests.exceptions.RequestException as e:
#     print(e)    

# print("\ntimeout = 1.0")    
# try:
#     r = requests.get('https://github.com/', timeout = 1.0)
#     print("Connected....!")
# except requests.exceptions.RequestException as e:
#     print(e)


# import requests
# x = requests.get('http://saral.navgurukul.org/api/courses/74/exercises')
# print(x.text)
# print("Response of http://saral.navgurukul.org/api/courses/74/exercises :")
# print(x.status_code)


import requests
x = requests.get('https://w3schools.com/python/demopage.htm')
print(x.text)
 