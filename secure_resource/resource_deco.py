
from auth import authenticate
from datetime import datetime

get_date = datetime.now()
readable_date = get_date.strftime("%d/%m/%Y %H:%M")


def resource_deco(email='example@email.com', password='example123'):
    
    def role_checker(func) :
        check_user = authenticate(email, password)
        
        def wrap_func() :
            if check_user :
                
                if check_user["role"] == "admin" or check_user["role"] == "superadmin" :

                    func()
                    users_result= func()
                    
                    with open("access_granted.txt",'a') as f:
                        f.write(f'\n{check_user["role"]} {check_user["first_name"]} {check_user["last_name"]} viewed company resources on {readable_date}')
                    return users_result


                elif check_user["role"] != "admin" or check_user["role"] != "superadmin" :
                    
                    user_log=("You are not allowed to view this resource")
                    
                    with open("access_denied.txt",'a') as f:
                            f.write(f"\n{check_user['role']} {check_user['first_name']} {check_user['last_name']} tried to view company most valuable resources on {readable_date}")  
                    return user_log  


                
            else:
                return "Only staff can access this resource"

        return wrap_func

    return role_checker





        

        
