"""from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'trial1/home.html');
    
"""
from django.shortcuts import render
#from models import FilesInventory
#from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template import Context, loader
from .forms import fileForm
#for converting DF to table
import dash
import dash_table
import datetime
import time
import timeit
import os
from django.conf import settings
from IPython.display import HTML
#from textblob import TextBlob
import json
def SingleFile(request):
    if request.method == 'POST':
        Form_S = fileForm(request.POST, request.FILES)
        if Form_S.is_valid():
            Form_S.save()
            Form_S = fileForm()           
            F_Name = str(request.FILES['File1'].name)
            
            Current_time = time.strftime("%Y%m%d-%H%M%S")
            time_details = str(Current_time)            
            F_prefix = os.path.splitext(F_Name)[0]
            F_suffix = os.path.splitext(F_Name)[1]
            changed_name = F_prefix + time_details + F_suffix
            changed_name1 = F_prefix + F_suffix
            #current_dir=os.getcwd()
            current_dir = r'C:\Project\django\prototype1'
            #dir_name = os.path.join(current_dir,'/trial1/media')
            os.chdir(r'C:\Project\django\prototype1\trial1\media')            
            os.rename(F_Name,changed_name1) 
            os.chdir(current_dir)
            #fileName = '/trial1/media'+ changed_name
            #text_file = os.path.splitext(fileName)[0]+".txt"
            fileURL = 'http://127.0.0.1:8000' + settings.MEDIA_URL + changed_name    
            fileURL1 = 'C:/Project/django/prototype1/trial1/media/'  + changed_name1

            #----------------------------------changed on Oct 11, stylized dataframe display---------------------------------------

            import pandas as pd
            import numpy as np
            import seaborn as sb

            cm = sb.light_palette("maroon", as_cmap=True)
            def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
            def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
            with open(r'C:\Project\django\DSA\imperative.csv', encoding="utf-8") as lst_wrds:
                phrases=lst_wrds.readlines()
                
            with open(r'C:\Project\django\prototype1\trial1\media\bank\weakphrase.txt', encoding="utf-8") as lst1_wrds: 
                weakwords=lst1_wrds.readlines()
            with open(r'C:\Project\django\prototype1\trial1\media\bank\Directive.txt', encoding="utf-8") as lst2_wrds: 
                directive=lst2_wrds.readlines()    

            with open(r'C:\Project\django\prototype1\trial1\media\bank\buzzwords.txt', encoding="utf-8") as lst2_wrds: 
                buzzwords=lst2_wrds.readlines()           
             
            with open(r'C:\Project\django\prototype1\trial1\media\bank\compound_requirements.txt', encoding="utf-8") as lst2_wrds: 
                comp_req=lst2_wrds.readlines()   
                
            with open(r'C:\Project\django\prototype1\trial1\media\bank\Continuance.txt', encoding="utf-8") as lst2_wrds: 
                Continuance=lst2_wrds.readlines()  

            with open(r'C:\Project\django\prototype1\trial1\media\bank\Incompleteness.txt', encoding="utf-8") as lst2_wrds: 
                Incompleteness=lst2_wrds.readlines()    

            with open(r'C:\Project\django\prototype1\trial1\media\bank\option.txt', encoding="utf-8") as lst2_wrds: 
                option=lst2_wrds.readlines()   

            #for lines in phrases:
            #    print(lines)
            with open(fileURL1,encoding='utf-8') as business:
                b1=business.read()
            lst1=[]
            lst2=[]
            lst3=[]
            lst4=[]
            lst5=[]
            lst6=[]
            lst7=[]
            lst8=[]

            phrases = [x.lower() for x in phrases]
            weakwords = [x.lower() for x in weakwords]
            directive = [x.lower() for x in directive]
            buzzwords = [x.lower() for x in buzzwords]
            comp_req = [x.lower() for x in comp_req]
            Continuance = [x.lower() for x in Continuance]
            Incompleteness = [x.lower() for x in Incompleteness]
            option = [x.lower() for x in option]

            #print(phrases)
            for lines in phrases:
                wrds_in_phrase = len(lines.split(' '))
                #print( wrds_in_phrase, lines)
                wrds=b1.lower().split()
                grpd_wrds = [' '.join(wrds[i:i+wrds_in_phrase]) for i in range (0,len(wrds))]
                counter=grpd_wrds.count(lines.strip())
                #print('{} \n found in document {} times'.format(lines.strip(),counter))
                lst1.append([lines.strip(),'Imperative',counter])
            for lines in weakwords:
                wrds_in_phrase=len(lines.split(' '))
                wrds=b1.lower().split()
                grpd_wrds = [' '.join(wrds[i:i+wrds_in_phrase]) for i in range (0,len(wrds))]
                counter=grpd_wrds.count(lines.strip())
                #print('{} \n found in document {} times'.format(lines.strip(),counter))
                lst2.append([lines.strip(),'Weak',counter])
            for lines in directive:
                wrds_in_phrase = len(lines.split(' '))
                #print( wrds_in_phrase, lines)
                wrds=b1.lower().split()
                grpd_wrds = [' '.join(wrds[i:i+wrds_in_phrase]) for i in range (0,len(wrds))]
                counter=grpd_wrds.count(lines.strip())
                #print('{} \n found in document {} times'.format(lines.strip(),counter))
                lst3.append([lines.strip(),'Directive',counter])  

            for lines in buzzwords:
                wrds_in_phrase = len(lines.split(' '))
                #print( wrds_in_phrase, lines)
                wrds=b1.lower().split()
                grpd_wrds = [' '.join(wrds[i:i+wrds_in_phrase]) for i in range (0,len(wrds))]
                counter=grpd_wrds.count(lines.strip())
                #print('{} \n found in document {} times'.format(lines.strip(),counter))
                lst4.append([lines.strip(),'Buzzwords',counter])  

            for lines in comp_req:
                wrds_in_phrase = len(lines.split(' '))
                #print( wrds_in_phrase, lines)
                wrds=b1.lower().split()
                grpd_wrds = [' '.join(wrds[i:i+wrds_in_phrase]) for i in range (0,len(wrds))]
                counter=grpd_wrds.count(lines.strip())
                #print('{} \n found in document {} times'.format(lines.strip(),counter))
                lst5.append([lines.strip(),'compound_requirements',counter])  

            for lines in Continuance:
                wrds_in_phrase = len(lines.split(' '))
                #print( wrds_in_phrase, lines)
                wrds=b1.lower().split()
                grpd_wrds = [' '.join(wrds[i:i+wrds_in_phrase]) for i in range (0,len(wrds))]
                counter=grpd_wrds.count(lines.strip())
                #print('{} \n found in document {} times'.format(lines.strip(),counter))
                lst6.append([lines.strip(),'Continuance',counter])  

            for lines in Incompleteness:
                wrds_in_phrase = len(lines.split(' '))
                #print( wrds_in_phrase, lines)
                wrds=b1.lower().split()
                grpd_wrds = [' '.join(wrds[i:i+wrds_in_phrase]) for i in range (0,len(wrds))]
                counter=grpd_wrds.count(lines.strip())
                #print('{} \n found in document {} times'.format(lines.strip(),counter))
                lst7.append([lines.strip(),'Incompleteness',counter]) 

            for lines in option:
                wrds_in_phrase = len(lines.split(' '))
                #print( wrds_in_phrase, lines)
                wrds=b1.lower().split()
                grpd_wrds = [' '.join(wrds[i:i+wrds_in_phrase]) for i in range (0,len(wrds))]
                counter=grpd_wrds.count(lines.strip())
                #print('{} \n found in document {} times'.format(lines.strip(),counter))
                lst8.append([lines.strip(),'option',counter])                
                
            #print(lst1)
            cm = sb.light_palette("blue", as_cmap=True)
            df=pd.DataFrame(lst1,columns=['Phrase','Type','Count'])
            df=df[df['Count']>0]
            styled_df=df.style.hide_index().background_gradient(cmap=cm).apply(lambda x: ["color: maroon" if v == x['Phrase'] else "" for v in x], axis = 1)
            with open(r"C:\Project\django\prototype1\trial1\templates\trial1\df1.html", "w") as file:
                file.write(styled_df.render())
            template = loader.get_template("./trial1/df1.html")
            #styled_df
            
            '''data = df.to_html(classes="table table-striped table-hover")
                                                with open("C:/Users/sumeetku/Videos/prototype1/prototype1/trial1/templates/trial1/df.html", "w") as file:
                                                    file.write(styled_df.render())
                                                template = loader.get_template("C:/Users/sumeetku/Videos/prototype1/prototype1/trial1/templates/trial1/file.html")'''
            #return HttpResponse(template.render())

            df1=pd.DataFrame(lst2,columns=['Phrase','Type','Count'])
            df1=df1[df1['Count']>0]
            #styled_df2.render()
            #data1 = df1.to_html(classes="table table-striped table-hover")
            

            
            #prCyan(df[df['Count']>0])
            #print("------------------------------------------------------Weakphrases---------------------------------------------------------")
            styled_df1=df1.style.hide_index().background_gradient(cmap=cm).apply(lambda x: ["color: blue" if v == x['Phrase'] else "" for v in x], axis = 1)
            #styled_df2
            with open(r"C:\Project\django\prototype1\trial1\templates\trial1\df2.html", "w") as file:
                file.write(styled_df1.render())
            template1 = loader.get_template("./trial1/df2.html")
            '''context = {'uploaded_file_url':fileURL,'text': strng}  
            #return render(request, 'trial1/simple_upload.html', {'text': strng},context)    
            return render(request, 'trial1/simple_upload.html', context)    '''     
            df2=pd.DataFrame(lst3,columns=['Phrase','Type','Count'])
            df2=df2[df2['Count']>0]
            styled_df2=df2.style.hide_index().background_gradient(cmap=cm).apply(lambda x: ["color: maroon" if v == x['Phrase'] else "" for v in x], axis = 1)
            #styled_df
            with open(r"C:\Project\django\prototype1\trial1\templates\trial1\df3.html", "w") as file:
                file.write(styled_df2.render())
            template2 = loader.get_template("./trial1/df3.html")

            df3=pd.DataFrame(lst4,columns=['Phrase','Type','Count'])
            df3=df3[df3['Count']>0]
            styled_df3=df3.style.hide_index().background_gradient(cmap=cm).apply(lambda x: ["color: maroon" if v == x['Phrase'] else "" for v in x], axis = 1)
            #styled_df
            with open(r"C:\Project\django\prototype1\trial1\templates\trial1\df4.html", "w") as file:
                file.write(styled_df3.render())
            template3 = loader.get_template("./trial1/df4.html")

            df4=pd.DataFrame(lst5,columns=['Phrase','Type','Count'])
            df4=df4[df4['Count']>0]
            styled_df4=df4.style.hide_index().background_gradient(cmap=cm).apply(lambda x: ["color: maroon" if v == x['Phrase'] else "" for v in x], axis = 1)
            #styled_df
            with open(r"C:\Project\django\prototype1\trial1\templates\trial1\df5.html", "w") as file:
                file.write(styled_df4.render())
            template4 = loader.get_template("./trial1/df5.html")

            df5=pd.DataFrame(lst6,columns=['Phrase','Type','Count'])
            df5=df5[df5['Count']>0]
            styled_df5=df5.style.hide_index().background_gradient(cmap=cm).apply(lambda x: ["color: maroon" if v == x['Phrase'] else "" for v in x], axis = 1)
            #styled_df
            with open(r"C:\Project\django\prototype1\trial1\templates\trial1\df6.html", "w") as file:
                file.write(styled_df5.render())
            template5 = loader.get_template("./trial1/df6.html")

            df6=pd.DataFrame(lst7,columns=['Phrase','Type','Count'])
            df6=df6[df6['Count']>0]
            styled_df6=df6.style.hide_index().background_gradient(cmap=cm).apply(lambda x: ["color: maroon" if v == x['Phrase'] else "" for v in x], axis = 1)
            #styled_df
            with open(r"C:\Project\django\prototype1\trial1\templates\trial1\df7.html", "w") as file:
                file.write(styled_df6.render())
            template6 = loader.get_template("./trial1/df7.html")

            df7=pd.DataFrame(lst8,columns=['Phrase','Type','Count'])
            df7=df7[df7['Count']>0]
            styled_df7=df7.style.hide_index().background_gradient(cmap=cm).apply(lambda x: ["color: maroon" if v == x['Phrase'] else "" for v in x], axis = 1)
            #styled_df
            with open(r"C:\Project\django\prototype1\trial1\templates\trial1\df8.html", "w") as file:
                file.write(styled_df7.render())
            template7 = loader.get_template("./trial1/df8.html")



            new_df = pd.concat([df,df1,df2,df3,df4,df5,df6,df7]) 
    
            filename = r"C:\Project\django\prototype1\trial1\new_json"

            def to_flare_json(new_df,filename):
                """Convert dataframe into nested JSON as in flare files used for D3.js"""
                flare = dict()
                d = {"name":"phrases", "children": []}
                
                for index, row in new_df.iterrows():
                    parent = row[1]
                    child = row[0]
                    child_size = row[2]
                

                    # Make a list of keys
                    key_list = []
                    for item in d['children']:
                        key_list.append(item['name'])

                    #if 'parent' is NOT a key in flare.JSON, append it
                    if not parent in key_list:
                        d['children'].append({"name": parent, "children":[{"size": child_size, "name": child}]})
                    # if parent IS a key in flare.json, add a new child to it
                    else:
                        d['children'][key_list.index(parent)]['children'].append({"size": child_size, "name": child})
                flare = d
                # export the final result to a json file
                with open(filename +'.json', 'w') as outfile:
                    json.dump(flare, outfile, indent=4)
                return ("Done")
                   
            to_flare_json(new_df,filename)  

            #-------------------------------------Generic Structure Analysis--------------------------------------------------
            import re
            start_time=time.time()
            gsa_list=[]
            gsa_str=''
            my_list =[]
            level1_count,level2_count,level3_count,level4_count,level5_count,level6_count = 0,0,0,0,0,0

            for words in (b1.split()):
                #level 1 req
                pattern1= '^\d$|^\d\.0$'
                result1 =re.match(pattern1,words)
                if result1 :
                    level1_count=level1_count+1 
                #level 2 req
                pattern = '^\d\.[123456789]$'
                result = re.match(pattern, words)
                if result:
                    #print(words)
                    level2_count = level2_count+1
                #level 3 req
                pattern3='^\d\.\d\.\d$'
                result3 = re.match(pattern3,words)
                if result3 : 
                    level3_count=level3_count+1
                #level 4 req
                pattern4='^\d\.\d\.\d\.\d$'
                result4=re.match(pattern4,words)
                if result4 :
                    level4_count=level4_count+1
                #level 5 req 
                pattern5 = '^\d\.\d\.\d\.\d\.\d$'
                result5=re.match(pattern5,words)
                if result5:
                    level5_count=level5_count+1
                    #level 6 req
                pattern6='^\d\.\d\.\d\.\d\.\d\.\d$'
                result6=re.match(pattern6,words)
                if result6:
                    level6_count=level6_count+1

            my_list.append(level1_count*10)
            my_list.append(level2_count*10)
            my_list.append(level3_count*10)
            my_list.append(level4_count*10)
            my_list.append(level5_count*10)
            my_list.append(level6_count*10)
            dafa=pd.DataFrame( [my_list])

            print('The Count or the depth of levels:')
            print('Level-1: {0}\nLevel-2: {1}\nLevel-3: {2}\nLevel-4: {3}\nLevel-5: {4}\nLevel-6: {5}' .format(level1_count, level2_count, level3_count, level4_count, level5_count, level6_count))
            print("Time to run: %s seconds ---" % (time.time() - start_time))
            gsa_list.append('The Count or the depth of levels:')
            gsa_list.append('Level-1: {0}\nLevel-2: {1}\nLevel-3: {2}\nLevel-4: {3}\nLevel-5: {4}\nLevel-6: {5}' .format(level1_count, level2_count, level3_count, level4_count, level5_count, level6_count))
            gsa_list.append("Time to run: %s seconds ---" % (time.time() - start_time))

            for i in gsa_list:
                gsa_str=gsa_str + str(i) + '\n'
            dafa.to_csv(r'C:\Project\django\prototype1\trial1\file1.csv',index = False, header = False)
