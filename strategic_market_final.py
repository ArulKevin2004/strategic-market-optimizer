from tabulate import tabulate

def calculate_payoff_matrix(payoff_matrix,no_of_towns_A,no_of_towns_B):

    #Getting inputs
   
    total_number_of_towns=max(no_of_towns_A,no_of_towns_B)
    town_A=[]
    town_B=[]
    town_A=input("Enter the towns where Vendor A can sell : ").split(" ")
    town_B=input("Enter the towns where Vendor B can sell  : ").split(" ")
    town_price=[]
    for i in range(total_number_of_towns):
        print("Enter the inhabitants of town ",i+1," : ",end=" ")
        pr=input()
        town_price.append(pr)
    distance=[]
    for i in range(1,total_number_of_towns):
        for j in range(i+1,total_number_of_towns+1):
            dist=[]
            print("Enter the distance between town ",i,"and ",j," :",end=" ")
            di=input()
            dist.append(i)
            dist.append(j)
            dist.append(di)
            distance.append(dist)
           
    percent_if_present=float(input("Enter the percentage of inhabitants that will buy the pictures if any one vendor is present in their town: "));
    percent_if_absent=float(input("Enter the percenatge of inhabitants that will travel to other towns to buy pictures if no vendor is there in their town : "));

    partiality=input("Do they prefer any vendor if both vendors are in the same town (Yes or No): ");

    if(partiality=="Yes"):
        vendor_preferred=int(input("Enter the vendor who is given preference (1 for Player A and 2 for Player B) : "));

        if(vendor_preferred==1):
            player_A_percent=float(input("Enter the preferred percentage (should be more than 50%) : "));
            player_B_percent=100-player_A_percent;

        else:
            player_B_percent=float(input("Enter the preferred percentage (should be more than 50%) : "));
            player_A_percent=100-player_B_percent;

    else:
        player_A_percent=50;
        player_B_percent=50;

   #To split the distance matrix
       
    Tot_Distance=[]
    for i in range(1,total_number_of_towns+1):
        Distancee=[]
        for j in range(1,total_number_of_towns+1):
            if (i<j):
                for k in range(len(distance)):
                    dist=[]
                    if(distance[k][1]==j and distance[k][0]==i):
                        dist.append(i)
                        dist.append(j)
                        dist.append(distance[k][2])
                        Distancee.append(dist)
            elif (i>j):
                for k in range(len(distance)):
                    dist=[]
                    if(distance[k][0]==j and distance[k][1]==i):
                        dist.append(i)
                        dist.append(j)
                        dist.append(distance[k][2])
                        Distancee.append(dist)
        Tot_Distance.append(Distancee)
               

    #To calculate the Total Number of Customers
   
    Total_cust=[]
    cust=0
    for i in town_A:
        Cust_for_town=[]
        for j in town_B:
            for k in range(1,total_number_of_towns+1):
                if int(i)==k or int(j)==k:
                    cust=cust+(percent_if_present/100)*int(town_price[k-1])
                else:
                    cust=cust+(percent_if_absent/100)*int(town_price[k-1])
            Cust_for_town.append(cust)
            cust=0
        Total_cust.append(Cust_for_town)


    #To print the total_customer table

    tabular_content=[[towna] + list(row) for row,towna in zip(Total_cust,town_A)]
    table=tabulate(tabular_content,town_B,tablefmt="fancy_grid")
    print("\n\nTotal Customer Table \n")
    print("  A \t\tB")
    print(table)


    #To calculate the customers for Vendor A
    Vendor_A=[]
    k=0;
    for i in town_A:
        l=0;
        A_town=[]
        for j in town_B:
            if i==j:
                tot=(player_A_percent/100)*Total_cust[k][l];
            else:
                tot=(int(town_price[int(i)-1])*(percent_if_present))/100;
                for x in (Tot_Distance[int(i)-1]):
                    if int(x[1])!=int(j):
                        new=x[1]
                        proportion_A=int(x[2])
                        for a in (Tot_Distance[int(j)-1]):
                            if int(a[1])==int(new):
                                proportion_B=int(a[2])
                                tot_pro=proportion_A+proportion_B
                                town_pr=(int(town_price[int(a[1])-1])*(percent_if_absent))/100;
                                tot=tot+(town_pr*proportion_B/tot_pro);
            A_town.append(round(tot,3))
            l=l+1;
        Vendor_A.append(A_town)
        k=k+1;

    #To print the Customer for Vendor A table

    tabular_content=[[towna] + list(row) for row,towna in zip(Vendor_A,town_A)]
    table=tabulate(tabular_content,town_B,tablefmt="fancy_grid")
    print("\n\nCustomer for Vendor A Table \n")
    print("  A \t\tB")
    print(table)

    #To calculate the customers for Vendor B
                   
    Vendor_B=[]
    for i in range(len(Total_cust)):
        B_town=[]
        for j in range(len(Total_cust[0])):
            vend_B=float(Total_cust[i][j])-float(Vendor_A[i][j])
            B_town.append(vend_B)
        Vendor_B.append(B_town)

     #To print the Customer for Vendor B table

    tabular_content=[[towna] + list(row) for row,towna in zip(Vendor_B,town_A)]
    table=tabulate(tabular_content,town_B,tablefmt="fancy_grid")
    print("\n\nCustomer for Vendor B Table \n")
    print("  A \t\tB")
    print(table)

    #To calculate the Market Share for Vendor A
   
    Market_share_A=[]
    for i in range(len(Total_cust)):
        A_town=[]
        for j in range(len(Total_cust[0])):
            M_Share_A=float(Vendor_A[i][j])/float(Total_cust[i][j])*100
            A_town.append(round(M_Share_A,1))
        Market_share_A.append(A_town)

    #To print the Market Share for Vendor A table

    tabular_content=[[towna] + list(row) for row,towna in zip(Market_share_A,town_A)]
    table=tabulate(tabular_content,town_B,tablefmt="fancy_grid")
    print("\n\nMarket Share for Vendor A Table \n")
    print("  A \t\tB")
    print(table)

    #To calculate the Market Share for Vendor B
   
    Market_share_B=[]
    for i in range(len(Total_cust)):
        B_town=[]
        for j in range(len(Total_cust[0])):
            M_Share_B=float(Vendor_B[i][j])/float(Total_cust[i][j])*100
            B_town.append(round(M_Share_B,1))
        Market_share_B.append(B_town)

    #To print the Market Share for Vendor B table

    tabular_content=[[towna] + list(row) for row,towna in zip(Market_share_B,town_A)]
    table=tabulate(tabular_content,town_B,tablefmt="fancy_grid")
    print("\n\nMarket Share for Vendor B Table \n")
    print("  A \t\tB")
    print(table)

    #To print the Result

    print("\n\nResult: ")
    print("\n\n")

    #To find the maximum market share of A
   
    count_A=[]    
    for i in range(len(Market_share_A)):
        town_count_A=0;
        for j in Market_share_A[i]:
            town_count_A=town_count_A+j
        count_A.append(town_count_A)
    t=count_A.index(max(count_A))
    print("Vendor A should choose town ",town_A[t]," to increase his/her market share ")

    #To find the maximum market share of B
   
    count_B=[0 for element in range(len(Market_share_A[0]))]
    for i in range(len(Market_share_A)):
        for j in range(len(Market_share_A[i])):
            count_B[j]=count_B[j]+int(Market_share_A[i][j])
    t=count_B.index(min(count_B))
    print("Vendor B should choose town ",town_B[t]," to increase his/her market share ")

     
def main():
   
    no_of_towns_A=int(input("Enter the total number of Towns where Vendor A can sell their picture: "))
    no_of_towns_B=int(input("Enter the total number of Towns where Vendor B can sell their picture: "))
    payoff_matrix=[]
    calculate_payoff_matrix(payoff_matrix,no_of_towns_A,no_of_towns_B)
main()
