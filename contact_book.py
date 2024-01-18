# CONTACT BOOK
from  beautifultable import BeautifulTable
class Contact_Book:
    def _init_(self):
        self.__data={}
    def addcontacts(self,name=None,address=None,phone_number=None,email=None):
        if(name!=None and address!=None and phone_number!=None and email!=None):
            if phone_number not in self.__data:
                self.__data[phone_number]=[name,address,phone_number,email]
                print("Added Successfully")
            else:
                print("Number already exists")
        else:
            print("Please enter all the values:-")

    def deletecontacts(self,phone_number=None):
        if phone_number!=None:
            if phone_number in self.__data:
                del self.__data[phone_number]
                print("Deleted successfully")
            else:
                print("Please enter phone number:-")
    def updateContact(self,name=None,address=None,phone_number=None,email=None):
        if phone_number!= None and phone_number in self.__data:
            lst_info= self.__data[phone_number]
            if name !=None:
                lst_info[0]=name
            if address!=None:
                lst_info[1]=address
            if email!=None:
                lst_info[3]=email
            self.__data[phone_number]=lst_info
            print("Data Updated successfully")
        else:
            print("Phone Number does not exists in the databases")
    def searchContact(self,query=None,sort_field=None):
        if query!=None:    
            search_arr=[]
            for key,val in self.__data.items():
                search_arr.append(val + [" ".join(val)])
            print(search_arr)
            result=set()
            for word in query.lower().split():
                for i in range (len(search_arr)):
                    if word in search_arr[i][-1].lower():
                        result.add(i)
            ans=[]
            for i in result:
                ans.append(search_arr[i])
            indx=0
            if sort_field=="name":
                indx=0
            if sort_field=="address":
                indx=1
            if sort_field=="phone_number":
                indx=2
            if sort_field=="email":
                indx=3
            ans.sort(key=lambda x :x[indx])
            return ans
        else:
            return []    
    def viewContact(self,data):
        table=BeautifulTable()
        for child_data in data:
            table.rows.append(child_data[:-1])

        table.rows.header=[str(i) for i in range(1,len(data)+1)]
        table.columns.header=["name","address","phone_number","email"]
        print(table)
contact_book=Contact_Book()
contact_book.addcontacts("CHHAVI","NMH","9827638327","chhavijain221864@gmail.com")
contact_book.addcontacts("AMAN JAIN","noida","913549017","amujain143@gmail.com")
#contact_book.deletecontacts("9827638327")
#contact_book.updateContact(name="Aman",phone_number="9827638327")
print(contact_book.searchContact(" 9131 JAIN"))