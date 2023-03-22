import requests 

# This is the url of the webpage you have visited with the browser
TWITTER_SEARCH = f"https://twitter.com/search?q=SPICEDAcademy"

# Send a get request to the above url
response = requests...

print("The response status is ",response...)

print("The response content is ", response...)