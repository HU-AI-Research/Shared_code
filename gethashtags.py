import pandas as pd 

df = pd.read_csv("tweets_labeled.csv")
df.head()

#1 find high frequency words in the tweets text
#1.1. convert text column to list 
text_list = df["text"].tolist()


#1.2. make a function, iterate the list,convert to sorted dictionary in words/frequency pairs:
def convert_dic(alist):
    dic_words={}

    for text in alist:
        words = text.split()
        for word in words:
            if word not in dic_words:
                dic_words[word] = 1
            else:
                dic_words[word] += 1           
    #print(dic_words)
    
    dic_sorted={}
    for word in sorted(dic_words,key=dic_words.get, reverse=True):   
        #print(word, dic_words[word]) 
        dic_sorted[word] = dic_words[word]
        
    return(dic_sorted) 

dic_sorted_words = convert_dic(text_list)    
#print(dic_sorted_words.items())


#2 find the related hashtags in the high frequence words:
#2.1 make a function select words by the start character.
def sec_key(s_dic,dic_sorted_words,s_char):
    s_dic = {}
    for k, v in dic_sorted_words.items():
        if k.startswith(s_char):
            s_dic[k] = v
    return s_dic        


#2.2. find related high frequency used hashtags,get the value
hf_hashtage = sec_key("hf_hashtage",dic_sorted_words,"#")
df_hf_hashtag = pd.DataFrame(hf_hashtage.items(), columns=['hf_hashtag', 'num'])
#print(df_hf_hashtag.head())


#2.3 write the high frequency hashtags to text:
df_hf_hashtag.to_csv('hf_hashtag.txt', header=None, index=False, sep=" ")  