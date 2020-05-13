"""
Created on Tue Apr  7 12:26:01 2020

@author: devinpowers
"""


''' Your header goes here '''

import csv
import pylab
from operator import itemgetter

def open_file():
    
    ''' Open File here, try and Except suite '''
    
    while True:  
        file_name = input("Input a file name: ")
        try:
            fp = open(file_name,'r', encoding = 'utf-8')
            break
        except FileNotFoundError:
            print("Unable to open file. Please try again.")
            continue
    return fp


def read_file(fp):
    '''
       Read file, and create Dictionaries, Create new Dictionaries and sort, return 3 new dictionaries
    '''
    # skip header
    fp.readline()
    data_reader = csv.reader(fp)

    D1 = {}
    D2 = {}
    D3 = {}

    for line in data_reader:
    
        name = line[0].lower()
        platform = line[1]
        
        if line[2] == 'N/A':
            year = 0
        else:
            year = int(line[2])
       
        genre = line[3].lower()
        publisher = line[4].lower()
        na_sales = float(line[5]) *1000000
        europe_sales = float(line[6])*1000000
        japan_sales = float(line[7])*1000000
        other_sales = float(line[8])*1000000
    
        global_sales = (na_sales + europe_sales + japan_sales + other_sales)
    
        #Start Making New Dictionaries 
        D1[name] = [name,platform, year, genre, publisher, global_sales]
    
    #You need to make the values of your dictionary an array of tuples. Then you can append new tuples instead of overwriting them. 

        if genre in D2:
            D2[genre].append((genre, year, na_sales, europe_sales, japan_sales, other_sales, global_sales))
        else: 
            D2[genre] = [(genre, year, na_sales, europe_sales, japan_sales, other_sales, global_sales)]
        
        
        if publisher in D3:
            D3[publisher].append((publisher, name, year, na_sales,europe_sales, japan_sales, other_sales, global_sales )) 
        else:
            D3[publisher] = [(publisher, name, year, na_sales,europe_sales, japan_sales, other_sales, global_sales)]
            
        
        # Sort Dictionary 1
        D1_new = {}
    
        for key, value in sorted(D1.items()):
            D1_new[key] = value
    
    
        # Sort DIctionary 2
        D2_new = {}
        
        for key, val in sorted(D2.items()):
            D2_new[key] = sorted(val, key=itemgetter(-1), reverse = True)

        # Sort Dictionary 3
        D3_new = {}
    
        for key,val in sorted(D3.items()):
            D3_new[key] = sorted(val, key=itemgetter(-1), reverse=True)
    
            
    return D1_new, D2_new, D3_new
  
    

def get_data_by_column(D1, indicator, c_value):
    '''
        Have to fix if the c_value isnt given!!
    '''
    new_list_of_tuple = []
    # sort List by Global Sales Largest to smallest
    
    if indicator == 'year':
        
        for value in D1.values():
            if value[2] == c_value:
                
                new_tuple = (value[0],value[1], value[2],value[3],value[4],value[5])
            
                new_list_of_tuple.append(new_tuple)
    
        new_list_of_tuple.sort(key= itemgetter(-1,1), reverse = True )
    
    elif indicator == 'platform':
        
        for value in D1.values():
                if value[1] == c_value:
                    
                    new_tuple = (value[0],value[1], value[2],value[3],value[4],value[5])
            
                    new_list_of_tuple.append(new_tuple)
                   
        new_list_of_tuple.sort(key= itemgetter(-1,2), reverse = True )
                    
    #sort new_list_tuple              
  
    return new_list_of_tuple


def get_publisher_data(D3, publisher):
    '''
       Function goes through D3 and finds Publisher and then creates
       a list of tuples with corresponding publishers!
    
    '''
    list_of_publisher = []
    
    for key,value in D3.items():

        if key == publisher:
        
            for element in value:
                list_of_publisher.append(element)

    #print(list_of_publisher)      
     
    list_of_publisher.sort(key = itemgetter(1))
    list_of_publisher.sort(key = itemgetter(-1), reverse =True)
    
    
    return list_of_publisher



def display_global_sales_data(L, indicator):
    
    '''Display Gloabal Sales for either Year or Platform'''
    

    if indicator == 'year':
        
        print("{:30s}{:10s}{:20s}{:30s}{:12s}".format('Name', 'Year', 'Genre', 'Publisher', 'Global Sales'))
        
        sum_of_global = 0
    
        for element in L:
            print("{:30s}{:10s}{:20s}{:30s}{:<12,.02f}".format(element[0],str(element[2]),element[3],element[4],element[5]))
            
            sum_of_global += element[5]

        print("\n{:90s}{:<15,.02f}".format('Sum of Global Sales:', sum_of_global)) 
    
    elif indicator =='platform':
        
         print("{:30s}{:10s}{:20s}{:30s}{:12s}".format('Name', 'Platform', 'Genre', 'Publisher', 'Global Sales'))
         
         sum_of_global = 0
         
         for element in L:
             
              print("{:30s}{:10s}{:20s}{:30s}{:<12,.02f}".format(element[0],element[1],element[3],element[4],element[5]))
            
              sum_of_global += element[5]
    
         print("\n{:90s}{:<15,.02f}".format('Sum of Global Sales:', sum_of_global)) 



