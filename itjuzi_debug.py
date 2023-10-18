from login import Login
from crawler import Crawler
import time

d0=Login().pwd_login()
d_p=Crawler(d0)


def person_to_company()->None:
    sample=open("person_sample.txt",'r',encoding='utf-8')
    lst_url=[]
    for line in sample.readlines():
        lst_url.append(line.split('\t')[-1].strip('\n'))
    sample.close()

    newfile=open('sample_person.txt','a+',encoding='utf-8')
    for url in lst_url:
        try:
            num,[region, work, education, firms]=d_p.process_person(url)
            print(num)
        except:
            newfile.write(url+'\t'+'unable to access'+'\n')
            continue
        for i in range(len(firms)):
            newfile.write('No.'+str(i+1)+'\t'+url+'\t'+region+'\t'+work+'\t'+education+'\t'+'///'.join(firms[i])+'\n')
        time.sleep(1)
    newfile.close()
    pass

def company_details()->None:    #文档处理方案是将多余的换行去掉，每个公司只占一行
    sample=open("sample_person_processed.txt",'r',encoding='utf-8')
    lst_url=[]
    for line in sample.readlines():
        if line[0]=="N":
            lst_url.append(line.split('\t')[5].split('///')[2])
        else:
            lst_url.append('nothing')
    sample.close()
    print(lst_url)

    newfile=open('sample_company.txt','a+',encoding='utf-8')
    for url in lst_url:
        try:
            register_name,phone,mail,details,labels,finance_time,turn_now,turn_now_amount,investors,website,address=d_p.process_company(url)
            print(url)
        except:
            newfile.write(url+'\t'+'unable to access'+'\n')
            continue
        newfile.write(url+'\t'+register_name+'\t'+phone+'\t'+mail+'\t'+details+'\t'+('/').join(labels)+'\t'+turn_now+'\t'+turn_now_amount+'\t'+investors+'\t'+address+'\t'+website+'\t'+finance_time+'\n')
        time.sleep(1)
    newfile.close()
    pass

# person_to_company()
company_details()

input('input to end')
d0.quit()