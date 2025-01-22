# cors-proxy-lambda

Lambda for proxying CORS requests

## Usage

```js
const response = await fetch(`${CORS_PROXY_URL}/${URL}`, {
    method: 'GET',
    headers: {
        'XCookie': MY_COOKIE
    }
});
```
