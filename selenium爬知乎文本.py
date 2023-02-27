import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")

chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
service = Service(r'C:\Users\caka\Desktop\文件\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

title = ''
url = 'https://www.zhihu.com/question/37792432'

def get_tags(url):
    global title
    # driver.get(url)
    # 等待页面加载完成
    # 我们使用了presence_of_element_located条件，表示要等待元素出现在页面上，但不需要元素可见。
    # 您也可以使用其他条件，例如visibility_of_element_located，表示要等待元素在页面上可见。
    wait = WebDriverWait(driver, 10)
    # wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(@class, 'Modal-closeButton')]"))).click()
    title = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div[1]/div[2]/div/div[1]/div[1]/h1').text
    # 模拟向下滚动直到页面底部
    n = 0
    while True:
        # 执行JavaScript代码来滚动到页面底部
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # 等待一段时间，让页面加载新内容
        time.sleep(3)
        n += 1
        print('滚动第{}次'.format(n))
        # 检查页面是否已经滚动到底部
        scrolled_to_bottom = driver.execute_script("return window.innerHeight + window.pageYOffset >= document.body.scrollHeight;")
        # 如果已经滚动到底部，停止滚动
        if scrolled_to_bottom:
            break

    # 获取所有p标签
    p_tags = driver.find_elements(By.TAG_NAME, "p")
    return p_tags

def save_txt(p_tags):
    # 遍历p标签并将文本保存到文件
    np = 0
    with open(title + ".txt", "w", encoding="utf-8") as f:
        for p in p_tags:
            p_text = p.text
            if len(p_text) > 1:
                f.write(p.text + "\n")
                np += 1
                if np % 10 == 0:
                    print('写入第{}行'.format(np))
    print('结束')

def main():
    p_tags = get_tags(url)
    save_txt(p_tags)

if __name__ == '__main__':
    main()