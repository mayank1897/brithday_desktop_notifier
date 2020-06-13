from plyer import notification
import pandas as pd
import datetime

def birthday_notifier(name,relation):
    notification.notify(
            title="Birthday Notifier",
            message=f"Today is {name} Birhtday....He is your {relation}",
            app_icon=r"E:\skills\mayankvscode\projects\birthday_desktop_notifier\icon.ico",
            timeout=15
        )
        

if __name__ == "__main__":
    dataframe=pd.read_excel(r"E:\skills\mayankvscode\projects\birthday_desktop_notifier\data.xlsx")
    today_date=datetime.datetime.now().strftime("%d-%m")
    current_year=datetime.datetime.now().strftime("%Y")
    c=[]
    for index,value in dataframe.iterrows():
        birthday_date=value["BIRTHDAY DATE"].strftime("%d-%m")
        birthday_year=str(value["YEAR"])
        if (birthday_date==today_date and current_year not in birthday_year):
            birthday_notifier(value["NAME"],value["RELATION"])
            c.append(index)
    
    if (len(c)!=0):
        for i in c:
            previour_year=dataframe.loc[i,"YEAR"]
            changed_year=str(previour_year)+","+current_year
            dataframe.loc[i,"YEAR"]=changed_year
    else:
        print("No one's birthday today")
    
    dataframe.to_excel(r"E:\skills\mayankvscode\projects\birthday_desktop_notifier\data.xlsx",index=False)
