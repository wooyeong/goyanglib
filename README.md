### goyanglib
고양시 사서 공무원을 위한 텔레그램 봇. 고양시 도서관센터 홈페이지에 새로운 민원(의견나눔방)이 올라가면 `@goyanglib` 텔레그램 채널로 알려줍니다.

### goyanglib
Telegram bot for Goyang city librarians. If there are new un-handled requests on the library homepage, it posts them to the `@goyanglib` telegram channel. 

### cron
```cron
*/30 8-18 * * 1-5 ./goyanglib/goyanglib.py 2>&1 | /usr/bin/logger -t goyanglib

```

### Notice
It uses the following softwares under MIT License.
* [BeautifulSoup]
* [twx.botapi]

[BeautifulSoup]: <https://www.crummy.com/software/BeautifulSoup/>
[twx.botapi]: <https://github.com/datamachine/twx.botapi>
