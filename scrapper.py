import requests
from bs4 import BeautifulSoup
import math


LIMIT = 10


def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    result_number = soup.find("div", {"id": "searchCountPages"})
    result_string = result_number.text
    result_split = result_string.split()
    result_str = result_split[-1].rstrip("건")
    result_int = int(result_str.replace(",", ""))
    result_page = (math.ceil(result_int/15)-1)*10

    indeed_result_page = requests.get(
        f"{url}&start={result_page}")
    indeed_result_page_soup = BeautifulSoup(
        indeed_result_page.text, "html.parser")
    result_pagination = indeed_result_page_soup.find(
        "div", {"class": "pagination"})
    result_last_page = result_pagination.find("b", {"aria-current": "true"})
    max_page = int(result_last_page.text)
    print(f"Last page is {max_page}")
    return max_page


""" pagination = indeed_soup.find("div", {"class":"pagination"})

links = pagination.find_all("a")

pages = []

for link in links[:-1] :
    pages.append(int(link.string))
    
max_page = pages[-1] 
마지막 페이지가 끝까지 다나올 경우 노마드코더가 알려준 방식 현재는 사용이 안됨"""


def extract_job(html):
    title = html.find("span")["title"]
    company = html.find("span", {"class": "companyName"}).string
    location = html.find(
        "div", {"class": "companyLocation"}).string
    # 노마드 코드는 location 역시 None값이 있어 잘보고 뽑아줬음
    job_id = html.find("a")["data-jk"]
    return {"title": title, "company": company, "location": location, "link": f"https://kr.indeed.com/viewjob?jk={job_id}"}

    """
    compayny_anchor = compayny_anchor
    if compayny_anchor is not None:
        company = (str(compayny_anchor.string))
    else:
        company = (str(company.string))
        노마드 코드 영상 코드 h태크 안에 있는 회사명이 랑크가 돼있는 게있고,
        링크가 안될시 span으로 둘라쎃여씨는게 있었음 현재는 모두 span에 들어가는듯
    company=company.strip()
    노마드는 스페이스가 너무 많이 나왔음 그래서 공간 삭제"""


def extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping page {page}")
        result = requests.get(f"{url}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "job_seen_beacon"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs(word):
    url = f"https://kr.indeed.com/jobs?q={word}"
    last_page = get_last_page(url)
    jobs = extract_jobs(last_page, url)
    return jobs
