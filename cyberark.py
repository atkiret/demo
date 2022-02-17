import requests
import json

url = "https://in.epm.cyberark.com/EPM/API/Auth/EPM/Logon"

payload = json.dumps({
  "Username": "kiran.katkar@xoriant.com",
  "Password": "Bcomkat@90",
  "ApplicationID": "Xoriant"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

jsn=response.json()

auth = jsn["EPMAuthenticationResult"]

print(auth)

###################################################

url = "https://in129.epm.cyberark.com/EPM/API/Sets"

payload={}
headers = {
  'Authorization': 'basic 
  'VFUser': '',
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

jsonResponse = response.json()


setid=jsonResponse["Sets"][0]["Id"]


print(txt)


####################


url = "https://in129.epm.cyberark.com/EPM/API/22.1/Sets/02278629-02bd-40d3-9f0f-f9f1cc16e7f8/Events/ThreatDetection?"

payload={}

headers = {
  'Authorization': 'basic 
  'VFUser': '',
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)