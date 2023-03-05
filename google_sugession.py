import requests
import json
import csv

# file = open("keywords.text")
# query = file.readlines()
# file.close()

query = input('Enter key: ')


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


    #     result = {}
    #     result['no_one'] = searches[0]
    #     result['no_two'] = searches[1]
    #     result['no_three'] = searches[2]
    #     result['no_four'] = searches[3]
    #     result['no_five'] = searches[4]
    #     result['no_six'] = searches[5]
    #     result['no_seven'] = searches[6]
    #     result['no_eight'] = searches[7]
    #     result['no_nine'] = searches[8]
    #     result['no_ten'] = searches[8]
    #     return result
    # else:
    #     return ""


my = makeGoogleRequest(query,"en","US","sh")
#My_data = my[0:]
print(my)

# def google_key(list):
#     file = open('google_data.csv', 'a+', newline='')
#     write = csv.writer(file)
#     write.writerow(list)
#     file.close()

# for q in query:
#     q = q.strip('\n')
#     temp_list = makeGoogleRequest(q,"en","US","sh")

#     data = []
#     for temp in temp_list:
#         data.append(temp)
    #google_key(data)



