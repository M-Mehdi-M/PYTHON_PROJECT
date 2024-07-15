#A System For Management Students Information

#Data structure [Student Name,Student Id Number,Classes,credit,Score]

print("*#*#*#*#*#*#*#*#*{{ Welcome To Student Management System }}*#*#*#*#*#*#*#*#*")

#Main Menu

while True:
    print("\nMain Menu:")
    print("1. Create")
    print("2. Update")
    print("3. Delete")
    print("4. Reports")
    print("5. Archive file")
    print("6. Exit\n")
    a=int(input("Enter your selection (1-6): "))

#Create

    if a==1:
        def searcher(filename,idnumber,name):
            if idnumber in open(filename).read():
                print("Student ID number already exists")
            else:
                z=open("database.txt","a")
                z.write(f"Student name == {name}")
                z.write(",")
                z.write(f"Student id number == {idnumber}\n")
                z.close()
                print("Student registred successfully")
                
                
        b=open("database.txt","a")
        b.close()
        c=str(input("\nPlease enter name of student : "))
        c.capitalize()
        d=str(int(input("\nPlease enter student id number : ")))
            
        e=0
        while e==0:
            if len(d)>6 or 6>len(d):
                print("\nInvalid input, please enter 6 digits student id number")
                d=str(input("\nPlease enter student id number : "))
            else:
                e+=1
        print("\n")
        searcher("database.txt",d,c)
 
#Update menu

    elif a==2:
        while True:
            print("\nUpdate menu:")
            print("1. Enter new score")
            print("2. Modify existing score")
            print("3. Exit update menu\n")
            f=int(input("Enter your selection (1-3): "))
            
#Record Score            
            
            if f==1:
                g=str(input("Please enter student id number: "))
                h=str(input("Please enter class name: "))
                h.capitalize()
                i=str(input("Please enter credit of class: "))
                j=str(input("Please enter given score: "))
                def searcher1(filename,idnumber):
                    infile=open(filename,"r")
                    s=infile.readlines()
                    if idnumber not in open(filename).read():
                        print("\nStudent isn't registred")
                    else:
                        for p in range(0,len(s)):
                            if idnumber in s[p]:
                                su=0
                                w=s[p]
                                x=w.split(",")
                                if h in w:
                                    print("\nThis class was already registred for this id number")
                                    break
                                for y in range(2,len(x)):
                                    ru=x[y].find("Credit==")
                                    su+=int(x[y][ru+8:ru+9])
                                print("\nTotal credits registered for this student: ",su+int(i))
                                if (su+int(i)>18) or (su>18):
                                    print("\nStudent cannot select this class due to credit limit")
                                    print("\nTotal credits for all classes must not exceed 18")
                                    print(f"\nThis student can only select {18-su} more credits")
                                    break
                                if idnumber in open(filename).read():
                                    k=open(filename).read()
                                    res=k.find(g)
                                    res2=res+6
                                    l=k[0:res2]+","+f"{h}==> Credit=={i} Score=={j} "+k[res2:]
                                    m=open(filename,"w")
                                    m.write(l)
                                    m.close()
                                    print("\nInformation reistred successfully")
    
                                         
                searcher1("database.txt",g)

#Change Score                
                
            elif f==2:
                n=str(input("Please enter student id number: "))
                o=str(input("Please input class name to change score: "))
                p=str(input("Please enter new score: "))
                def searcher2(filename,idnumber):
                    infile=open(filename,"r")
                    s=infile.readlines()
                    if idnumber not in open(filename).read():
                        print("\nStudent isn't registred")
                    else:
                        for t in range(0,len(s)):
                            if idnumber in s[t]:
                                w=s[t]
                                x=w.split(",")
                                for y in range(2,len(x)):
                                    su=len(x)-2
                                    if o in x[y]:
                                        a=x[y][len(o)+21:len(o)+23]
                                        c=x[y].replace(a,p)
                                        x[y]=c
                                        s[t]=(",").join(x[0:2])+","+(",").join(x[2:])
                                        mt=""
                                        for i in range(0,len(s)):
                                            mt+=s[i]
                                        u=open(filename,"w")
                                        u.write(mt)
                                        u.close()
                                        print("\nScore changed successfully")
                                        break
                                    else:
                                        su-=1
                                if su==1:
                                    print("\nClass not found")
                                        
                                        

                searcher2("database.txt",n)

#Exit Update Menu
    
            elif f==3:
                break

