from django.shortcuts import render

import requests
import json

def makeGoogleRequest(query, language, country, context):
    URL=f'http://google.com/complete/search?output=toolbar&gl=COUNTRY&q={query}'
    PARAMS = {"client": "firefox",
            "hl": language,
            "q": query,
            "gl": country,
            "ds": context}
    headers = {'User-agent':'Mozilla/5.0'}
    response = requests.get(URL, params=PARAMS, headers=headers)
    if response.status_code == 200:
        searches = json.loads(response.content.decode('utf-8'))[1]

        results = {}
        for i in range(10):
            if i < len(searches):
                results[f'no_{i+1}'] = searches[i]
            else:
                results[f'no_{i+1}'] = ''
        return results
    else:
        return ""


# Create your views here.

def app_home(request):
    if request.method == "GET" and 'query' in request.GET:
        query = request.GET.get('query')
        language = request.GET.get('language')
        country = request.GET.get('country')
        context = request.GET.get('context')
        results = makeGoogleRequest(query, language, country, context)
        my_context = {'results':results} 

    else:
        my_context={}        


    return render(request, 'index.html', my_context)