'''
@author: siddardha.teegela
'''
import requests

def file_uplpad_with_api():
    api_url = 'https://platform.rescale.com/api/v2/files/contents/'
    key = 'api-key'
    try:
        with open('<file-path>','rb') as upload_file:
            response = requests.post(api_url,headers = {'Authorization': 'Token '+key},files={'file': upload_file})
            print(response.status_code)
            print(response.text)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    #pass
    file_uplpad_with_api()
    

'''
Response:
201
{"pathParts":{"path":"user/user_EUuNk/testdoc_api-5cbab800-dd06-4870-87b5-d1daa4d129b3.txt",
"container":"prod-rescale-platform"},"typeId":1,"name":"testdoc_api.txt",
"dateUploaded":"2019-01-28T21:34:04.447607Z","relativePath":"testdoc_api.txt",
"storage":{"storageType":"S3Storage","id":"pCTMk",
"connectionSettings":{"region":"us-east-1"},"encryptionType":"default"},
"decryptedSize":151,"downloadUrl":"https://platform.rescale.com/api/v2/files/PCJNzf/contents/",
"sharedWith":[],"encodedEncryptionKey":"MggLWPwsdYjn8aIlYlwL8kndsvu66i2qAbMAqXj/bgg=",
"owner":"sidhumeher@yahoo.co.in",
"path":"user/user_EUuNk/testdoc_api-5cbab800-dd06-4870-87b5-d1daa4d129b3.txt",
"isUploaded":true,"viewInBrowser":true,"id":"PCJNzf","isDeleted":false,
"md5":"20ae7043ab52c870a79ab94e59a82309"}
'''