#Delete menu

    elif a==3:
        while True:
            print("\nDelete Menu:")
            print("1. Remove Student")
            print("2. Remove Class")
            print("3. Exit Delete Menu")
            print("\n")
            b=int(input("Enter your selection (1-3): "))
            
#Delete student            
            
            if b==1:
                d=str(input("Please enter student id number: "))
                def searcher3(filename,idnumber):
                    infile=open(filename,"r")
                    s=infile.readlines()
                    if idnumber not in open(filename).read():
                        print("\nStudent isn't registred")
                    else:
                        for t in range(0,len(s)):
                            if idnumber in s[t]:
                                w=s[t]
                                s.remove(w)
                                mt=""
                                for i in range(0,len(s)):
                                    mt+=s[i]
                                t=open(filename,"w")
                                t.write(mt)
                                t.close()
                                print("\nStudent delited successfully")
                                break
                                

                searcher3("database.txt",d)
        
#Delete class        
        
            elif b==2:
                n=str(input("Please enter student id number: "))
                o=str(input("Please input class name to delete: "))
                def searcher4(filename,idnumber):
                    infile=open(filename,"r")
                    s=infile.readlines()
                    if idnumber not in open(filename).read():
                        print("\nStudent isn't registred")
                    else:
                        for t in range(0,len(s)):
                            if idnumber in s[t]:
                                w=s[t]
                                x=w.split(",")
                                if len(x)==2:
                                    print(f"\n{n} Is whithout any classes")
                                    break
                                else:
                                    su=len(x)-2
                                    for y in range(2,len(x)):
                                        if o in x[y]:
                                            a=x[y]
                                            if "\n" in a:
                                                x.remove(a)
                                                if len(x)>2:
                                                    s[t]=(",").join(x[0:2])+","+(",").join(x[2:])+"\n"
                                                    mt=""
                                                    for i in range(0,len(s)):
                                                        mt+=s[i]
                                                    u=open(filename,"w")
                                                    u.write(mt)
                                                    u.close()
                                                    print("\nClass delited successfully")
                                                    break
                                                else:
                                                    s[t]=(",").join(x[0:2])+(",").join(x[2:])+"\n" 
                                                    mt=""
                                                    for i in range(0,len(s)):
                                                        mt+=s[i]
                                                    u=open(filename,"w")
                                                    u.write(mt)
                                                    u.close()
                                                    print("\nClass delited successfully")
                                                    break
                                            else:
                                                x.remove(a)
                                                if len(x)>2:
                                                    s[t]=(",").join(x[0:2])+","+(",").join(x[2:])
                                                    mt=""
                                                    for i in range(0,len(s)):
                                                        mt+=s[i]
                                                    u=open(filename,"w")
                                                    u.write(mt)
                                                    u.close()
                                                    print("\nClass delited successfully")
                                                    break
                                                else:
                                                    s[t]=(",").join(x[0:2])+(",").join(x[2:])
                                                    mt=""
                                                    for i in range(0,len(s)):
                                                        mt+=s[i]
                                                    u=open(filename,"w")
                                                    u.write(mt)
                                                    u.close()
                                                    print("\nClass delited successfully")
                                                    break
                                        else:
                                            su-=1
                                    if su==1 or su==0:
                                        print("\nClass not found")
                
                
                searcher4("database.txt",n)
               
#Exit Delete Menu                
               
            elif b==3:
                break

#Reports menu

    elif a==4:
        while True:
            print("\nReports Menu:")
            print("1. List of Students in Alphabetical Order")
            print("2. List of Students on Academic Probation")
            print("3. List of Students Sorted by Average Score")
            print("4. Detailed Student Performance Report")
            print("5. Exit Reports Menu")
            b = int(input("\nEnter your selection (1-5): "))
            print("\n")

#List Of Students In Alphabetical Order      
        
            if b==1:
                lst=[]
                infile=open("database.txt","r")
                s=infile.readlines()
                for i in range(0,len(s)):
                    t=s[i]
                    u=(t.find("=="))+3
                    v=(t.find(","))
                    lst.append(t[u:v])
                lst.sort()
                print("\nList of students in alphabetical order=",lst)
                
