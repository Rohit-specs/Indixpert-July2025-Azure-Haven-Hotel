import datetime
import os
class log:
    def __init__(self,error,module):
        path=os.path.join("log","error.txt")
        self.module=module
        self.path=path
        self.error=str(error)
        if not os.path.exists(path):
            with open(self.path,'w') as f:
                f.write("")
        self.error_logs()

    def save(self):
        with open(self.path,'a') as file:
            file.write(self.log_entry+"\n")
    
    def error_logs(self):
        current_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log_entry="Log Time: "+current_time+"  | Error Type: "+self.error+ "  | Module Name: "+self.module
        self.save()
        
        
        
        
        
        
        