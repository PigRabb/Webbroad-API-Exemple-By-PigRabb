
import requests
import unittest


class httpMethodsTest(unittest.TestCase):

    def setUp(self):
        self.urlPost = "post/create"
        self.urlCommnet = "post/comment/create"
        self.header = {"Authorization": "Basic c2lyaW1vbmdrb24uc0BrdS50aDoxMjM0NTY3ODk=","Content-Type": "application/json"}
        self.postData  = {"title" : "Calculate","content":"1+1=9"}
        self.commentData = {"post_id":3,"content":"4+1=19"}
   
    def test_post_with_create_post(self) :
        resp = requests.post("http://127.0.0.1:8000/"+self.urlPost,headers=self.header,json=self.postData)
        try:
            self.assertEqual(resp.status_code,201)
        except Exception as ex :
            print("test_post_with_create_post is fail : ",ex)
        else:
            print("test_post_with_create_post is pass")



    def test_other_with_create_post(self) :
        resp = requests.get("http://127.0.0.1:8000/"+self.urlPost)
        try:
            self.assertEqual(resp.status_code,405,"test_get_with_create_post ")
        except Exception as ex :
            print("test_post_with_create_post is fail : ",ex)
        else:
            print("test_other_with_create_post is pass")


    def test_post_with_create_comment(self) :
        resp = requests.post("http://127.0.0.1:8000/"+self.urlPost,headers=self.header,json=self.commentData)
        try:
            self.assertEqual(resp.status_code,201)
        except Exception as ex :
            print("test_post_with_create_comment is fail : ",ex)
        else:
            print("test_post_with_create_comment is pass")



    def test_other_with_create_comment(self) :
        resp = requests.get("http://127.0.0.1:8000/"+self.urlCommnet)
        try:
            self.assertEqual(resp.status_code,405,"test_get_with_create_post ")
        except Exception as ex :
            print("test_post_with_create_comment is fail : ",ex)
        else:
            print("test_other_with_create_comment is pass")


if __name__ == '__main__':
    print("=====Test=====")
    unittest.main()