#List Of Students Who Became Conditional                
                
            elif b==2:
                infile=open("database.txt","r")
                s=infile.readlines()
                lst=[]
                for i in range(0,len(s)):
                    t=s[i]
                    u=(t.find("=="))+3
                    v=(t.find(","))
                    f=t.split(",")
                    sum=0
                    makh=0
                    for i in range(2,len(f)):
                        l=f[i].find("re==")
                        wx=f[i].find("it==")
                        makh+=int(f[i][wx+4:wx+5])
                        sum+=int(f[i][l+4:l+6])*int(f[i][wx+4:wx+5])
                    if makh==0:
                        print(f"{t[u:v]} without any class\n")
                    else:
                        average=round(sum/makh,2)
                        if average<12:
                            lst.append(t[u:v])
                if lst==[]:
                    print("\nNo students have been placed on academic probation")
                else:
                    print("\nStudents on academic probation=",lst)
            
#List Of Students In Order Of Average Score            
               
            elif b==3:
                infile=open("database.txt","r")
                s=infile.readlines()
                lst1=[]
                lst2=[]
                for i in range(0,len(s)):
                    t=s[i]
                    u=(t.find("=="))+3
                    v=(t.find(","))
                    f=t.split(",")
                    sum=0
                    makh=0
                    for i in range(2,len(f)):
                        l=f[i].find("re==")
                        wx=f[i].find("it==")
                        makh+=int(f[i][wx+4:wx+5])
                        sum+=int(f[i][l+4:l+6])*int(f[i][wx+4:wx+5])
                    if makh==0:
                        print(f"\n{t[u:v]} Is without any class")
                    else:
                        average=round(sum/makh,2)
                        lst1.append(average)
                        lst2.append(t[u:v])
                dit=dict(zip(lst2,lst1))
                z=dict(sorted(dit.items(), key=lambda x: x[1],reverse=True))
                y=z.keys()
                u=list(y)
                print("\nList of students in order of average score=",u)
            
#Student Scores And Average Student Score And Place In Class List In Order Of Average Score            
            
            elif b==4:
                infile=open("database.txt","r")
                c=str(input("Please enter student id number: "))
                s=infile.readlines()
                for j in range(0,len(s)):
                    u=s[j]
                    if c in u:
                        sum=0
                        k=u
                        w=u.split(",")
                        x=(k.find("=="))+3
                        v=(k.find(","))
                        makh=0
                        for i in range(2,len(w)):
                            m=w[i].find("re==")
                            wx=w[i].find("it==")
                            makh+=int(w[i][wx+4:wx+5])
                            sum+=int(w[i][m+4:m+6])*int(w[i][wx+4:wx+5])
                        if makh==0:
                            print(f"\n{k[x:v]} Without any class")
                        else:
                            average=round(sum/makh,2)
                            print("\nStudent Name,Student Id Number,Classes,Credit Of Classes,Scores ="f"[{u}]")
                            print("\naverage scores is :",average)
                        h=k[x:v]
                infile=open("database.txt","r")
                s=infile.readlines()
                lst1=[]
                lst2=[]
                for i in range(0,len(s)):
                    t=s[i]
                    u=(t.find("=="))+3
                    v=(t.find(","))
                    f=t.split(",")
                    sum=0
                    for i in range(2,len(f)):
                        l=f[i].find("re==")
                        sum+=int(f[i][l+4:l+6])
                    makh=len(f)-2
                    if makh==0:
                        print(f"\n{t[u:v]} Is without any class")
                    else:
                        average=round(sum/makh,2)
                        lst1.append(average)
                        lst2.append(t[u:v])
                dit=dict(zip(lst2,lst1))
                z=dict(sorted(dit.items(), key=lambda x: x[1],reverse=True))
                y=z.keys()
                u=list(y)
                for J in range(0,len(u)):
                    if u[J]==h:
                        print("\nPlace in order of average score :",J+1)
                      
#Exit Report Menu            
                
            elif b==5:
                break

#Archive File Menu
          
    elif a==5:
        while True:
            print("\nArchive File Management:")
            print("1. View Archive File Contents")
            print("2. Delete Archive File")
            print("3. Exit Archive Menu")
            s=int(input("Enter your selection (1-3): "))
            print("\n")
            
#Print Archive File            
            
            if s==1:
                infile=open("database.txt","r")
                res=infile.read()
                print("Archive file is :","\n",res)
                print("\n")
                
#Delet Archive File
                
            elif s==2:
                infile=open("database.txt","w")
                infile.write("")
                infile.close()
                print("Archive file deleted successfully\n")
                
#Exit Archive Menu               
                
            elif s==3:
                break
            
#Exit                

    elif a==6:
        print("\n*{{ Thank you for using my student information management system }}*")
        break
