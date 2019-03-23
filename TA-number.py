import urllib.request, json
import time , sys , random , re , platform




def print_logo():
    clear = "\x1b[0m"
    colors = [34 , 37]
    x = ''''

     _____       ___        __   _   _   _       ___  ___   _____   _____   _____   
    |_   _|     /   |      |  \ | | | | | |     /   |/   | |  _  \ | ____| |  _  \  
      | |      / /| |      |   \| | | | | |    / /|   /| | | |_| | | |__   | |_| |  
      | |     / /-| |      | |\   | | | | |   / / |__/ | | |  _  { |  __|  |  _  /  
      | |    / /  | |      | | \  | | |_| |  / /       | | | |_| | | |___  | | \ \  
      |_|   /_/   |_|      |_|  \_| \_____/ /_/        |_| |_____/ |_____| |_|  \_\ 

                  '''
    for N , line in enumerate ( x.split ( "\n" ) ):
        sys.stdout.write ( "\x1b[1;%dm%s%s\n" % (random.choice ( colors ) , line , clear) )
        time.sleep ( 0.03 )

def self():
    self.r = '\033[31m'
    self.g = '\033[32m'
    self.y = '\033[33m'
    self.b = '\033[34m'
    self.m = '\033[35m'
    self.c = '\033[36m'
    self.w = '\033[37m'


def number():
    self.y = '\033[33m'
    self.b = '\033[34m'
    print ( self.y+"please put number without (0) => Example : 555555555" )
    num = input (self.b+ "Enter Numbers => " )

    with urllib.request.urlopen (
            "http://146.148.112.105/caller/index.php/UserManagement/search_number?number=" + num + "&country_code=SA" ) as url:
        data = json.loads ( url.read ( ).decode ( ) )
        print ( data )
        with open ( 'data.txt' , 'a' ) as name:
            name.write ( str ( data ) + '\n' )



if __name__ == '__main__':
    print_logo()
    number()




