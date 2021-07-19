def open_txtfile():
    with open("file2.txt") as f:
        return f.read().strip().split("\n")

def filter_file(open_file):
    l=[]
    for i in open_file:
        l.append(i.split(":"))
    return l

def create_dict(filtered_file):
    lis=[]
    d={}
    for i in filtered_file:
        if len(i)==2:
            k = i[0]
            lis=[]
        else:
            lis.append(i)
        d[k]=lis
    return d

def filter_dict(my_createdict,city1,city2):
    res = str(city1)+"-"+str(city2)
    lis1=[]
    for i in my_createdict[res]:
        for j in i:
            lis1.append(j.strip())
    my_createdict[res]=lis1
    lis2=[]
    for el in my_createdict[res]:
        lis2.append(el.split("/"))
    my_createdict[res]=lis2
    return my_createdict[res]

def route_map(filtered_dict):
    for j in range(len(filtered_dict)):
        print (filtered_dict[j][0])

def route_results(filtered_dict,route,endroute):
    c=0
    for i in range(len(filtered_dict)):
        if route == filtered_dict[i][0].split("-")[0]:
            while endroute != filtered_dict[i][0].split("-")[0]:
                c += int(filtered_dict[i][1])
                i += 1
    print("The road from "+route+" to "+endroute+" is "+str(c)+" km long")

def my_location(filtered_dict,route,endroute,locations):
    c=0
    e=0
    for i in range(len(filtered_dict)):
        if route == filtered_dict[i][0].split("-")[0]:
            num = i
            while locations != filtered_dict[i][0].split("-")[0]:
                c += int(filtered_dict[i][1])
                i += 1
            else:
                while endroute != filtered_dict[num][0].split("-")[0]:
                    e += int(filtered_dict[num][1])
                    num += 1
                else:
                    left = e - c
    print("you drove "+str(c)+" km")
    print(str(left)+" km left")


def main():
    print("choose your route \n1.input label Gyumri \n2. input label Yerevan or Vanadzor or Stepanavan")
    city1 = raw_input("1.")
    city2 = raw_input("2.")
    open_file = open_txtfile()
    filtered_file = filter_file(open_file)
    my_createdict = create_dict(filtered_file)
    filtered_dict = filter_dict(my_createdict,city1,city2)
    my_routemap = route_map(filtered_dict)
    route = raw_input("select your starting city from the list: ")
    endroute = raw_input("select your finishing city from the list: ")
    my_route = route_results(filtered_dict,route,endroute)
    locations = raw_input("where are you at the moment?: ")
    location = my_location(filtered_dict,route,endroute,locations)

if __name__=="__main__":
    main()