#-----------------------------------------------------Duplicate phrases-----------------------------------------------------------
            '''start_time=time.time()
            lst=b1.lower().split()
            dp_list=[]
            str_new=''
            dup_count = {k:lst.count(k) for k in lst}
            for key,value in dup_count.items():
                if(value>1):
                    #print('"%s" Occurs %d times' % (key,value))
                    dp_list.append('"%s" Occurs %d times' % (key,value))

            words = b1.lower().replace('.','').split()
            grp_wrd = [' '.join(words[i: i + 3]) for i in range(0, len(words))]
            dup_count = {k:grp_wrd.count(k) for k in grp_wrd}
            for key,value in dup_count.items():
                if(value>1):
                    #print('"%s" Occurs %d times' % (key,value))
                    dp_list.append('"%s" Occurs %d times' % (key,value))
            #print("------------------------------------------------------------------------------------------------------------\n\n For 2 word phrases:\n")
            grp_wrd = [' '.join(words[i: i + 2]) for i in range(0, len(words), 3)]
            dup_count = {k:grp_wrd.count(k) for k in grp_wrd}
            for key,value in dup_count.items():
                if(value>1):
                    #print('"%s" Occurs %d times' % (key,value))
                    dp_list.append('"%s" Occurs %d times' % (key,value))
            dp_list.append("Time to run: %s seconds ---" % (time.time() - start_time))

            #dp_list=set(dp_list) 
            for i in dp_list:
                str_new=str_new + str(i) + '\n' '''
            start_time=time.time()
            lst=b1.lower().split()
            dp_list=[]
            new_dp_lst = []
            str_new=''
            dup_count = {k:lst.count(k) for k in lst}
            for key,value in dup_count.items():
                if(value>1):
                    dp_list.append('"%s" Occurs %d times' % (key,value))
                    new_dp_lst.append([key, value,1])

            words = b1.lower().replace('.','').split()
            grp_wrd = [' '.join(words[i: i + 3]) for i in range(0, len(words))]
            dup_count = {k:grp_wrd.count(k) for k in grp_wrd}
            for key,value in dup_count.items():
                if(value>1):
                                #print('"%s" Occurs %d times' % (key,value))
                    dp_list.append('"%s" Occurs %d times' % (key,value))
                    new_dp_lst.append([key, value,3])
                        #print("------------------------------------------------------------------------------------------------------------\n\n For 2 word phrases:\n")
            grp_wrd = [' '.join(words[i: i + 2]) for i in range(0, len(words), 3)]
            dup_count = {k:grp_wrd.count(k) for k in grp_wrd}
            for key,value in dup_count.items():
                if(value>1):
                                #print('"%s" Occurs %d times' % (key,value))
                    dp_list.append('"%s" Occurs %d times' % (key,value))
                    new_dp_lst.append([key, value,2])
            dp_list.append("Time to run: %s seconds ---" % (time.time() - start_time))

                        #dp_list=set(dp_list) 
            for i in dp_list:
                str_new=str_new + str(i) + '\n'
                    
            bubble_df=pd.DataFrame(new_dp_lst,columns=['Phrase','Count','Level'])      

            filename = r"C:\Project\django\prototype1\trial1\bub_json"

            def to_flare_json1(bubble_df,filename):
                """Convert dataframe into nested JSON as in flare files used for D3.js"""
                flare = dict()
                d = {"name":"phrases", "children": []}
                
                for index, row in bubble_df.iterrows():
                    parent = row[2]
                    child = row[0]
                    child_size = row[1]
                

                    # Make a list of keys
                    key_list = []
                    for item in d['children']:
                        key_list.append(item['name'])

                    #if 'parent' is NOT a key in flare.JSON, append it
                    if not parent in key_list:
                        d['children'].append({"name": parent, "children":[{"size": child_size, "name": child}]})
                    # if parent IS a key in flare.json, add a new child to it
                    else:
                        d['children'][key_list.index(parent)]['children'].append({"size": child_size, "name": child})
                flare = d
                # export the final result to a json file
                with open(filename +'.json', 'w') as outfile:
                    json.dump(flare, outfile, indent=4)
                return ("Done")
            to_flare_json1(bubble_df,filename)

