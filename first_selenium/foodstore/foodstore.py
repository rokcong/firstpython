from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

import time
import mysql.connector

def main():

    driver = webdriver.Chrome()
    url = 'https://map.kakao.com/'
    driver.get(url)
    time.sleep(0.5)
    # 다음지도에서 종각역 맛집 검색
    driver.find_element(By.ID, 'search.keyword.query').send_keys('종각역 맛집')
    driver.find_element(By.ID, 'search.keyword.query').send_keys(Keys.ENTER)
    time.sleep(0.5)

    html = driver.page_source

    # result = [['가게이름', '태그', '주소', '별점', '핸드폰번호'], [], []]
    result = []

    # 가게 이름, 태그, 별점, 주소 , 전화번호 데이터 뽑아오기

    # 전체 페이지 찾기
    soup = BeautifulSoup(html, 'lxml')
    for line in soup.find_all('div', {'class': "section places lst"}):
        # => print(line) ; input()
        html_line = '<html>' + str(line) + '</html>'
        soup2 = BeautifulSoup(html_line, 'lxml')

        # 1) 가게이름 찾기
        # => print(soup2.find_all('a', {'class': "link_name"})) ; input()
        for i, line2 in enumerate(soup2.find_all('a', {'class': "link_name"})):
            line2 = '<html>' + str(line2) + '</html>'
            soup3 = BeautifulSoup(line2, 'lxml').text
            # => print(soup3) ; input()
            result.append([soup3])

        # => print(result); input()
        # => result: [['광화문미진 본점'], ['진진수라 광화문점'], ['청진옥'], ['이문설농탕'], ['서린낙지'], .... ]
        # 2) phone number 찾기
        # phone 전화번호 없는 곳도 있음
        for i, line3 in enumerate(soup2.find_all('span', {'class': "phone"})):
            line3 = '<html>' + str(line3) + '</html>'
            soup4 = BeautifulSoup(line3, 'lxml').text
            result[i].append(soup4)
        # => print(result) ; input()
        # => result: [['광화문미진 본점', '한식'], ['진진수라 광화문점', '한정식'], ['청진옥', '해장국'], ... ]

        # 3) 주소 찾기
        for i, line4 in enumerate(soup2.find_all('p', {'data-id': "address"})):
            line4 = '<html>' + str(line4) + '</html>'
            soup5 = BeautifulSoup(line4, 'lxml').text.strip()
            # => print(soup5) ; input()
            result[i].append(soup5)

        # => print(result) ; input()
        # result: [['광화문미진 본점', '한식', '서울 종로구 종로 19 르메이에르종로타운 1층 116-2,117호'], ....]

        # 4) 별점 찾기
        for i, line5 in enumerate(soup2.find_all('em', {'class': "num"})):
            line5 = '<html>' + str(line5) + '</html>'
            soup6 = BeautifulSoup(line5, 'lxml').text
            result[i].append(soup6)
        # => print(result) ; input()

        # 5) tag 찾기
        for i, line6 in enumerate(soup2.find_all('span', {'class': "subcategory clickable"})):
            line6 = '<html>' + str(line6) + '</html>'
            soup7 = BeautifulSoup(line6, 'lxml').text
            # print(i, soup4) ; input()
            result[i].append(soup7)

        print(result)


# DB Connection

    mydb = mysql.connector.Connect(
        host="AWS_Sever",
        port="AWS_Server_port",
        user="AWS_Server_name",
        password="AWS_Password",
        database="AWS_DateBaseName",

    )
    
    mycursor = mydb.cursor()
    
    sql = "INSERT INTO tt (name, num, addr, star, category) VALUSE (%s, %s, %s, %s, %s)"

    valoutput = [[], [], [], [], [], []]
    for i, inter_list in enumerate(result):
        for j in inter_list:
            valoutput[i].append(j.strip())

    val = []
    for inter_list in valoutput:
        val.append(tuple(inter_list))

    mycursor.executemany(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "was inserted.")


if __name__ == '__main__':
    main()
