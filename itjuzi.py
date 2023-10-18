from login import Login
from crawler import Crawler
import time

d0=Login().pwd_login()
d_p=Crawler(d0)

global source,person_infos,result
source=open('person_sample.txt','r',encoding='utf-8')
person_infos={}
for line in source.readlines():
    lst=line.split('\t')
    name=lst[0]
    brief_intro=lst[2]
    turn=lst[4]
    person_infos[line.split('\t')[-1].strip('\n')]=[name,brief_intro,turn]
source.close()
result=open("result_source.txt",'a+',encoding='utf-8')
result.write('姓名\t项目名称\t注册名\t手机号\t邮箱\t个人主页\t项目简介\t赛道关键词\t成立时间\t当前轮次\t融资额\t投资机构\t通讯地址\t创业者城市\t公司官网\t是否连续创业者\n')

if __name__=="__main__":
    for url_p in list(person_infos.keys()):
        try:    #projects[i]=[project_name,v1,company_url,founding_date,v2,v3]
            num,[intro_p, region_p, v1, v2, projects]=d_p.process_person(url_p)
            time.sleep(0.5)
        except:
            del person_infos[url_p]
            continue
        for item in range(num):
            project=projects[item]
            project_name=project[0]
            company_url=project[2]
            founding_date=project[3]
            # get into the page of the company
            try:
                register_name,phone,mail,detail_c,labels,finance_time,turn_now,turn_now_amount,investors,website,address=d_p.process_company(company_url)
            except:
                print(company_url)
                continue
            # decisions
            var10=turn_now if turn_now!='empty' else person_infos[url_p][2]
            var13=address if address!='empty' else region_p
            var15=website if website!='empty' else company_url
            var16='Y' if num>=2 else 'N'
            result.write(person_infos[url_p][0]+'\t'+project_name+'\t'+register_name+'\t'+phone+'\t'+mail+'\t'+f'{person_infos[url_p][1]},{intro_p},({url_p})'+'\t'+detail_c+'\t'+'/'.join(labels)+'\t'+founding_date+'\t'+var10+'\t'+turn_now_amount+'\t'+'/'.join(investors)+'\t'+var13+'\t'+region_p+'\t'+var15+'\t'+var16+'\n')
    pass

result.close()
input('input to end')
d0.quit()