#-----------------------------------------------------Generic Capabilities Analysis-----------------------------------------------------------
            phrases = [x.lower() for x in phrases]
            print(phrases)
            noiseless_words=''.join(i for i in b1.lower() if not i in phrases)

            with open(r"C:\Project\django\prototype1\trial1\media\bank\stopwords.txt",encoding='utf-8') as busy:
                stopwords = busy.read()
               
            stopwords = stopwords.lower().split()
            new_list = []
            stop_list = []

            count = {k:lst.count(k) for k in stopwords }

            for key,value in count.items():
                if value > 1 :
                    stop_list.append([key, value])

            stop_list =pd.DataFrame(stop_list,columns=['Phrase','Count'])

            filename = r"C:\Project\django\prototype1\trial1\stop_json"

            def to_flare_json2(new_df,filename):
                """Convert dataframe into nested JSON as in flare files used for D3.js"""
                flare = dict()
                d = {"name":"phrases", "children": []}
                
                for index, row in new_df.iterrows():
                    parent = row[0]
                    child = row[0]
                    child_size = row[1]
                            

            # Make a list of keys
                    key_list = []
                    for item in d['children']:
                        key_list.append(item['name'])

            #if 'parent' is NOT a key in flare.JSON, append it
                    if not parent in key_list:
                        d['children'].append({"name": parent, "children":[{"size": child_size, "name": child}]})
                # if parent IS a key in flare.json, add a new child to it
                    else:
                        d['children'][key_list.index(parent)]['children'].append({"size": child_size, "name": child})
                flare = d
                            # export the final result to a json file
                with open(filename +'.json', 'w') as outfile:
                    json.dump(flare, outfile, indent=4)
                return ("Done")
                            
            ###############################################################################    
            to_flare_json2(stop_list,filename)  

            

#--------------------------------------------------Passing Context-------------------------------------------------            
            context = {'uploaded_file_url':fileURL,'text': template1.render(),'Imperative': template.render(),'Directive':template2.render(),'Buzzwords' : template3.render(),'compound_requirements': template4.render(),'Continuance' : template5.render(),'Incompleteness': template6.render(),'option':template7.render(), 'gsa':gsa_str,'dp':str_new , 'dca':noiseless_words }
            #return render(request, 'trial1/simple_upload.html', {'text': strng},context)    
            return render(request, 'trial1/simple_upload.html', context)

#----------------------------------------------------------------------------------------------------------------------------------
        else:
            Form_S = fileForm()       
        return render(request, 'trial1/simple_upload.html', {'Form_S' : Form_S})
    else: 
        Form_S = fileForm() 
    return render(request, 'trial1/simple_upload.html', {'Form_S' : Form_S})