def get_genre_data(D2, year):
    '''
        WRITE DOCSTRING HERE!
    
    '''
    list_of_genres = []


    for value in D2.values():
    
        count = 0
        total_na_sales = 0
        total_eur_sales = 0
        total_jpn_sales = 0
        total_other_sales = 0
        total_global_sales = 0
    
        for element in value:
        
            if element[1] == year:
            
           # print('Value:',value)
  
                count += 1
                total_na_sales += element[2]
                total_eur_sales += element[3]
                total_jpn_sales += element[4]
                total_other_sales += element[5]
                total_global_sales += element[6]
    
        if count != 0:
       
            new_tuple= (element[0],count,total_na_sales,total_eur_sales,total_jpn_sales, total_other_sales, total_global_sales)
    
            list_of_genres.append(new_tuple)
        
    list_of_genres.sort(key= itemgetter(0))
    
    return list_of_genres

 
def display_genre_data(genre_list):
    '''
        Display Genre Data
    '''
    
    print( "{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}".format('Genre', 'North America', 'Europe', 'Japan', 'Other', 'Global'))
    
    sum_of_global = 0
  
    for element in genre_list:
    
        print("{:15s}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}".format(element[0],element[2],element[3],element[4], element[5], element[6]))

        sum_of_global += element[6]
        
    print("\n{:75s}{:<15,.02f}".format('Sum of Global Sales:', sum_of_global))


def display_publisher_data(pub_list):

    '''
       Display Publisher data
    '''
    
    print("{:30s}{:15s}{:15s}{:15s}{:15s}{:15s}".format('Title', 'North America', 'Europe', 'Japan', 'Other', 'Global'))

    sum_of_global = 0
    for element in pub_list:
        print("{:30s}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}".format(element[1],element[3],element[4],element[5],element[6], element[7]))
    
        sum_of_global += element[7]

    print("\n{:90s}{:<15,.02f}".format('Sum of Global Sales:', sum_of_global))
    
    

def get_totals(L, indicator):
    
    '''
        Build Two list (L1, L2) of Corresponding Values with L1 being  each year or each platform, and  
        L2 being the corresponding gloabl sales for that year or platform.
        Built a Dictionary with Key being either year or platform, then the Value equal to the
        global sales.
           
    '''
    
    if indicator == 'year':
        
        D = {}

        for platform in L:
            if platform[1] in D:
                D[platform[1]] += platform[5]    #If platform already in Dictionary, add gloabl sales
            else:
                D[platform[1]] = platform[5]     #Else, platform hasnt been entered in the dictionary yet so we enter it in with global sales as its value
                
        L1 = []  # list of platforms
        L2 = []  # corresponding list of global sales for each platform
        
        for keys in D.keys():
            L1.append(keys)   #add platform to L1
        
        L1.sort()                        # Sort L1
        L2 = [D[v] for v in L1]          # Add corresponding Value (global sales) to L2 from reading L1
    
  
    
    elif indicator == 'platform':
        
        D = {}
        
        for year in L:
            if year[2] in D:           # If year already in Dictionary, we add global sales
                D[year[2]] += year[5]
            else:             
                D[year[2]] = year[5]    # Else, year hasnt been added yet, so we enter it in as a key and set gloabl sales as its value
        
        L1 = []   # list of years
        L2 = []   # corresponding list of global sales for each year

        for keys in D.keys():
            L1.append(keys)          # adds year to L1
        
        L1.sort()
        L2 = [D[v] for v in L1]     # adds corresponding Value (global sales) to L2 from reading L1
        

    
    return L1, L2


def prepare_pie(genres_list):
    '''
        Prepare pie for genre list stuff, return 2 lists:
    '''
     
    list_of_tuples = []

    for element in genres_list:
    
        genre_sales = (element[0], element[6])  # Genre name and Global Sales
    
        list_of_tuples.append(genre_sales)  
    
    
    list_of_tuples.sort(key = itemgetter(1), reverse = True) #sort by Genre Name first, then by Global Sales

    L1 = []  #Genre Name

    L2 = []  #Corresponding Global Sales

    for pair in list_of_tuples:
    
        L1.append(pair[0])
    
        L2.append(pair[1])
    
    return L1, L2




