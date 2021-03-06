from django.shortcuts import render
import urllib.request
import json
# Create your views here.



def search(request):

    if request.method == 'GET':


        client_id = "DshukL7WQcANLYUiQTsY"
        client_secret = "p5RxLlzjyJ"

        q = request.GET.get('q')
 
        encText = urllib.parse.quote("{}".format(q))
        url = "https://openapi.naver.com/v1/search/news?query=" + encText #json 결과
        movie_api_request = urllib.request.Request(url)
        movie_api_request.add_header("X-Naver-Client-Id", client_id)
        movie_api_request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(movie_api_request)
        rescode = response.getcode()

        if (rescode == 200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            items = result.get('items')

            context = {
                'items':items,
            }

            return render(request, 'openapp/index.html', context=context)
