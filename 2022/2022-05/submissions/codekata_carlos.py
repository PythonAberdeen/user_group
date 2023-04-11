def myfunction2(text,n):
    if type(text)==str and type(n)==int and n>=2:
        if len(text)<n:
            print('try a larger text')
        else:
            list_final = []
            flag=0
            for i in range(0, len(text), n):
                if flag==1:
                    i=i-1
                    flag=0
                candidate = text[i:i+n]
                if candidate[-1]!=' ':
                    candidate=candidate[:-1]+'-'
                    flag=1
                list_final.append(candidate)
        return list_final
    else:
        print('try again')

test = myfunction2('Hello my name is elder price',6)