def plot_global_sales(x,y,indicator, value):
    '''
        This function plots the global sales per year or platform.
        
        parameters: 
            x: list of publishers or year sorted in ascending order
            y: list of global sales that corresponds to x
            indicator: "publisher" or "year"
            value: the publisher name (str) or year (int)
        
        Returns: None
    '''
    
    if indicator == 'year':    
        pylab.title("Video Game Global Sales in {}".format(value))
        pylab.xlabel("Platform")
    elif indicator == 'platform':    
        pylab.title("Video Game Global Sales for {}".format(value))
        pylab.xlabel("Year")
    
    pylab.ylabel("Total copies sold (millions)")
    
    pylab.bar(x, y)
    pylab.show()

def plot_genre_pie(genre, values, year):
    '''
        This function plots the global sales per genre in a year.
        
        parameters: 
            genre: list of genres that corresponds to y order
            values: list of global sales sorted in descending order 
            year: the year of the genre data (int)
        
        Returns: None
    '''
            
    pylab.pie(values, labels=genre,autopct='%1.1f%%')
    pylab.title("Video Games Sales per Genre in {}".format(year))
    pylab.show()
    
    
    
    

def main():
    
    #open the file
    fp = open_file()
    
    #Read the file
    
    D1_new, D2_new, D3_new = read_file(fp)
    
    MENU = '''Menu options
    
    1) View data by year
    2) View data by platform
    3) View yearly regional sales by genre
    4) View sales by publisher
    5) Quit
    
    Enter choice: '''
    
    choice = input(MENU)   
    
    
    while choice != '5':
        
        #Option 1: Display all platforms for a single year
        
        if choice == '1':
            indicator = 'year'
            
            try: 
                c_value = input('Please Enter a Year (int): ')
                c_value = int(c_value)
                
                # Call get data by Column Function
                L = get_data_by_column(D1_new, indicator, c_value)
                
                #display the data if the year exists
                
                display_global_sales_data(L, indicator)
                
                # get lists of platform and coressponding global sales
                
                list_of_platforms_and_sales = get_totals(L, indicator)
                
                # ask user if they would like to plot
                plot = input("Would you like to plot the Data? (y or n): ")
                
                if plot == 'y':
                    #plot global sales
                    
                    plot_global_sales(list_of_platforms_and_sales[0], list_of_platforms_and_sales[1],indicator, c_value)
                break
   
            except ValueError:
                
                print('Error')
                
        
        elif choice == '2':
            
            indicator = 'platform'
            
            try:
                c_value = input(str('Please enter a platform: '))
                
                L = get_data_by_column(D1_new, indicator, c_value)
                
                display_global_sales_data(L, indicator)
                
                list_of_years_and_sales = get_totals(L, indicator)
                
                plot = input("Would you like to plot the Data? (y or n): ")
                
                if plot == 'y':
                    #plot global sales
                    
                    plot_global_sales(list_of_years_and_sales[0], list_of_years_and_sales[1],indicator, c_value)
                    
                break
   
            except ValueError:
                
                print('Error')
                
                

        elif choice == '3':
            
            year = input(('Please Enter a Year (int): '))
       
            try:
                
                year = int(year)
                # Call get genre data function
                genre_list = get_genre_data(D2_new, year)
                
                #display Genre List if year exsits
                display_genre_data(genre_list)
                
                #ask user if they would like to plot the data
                
                plot = input("Would you like to plot the Data? (y or n): ")
                
                if plot == 'y':
                    
                    #Call prepare pie function
                    
                    genre, values = prepare_pie(genre_list)
                    
                    # Display Pie Function
                    
                    plot_genre_pie(genre, values, year)
                    
                    break
                
            except ValueError:
                print('Error')
                
            
        #Option 4: Display publisher data
        elif choice == '4':
            
            publisher = input('Please enter a Publisher: ')
            
            try:
                
                #Get list of plublishers
                
                pub_list = get_publisher_data(D3_new, publisher)
                
                # display list of publishers
                display_publisher_data(pub_list)

            
   
                # Enter keyword for the publisher name
                
                # search all publisher with the keyword
                match = []
                
                # print the number of matches found with the keywords
                if len(match) > 1:    
                    print("There are {} publisher(s) with the requested keyword!".format(len(match)))
                    for i,t in enumerate(match):
                        print("{:<4d}{}".format(i,t[0]))
                    
                    # PROMPT USER FOR INDEX
                    
                else:
                    index = 0
                
                choice = input(MENU)
                
            except ValueError:
                print('Error')   

    
    print("\nThanks for using the program!")
    print("I'll leave you with this: \"All your base are belong to us!\"")

if __name__ == "__main__":
    main() 