from skipList import SkipList 
from webCrawler import WebCrawlerNSE

def prepare_stock_data(website_url,start_date,end_date):
    scrapper = WebCrawlerNSE(website_url)
    stock_data = scrapper.fetch_data(start_date,end_date)
    print(stock_data)
    scrapper.clear_driver_data()
    return stock_data

def prepare_skip_for_stock_data(list_data,max_level,p_value):
    skip_list = SkipList(max_level,p_value)
    for i in range(0,len(list_data)):
        skip_list.insertElement(list_data[i])
    skip_list.indexing()
    skip_list.display()
    return skip_list

def intersecting_element(list1,list2):
    common_data_list=[]
    head_ptr  = list1.head
    node_ptr = head_ptr.forward[0]
    while node_ptr!=None:
        if(list2.find(node_ptr.key)):
            # print(list2.find(node_ptr.key))
            common_data_list.append(node_ptr.key)
        node_ptr = node_ptr.forward[0]
    return common_data_list

if __name__ == "__main__":
    print("Please enter your website url:\n eg: https://www.nseindia.com/get-quotes/equity?symbol=TATASTEEL")
    print("This crawler is only for nse website:")
    website_url = input()
    print("Pls provide the start date and end date")
    start_date = input("Start Date in (dd-mm-yyy) formate: ")
    end_date = input("End Date in (dd-mm-yyy) formate: ")
    # parser.add_argument("-url","--website_url", help="website url",required=True)
    # parser.add_argument("-days","--no_of_days", help="number of days for stock",required=True)
    # args = parser.parse_args()
    
    stock_list = prepare_stock_data(website_url,start_date,end_date)
    sklist1 = prepare_skip_for_stock_data(stock_list,4,.2)


    print("Please enter your website url:\n eg: https://www.nseindia.com/get-quotes/equity?symbol=JINDALSTEL")
    print("This crawler is only for nse website:")
    website_url = input()
    print("Pls provide the start date and end date")
    start_date = input("Start Date in (dd-mm-yyy) formate: ")
    end_date = input("End Date in (dd-mm-yyy) formate: ")
    # parser.add_argument("-url","--website_url", help="website url",required=True)
    # parser.add_argument("-days","--no_of_days", help="number of days for stock",required=True)
    # args = parser.parse_args()
    
    stock_list2 = prepare_stock_data(website_url,start_date,end_date)
    sklist2 = prepare_skip_for_stock_data(stock_list2,4,.2)


    common_elements = intersecting_element(sklist1,sklist2)
    print("Intersection Element: ",common_elements)

    ##deletion of kth smallest element in the skip list:
    k = int(input("Enter the k value:"))
    sklist2.removeElementByIndex(k)
    sklist2.display()
    
