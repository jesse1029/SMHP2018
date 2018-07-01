import numpy as np
import pdb


"""
finduni 的目標是把會重複的文字變成編號
比方說，類別、子類別都重複，因此一個類別
就有一個自己的編號。例如，類別Fashion都變成1
類別Beauty都變成2之類的
"""
def finduni(data, key1=None):
    if key1 is None:
        ca, indices = np.unique(data, return_index=True)
    else:
        ca=key1
    len1 = len(ca)
    ischeck=np.zeros((len(data)))
    for i in range(len1):
        key1 = ca[i]
        for j in range(len(data)):
            if data[j]==key1:
                data[j] = str(i)
                ischeck[j]+=1
    for i in range(len(data)):
        if ischeck[i]==0 :
            #pdb.set_trace()
            data[i] = -1

    return ca, data

"""
針對其中一種屬性：有沒有自己取網址名稱
如果有，就設1，反之就0
可能有其他處理方法
"""
def checkAlias(data):
    data2=[]
    for i in range(len(data)):
        if data[i]=="None":
            data2.append(0)
        else:
            data2.append(1)
    return data2


def preprocessing(filename1, key2=None,key3=None,key4=None,key5=None,key6=None,key7=None,key9=None):
    f=open(filename1,'r', encoding='utf-8')
    data=f.readlines()
    f.close()
    len1=len(data)

    d0=[]
    d1=[]
    d2=[]
    d3=[]
    d4=[]
    d5=[]
    d6=[]
    d7=[]
    d8=[]
    d9=[]
    d10=[]
    d11=[]
    d12=[]
    d13=[]
    d14=[]
    """
    把每一個屬性依序讀近來，然後分別處理。比方說，d0是uid，因此直接把非數字部分消除掉，然後轉數字
    d1也是，但d1本來就數字，所以直接轉
    至於d8/d10 一個是標題，一個是tag，都是文字，我簡單處理，就計算文字長度就好，沒特別處理，可以思考看看
    """
    print('Reading data to preprocessing...')
    for i in range(len1):
        uid, pid, category, subcategory, concept, pathalias, ispublic, mediastatus, title, mediatype, alltags, postdate, latitude, geo, ld = data[i].split('" "')

        d0.append(int(uid.replace('"','').replace("@N","")))
        d1.append(int(pid))
        d2.append(category)
        d3.append(subcategory)
        d4.append(concept)
        d5.append(pathalias)
        d6.append(ispublic)
        d7.append(mediastatus)
        d8.append(len(title))
        d9.append(mediatype)
        d10.append(len(alltags)+1)
        d11.append(int(postdate))
        d12.append(float(latitude))
        d13.append(int(geo))
        d14.append(float(ld.replace('"\n', '')))
    
#     ischeck = np.zeros((len1))
#     for i in range(len1):
#         for j in range(len(timezone)):
#             a1, a2 = timezone[j].split(' ')
#             if a1==d15[i]:
#                 ischeck[i]=True
#                 d15[i] = float(a2)
#     for i in range(len1):
#         if ischeck[i]==0:
#             d15[i]=0.0

    print('Find the unique code to replace strings....')
    key2,d2=finduni(d2, key2)
    key3,d3=finduni(d3, key3)
    print('Process attributes 4 and 5...')
    key4,d4=finduni(d4, key4)
    print('Process attributes 6 and 7...')
    key6,d6=finduni(d6, key6)
    key7,d7=finduni(d7, key7)
    print('Process attributes 9...')
    key9,d9=finduni(d9, key9)
    d5 = checkAlias(d5)

    print('Merge data...')
    data=[]
    # ~ pdb.set_trace()
    for i in range(len1):
        data.append([d0[i],d1[i],d2[i],d3[i],d4[i],d5[i],d6[i],d7[i],d8[i],d9[i],d10[i],d11[i],d12[i],d13[i],d14[i]])
    data=np.asarray(data, np.float32)

    return data, key2,key3,key4,key5,key6,key7,key9
