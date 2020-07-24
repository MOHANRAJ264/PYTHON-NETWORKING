import requests

def post():
    data = {'username':'Vandana','password':'123'}
    r = requests.post('https://httpbin.org/post',data = data)
    print(r.text)
def get():
    data= {'things':2,'total':25}
    r = requests.get('https://httpbin.org/get',params=data)
    print(r.text)
    print(r.url)

if __name__ == "__main__":
    post()
    get()