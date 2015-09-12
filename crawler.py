
# coding: utf-8

# In[1]:

'''抓取文档目录，根据目录抓取对应的文章'''

import urllib2
import urllib

from lxml.html import fromstring,make_links_absolute
import lxml
import pdfkit


def get_html_text(url):
    '''根据url获得html代码'''
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3)                 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'    
    headers = { 'User-Agent' : user_agent } 
    req = urllib2.Request(url, headers = headers)    
    try:
        response = urllib2.urlopen(req)
        content = response.read()
    except urllib2.URLError, e:
        if hasattr(e, 'code'):  

            print 'The server couldn\'t fulfill the request.'  

            print 'Error code: ', e.code  

        elif hasattr(e, 'reason'):  

            print 'We failed to reach a server.'  

            print 'Reason: ', e.reason  


        else:  
            print 'No exception was raised.', e.code      
       
    return content


def get_catalogue(url, css):
    '''抓取符合css规则的html代码, 返回目录的链接列表和标题列表'''

    content = get_html_text(url)
    doc = lxml.html.fromstring(content)
    doc.make_links_absolute('http://www.liaoxuefeng.com')
    css_result = doc.cssselect(css)
    href_list = [e.get('href') for e in css_result]
    title_list = [ e.text_content() for e in css_result]
    return(href_list, title_list)

def get_target_html(url, css):
    content = get_html_text(url)
    doc = fromstring(content)
    doc.make_links_absolute('http://www.liaoxuefeng.com')
    css_result = doc.cssselect(css)
    out = lxml.html.tostring(css_result[0], encoding= 'utf-8')
    return out


def bind_html(title_list, div_list):
    
    ''' 将得到的div code 合并并添加title'''
    
    div_code = ''
    for x in range(len(title_list)):
        div_code = div_code + '<div class="chapter"><h2 id="title'+ str(x) + '">' + title_list[x] + '</h2>' + div_list[x] + '</div>' 
    
    return div_code

# 设置打印pdf的样式
css_file = 'css.css'
pre_html = '''
    <html>
      <head>
        <meta name="pdfkit-page-size" content="Legal"/>
        <meta name="pdfkit-orientation" content="Landscape"/>
               <link rel="stylesheet" type="text/css" href="css.css">
      </head>
      <body>
      '''
#设置pdf页面布局
options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None
}

def html2pdf(html_code, file_name):
    '''
    标题和html代码转换成pdf
    '''
#     html = pre_html + body_code + '</body></html>'
    try:
        pdfkit.from_string(html_code, file_name, options=options, css= css_file)
    except  Exception, e:
        print e

def write_html(html_code, file_name):
    f=open(file_name, 'w+')
    f.truncate() 
    f.write(html_code)
    f.close()
    
def generate_content(title_list):
    html_code = '<div class="content"><h2>Content</h2><ul>'
    for ii in range(len(title_list)):
        html_code = html_code + '<li><a href="#title'+ str(ii) + '">'+ title_list[ii] + '</a></li>'
    html_code = html_code + '</ul></div>'
    return html_code


def html_file2pdf(html_name, pdf_name,options = options, css_file=css_file):
    pdfkit.from_file(html_name, pdf_name, options=options, css= css_file)

    


def main():
    css_catalogue = 'div.x-sidebar-left-content ul:nth-child(2) li a'
    url_catalouge = 'http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000'
    (href_list, title_list) = get_catalogue(url_catalouge, css_catalogue)
    css_doc = 'div.x-wiki-content'

    div_list = []
    for ii in range(len(href_list)):
        div_list.append(get_target_html(href_list[ii], css_doc))

    html = bind_html(title_list, div_list)
    html_code = pre_html + generate_content(title_list) +html + '</body></html>'
    write_html(html_code, 'python3.0.html')
    html2pdf(html_code, 'python3.0.pdf')
    html_file2pdf('python3.0.html', 'python3.0.pdf', options, css_file)

if __name__ == '__main__':
    main()







