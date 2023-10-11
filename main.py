#https://www.odoo.com/vi_VN/forum/tro-giup-1/how-can-i-get-odoo-environment-in-thread-145704
######### kHAI BÁO THƯ VIÊN SỬ DỤNG  ################

from skpy import SkypeEventLoop, SkypeCallEvent #pip install SkPy
from datetime import datetime, timedelta
import socket
import time
######### kHAI BÁO THƯ VIÊN SỬ DỤNG  ################

######### kHAI BÁO fILE LIÊN KẾT  ################
from python_config_infomation import read_file_config
######### kHAI BÁO fILE LIÊN KẾT  ################

######### kHAI BÁO BIẾN  ################
HOST = '127.0.0.1'    # Cấu hình address server
PORT = 0            # Cấu hình Port sử dụng
USER_NAME = ''
PASS_WORD = ''
type_started = ''
type_ended = ''
type_missed = ''

_date = datetime.now() + timedelta(days=0, hours=0)
data_log_error = 'LOG/data_log_error_'+_date.strftime('%Y_%m_%d')+ '.txt'
data_log = 'LOG/data_log_'+_date.strftime('%Y_%m_%d')+ '.txt'
######### kHAI BÁO BIẾN  ################

######### Class SkypePing  ################
class SkypePing(SkypeEventLoop):
   
    def __init__(self):
        super(SkypePing, self).__init__(USER_NAME, PASS_WORD)
    def onEvent(self, event):
        if isinstance(event, SkypeCallEvent):
            message = ('New message from user {} at {}: \'{} \''.format(event.msg.type,
                                                                    event.msg.time.strftime('%H:%M dd. %d.%m.%Y'),
                                                                    event.msg.content))
            print(message)
            if('type="started"' in event.msg.content):
                print('Bạn nhận được tín hiệu bắt đầu cuộc gọi')
                # chuổi dữ liệu gửi qua socket khi nhận được tín hiệu
                str_send = type_started
                if len(str_send) > 0:
                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cấu hình socket
                        s.connect((HOST, PORT)) # tiến hành kết nối đến server
                        s.sendall(str_send.encode('utf-8')) # Gửi dữ liệu lên server 
                        #data = s.recv(1024) # Đọc dữ liệu server trả về (chua can)
                        s.close()
                        #ghi nhận dữ liệu nhận được vào file log
                        strlog = "Socket:" + str_send +":"
                        sbLogWrite("OK",strlog)
                    except:
                        #ghi nhận dữ liệu nhận được vào file log
                        strlog = "Socket Error:" + str_send
                        sbLogWrite("ERROR",strlog)
                else:
                    strlog = "Socket:" + str_send +"len=0"
                    sbLogWrite("ERROR",strlog)
                
            elif('type="ended"' in event.msg.content):
                print('Bạn nhận được tín hiệu kết thúc cuộc gọi ')
                # chuổi dữ liệu gửi qua socket khi nhận được tín hiệu
                str_send = type_ended
                if len(str_send) > 0:
                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cấu hình socket
                        s.connect((HOST, PORT)) # tiến hành kết nối đến server
                        s.sendall(str_send.encode('utf-8')) # Gửi dữ liệu lên server 
                        #data = s.recv(1024) # Đọc dữ liệu server trả về (chua can)
                        s.close()
                        #ghi nhận dữ liệu nhận được vào file log
                        strlog = "Socket:" + str_send +":"
                        sbLogWrite("OK",strlog)
                    except:
                        strlog = "Socket Error:" + str_send
                        sbLogWrite("ERROR",strlog)
                else:
                    strlog = "Socket:" + str_send +"len=0"
                    sbLogWrite("ERROR",strlog)
            elif('type="missed"' in event.msg.content):
                print('Cuộc gọi bị nhỡ không bắt máy')
                # chuổi dữ liệu gửi qua socket khi nhận được tín hiệu
                str_send = type_missed
                if len(str_send) > 0:
                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cấu hình socket
                        s.connect((HOST, PORT)) # tiến hành kết nối đến server
                        s.sendall(str_send.encode('utf-8')) # Gửi dữ liệu lên server 
                        #data = s.recv(1024) # Đọc dữ liệu server trả về (chua can)
                        s.close()
                        #ghi nhận dữ liệu nhận được vào file log
                        strlog = "Socket:" + str_send +":"
                        sbLogWrite("OK",strlog)
                    except:
                        strlog = "Socket Error:" + str_send
                        sbLogWrite("ERROR",strlog)
                else:
                    strlog = "Socket:" + str_send +"len=0"
                    sbLogWrite("ERROR",strlog)
######### Class SkypePing  ################

# Hàm xử lý log file vào thư mục LOG
def sbLogWrite(tpye,strlog):
    global data_log_error #tên của file log
    global data_log #tên của file log
    #lấy ngày tháng hiện tại khi log file
    _date = datetime.now() + timedelta(days=0, hours=0)
    string_date = _date.strftime('%Y-%m-%d %H:%M:%S')
    try:
        # thêm thời gian vào chuỗi string
        str = string_date + " --> " + strlog
        if tpye == "ERROR":
            f = open(data_log_error,'a')
            f.write(str + "\n")
            f.close()
        else:
            f = open(data_log,'a')
            f.write(str + "\n")
            f.close()
        print('sbLogWrite:'+str) 
    except:
        pass
  
######### ĐỌC DỮ LIỆU  KHAI BÁO TRONG FILE CONFIG.INI ################
def read_config():
    global HOST 
    global PORT
    global USER_NAME
    global PASS_WORD

    global type_started
    global type_ended
    global type_missed
    try:
        string_config = read_file_config("config.ini","main")
        USER_NAME = string_config["username_skype"]
        PASS_WORD = string_config["password_skype"]
        HOST = string_config["socket_ip"]
        PORT = int(string_config["socket_port"])
        #ghi nhân main
        strlog = "Read file config main : " + str(string_config)
        sbLogWrite("OK",strlog)
        print(strlog)

        string_config = read_file_config("config.ini","socket_send")
        type_started = string_config["type_started"]
        type_ended = string_config["type_ended"]
        type_missed = string_config["type_missed"]
        #ghi nhân main
        strlog = "Read file config socket_send : " + str(string_config)
        sbLogWrite("OK",strlog)
        print(strlog)




    except:
        strlog = "Read file config error "
        sbLogWrite("ERROR",strlog)
        print(strlog)
########################################################################################

######################################################################
############################# HÀM XỬ LÝ MAIN #########################      
if __name__ == '__main__':
    while(True):
        try:
            strlog = "Begin_Program"
            sbLogWrite("OK",strlog)
            #đọc file con file
            read_config()
            # vào vòng lặp của class
            event = SkypePing()
            event.loop()
        except:
            time.sleep(1000)
            strlog = "Error_Program"
            sbLogWrite("ERROR",strlog)
            pass
############################# HÀM XỬ LÝ MAIN #########################
######################################################################   