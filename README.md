## sqlalchemy-utils를 이용한 data encrypt
참고 문서 : https://blog.linewalks.com/archives/7645

- POST `/api/identity`</br>
**body**

    ```
  {
    "name": "홍길동",
    "phone_number": "010-1111-2222"
  }
  ```
  -> plain text로 post 요청을 해도 `phone_number`은 `EncryptedType`로 되어있기 때문에 **binary**값으로 저장됨
- GET `/api/identity?name=`
 ```
{
    "id": "01GJCVZPV3JR8R4AAHNZ64PCD7",
    "name": "홍길동",
    "phone_number": "010-1111-2222"
}
``` 
 -> 별도의 decode 값 없이도 return 값이 binary data가 decode된 것으로 반환됨