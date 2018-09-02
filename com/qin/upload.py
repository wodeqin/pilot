import requests

def imagesUpload(file):
    url = 'http://localhost/api/uploadImg'
    #files = {'images': open(filename, 'rb')}
    files = {'file': open(file, 'rb')}
    # multiple_files = [
    #    ('images', ('11.png', open('11.png', 'rb'), 'image/png')),
    #    ('images', ('desktop.png', open('desktop.png', 'rb'), 'image/png'))
    # ]
    headers = {
        'Api-Key':'InhpeWFuZzA4MDdJBtx4AWlPpI_Oxx1Ki8',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
        'Content-Type':'multipart/form-data'
    }
    # r = requests.post(url, files=multiple_files, headers=headers)
    r = requests.post(url, files=files)
    print(r.text)
    return r