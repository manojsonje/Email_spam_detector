import sys

def dictnary(spam_lines,ham_lines):
    res = []
    for i in spam_lines:
        if(i not in res):
            res.append(i)
    for i in ham_lines:
        if(i not in res):
            res.append(i)
    return len(res)

            
def prob(X,N,k,x_types):
    res  = 0
    res = float(len(X)+k)/(N+k*(x_types)) 
    return res

def p(X,N,k,x_types):
    res  = 0
    res = float(len(X)+k)/(N+k*(x_types)) 
    return res

def check_cal(check_lines,spam_ham,a_spam_ham,k,x_types,flag):
    for i in check_lines:
        myi=i.split(" ")
        N_spam = 9
        N_ham = 15
        res = 1
        if(flag == "s"):
            for i in range(len(myi)):
                #print(myi[i])
               
               res *= float(p(myi[i],N_spam,k,x_types))
            res *= p_spam
                   
        else:
            for i in range(len(myi)):
                #print(myi[i])
                
                res *= float(p(myi[i],N_ham,k,x_types))
            res *= p_ham
    return res
  

def check_email_spam(check_lines,spam_ham,a_spam_ham,k,x_types,flag):
    if(flag =="s"):
        A = check_cal(check_lines,spam_ham,a_spam_ham,k,x_types,flag)
        B = check_cal(check_lines,a_spam_ham,spam_ham,k,x_types,flag)
    else:
        A = check_cal(check_lines,a_spam_ham,spam_ham,k,x_types,flag)
        B = check_cal(check_lines,spam_ham,a_spam_ham,k,x_types,flag)
    
    res = float(A)/(A+B)
    return res

with open('spam_dataset.txt','r') as i_s:
    spam_lines = i_s.readlines()
with open('email_dataset.txt','r') as i_e:
    email_lines = i_e.readlines()
with open('check_email.txt','r') as i_c:
    check_lines = i_c.readlines()
    
k = int(input("enter value of k = "))


spam_lines.remove('\n')
len_spam = len(spam_lines)
len_email = len(email_lines)

N = len_spam + len_email
X_types = 2

p_spam = float(prob(spam_lines,N,k,X_types))
print("probablity of spam i.e-P(spam)" ,p_spam,sep="=")
p_ham = float(prob(email_lines,N,k,X_types))
print("probability of HAM i.e-P(ham)" ,p_ham,sep="=")

x_types = dictnary(spam_lines,email_lines)

ch1 = ch2 = 0
flag1 = "s"
flag2 = "h"
ch1=check_email_spam(check_lines,p_spam,p_ham,k,x_types,flag1)
ch2=check_email_spam(check_lines,p_ham,p_spam,k,x_types,flag2)
if(ch1>ch2):
    print("WARNING!!!! given email is spam detected ")
else:
    print(" given email is not spam")

       

        
