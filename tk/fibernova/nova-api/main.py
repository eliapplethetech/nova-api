import scratchapi
import time

#  Simple request base for scratch.

class Main:

    #  Enclo please update encode and decode to match antee's engine,
    #  I don't know how to, I would if I could. I used my old one
    #  For you to substitute.

    def decode(self, encode_string):
        encode = list(encode_string)
        letters = [" ", "!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0",
                   "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A",
                   "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                   "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "/", "]", "^", "_", "`", "a", "b", "c",
                   "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z", "{", "|", "}", "~", "£"]
        decode_var = ['', '', '', '']
        i = 0
        x = 0
        while i < len(encode):
            ii = encode[i] + encode[i + 1]
            if ii == "00":
                x += 1
                i += 2
                continue
            decode_var[x] += letters[int(ii) - 1]
            i += 2
        return decode_var

    def encode(self, message_string):
        message = list(message_string)
        letters = [[" ", "00"], ["!", "01"], ['"', "02"], ["#", "03"], ["$", "04"], ["%", "05"], ["&", "06"], ["'", "07"],
                   ["(", "08"], [")", "09"],
                   ["*", "10"], ["+", "11"], [",", "12"], ["-", "13"], [".", "14"], ["/", "15"],
                   ["0", "16"], ["1", "17"],
                   ["2", "18"], ["3", "19"], ["4", "20"], ["5", "21"], ["6", "22"], ["7", "23"], ["8", "24"],
                   ["9", "25"], [":", "26"],
                   [";", "27"], ["<", "28"], ["=", "29"], [">", "30"], ["?", "31"], ["@", "32"], ["A", "33"],
                   ["B", "34"], ["C", "35"],
                   ["D", "36"], ["E", "37"], ["F", "38"], ["G", "39"], ["H", "40"], ["I", "41"], ["J", "42"],
                   ["K", "43"], ["L", "44"],
                   ["M", "45"], ["N", "46"], ["O", "47"], ["P", "48"], ["Q", "49"], ["R", "50"], ["S", "51"],
                   ["T", "52"], ["U", "53"],
                   ["V", "54"], ["W", "55"], ["X", "56"], ["Y", "57"], ["Z", "58"], ["[", "59"], ["/", "60"],
                   ["]", "61"], ["^", "62"],
                   ["_", "63"], ["`", "64"], ["a", "65"], ["b", "66"], ["c", "67"], ["d", "68"], ["e", "69"],
                   ["f", "70"], ["g", "71"],
                   ["h", "72"], ["i", "73"], ["j", "74"], ["k", "75"], ["l", "76"], ["m", "77"], ["n", "78"],
                   ["o", "79"], ["p", "80"],
                   ["q", "81"], ["r", "82"], ["s", "83"], ["t", "84"], ["u", "85"], ["v", "86"], ["w", "87"],
                   ["x", "88"], ["y", "89"],
                   ["z", "90"], ["{", "91"], ["|", "92"], ["}", "93"], ["~", "94"], ["£", "95"]]
        encoded = ""
        i = 0
        while i < len(message):
            x = 0
            while x < len(letters):
                if letters[x][0] == message[i]:
                    if len(str(int(letters[x][1]))) > 1:
                        encoded += str(int(letters[x][1]) + 1)
                    else:
                        encoded += "0" + str(int(letters[x][1]) + 1)
                    break
                x += 1
            i += 1
        return encoded + "00"

    def check_data(self):
        if request[1] == "SOME_COMMAND":
            return "This is 'such' a command."
        else:
            return "That's not a command!"

    def _init__(self):
        scratch = scratchapi.ScratchUserSession("<username>", "<password>")
        if scratch.tools.verify_session():
            print("Account Verified")
        cloud = scratchapi.CloudSession(116725373, scratch)

        # server loop
        while True:
            port = cloud.get_var("port")
            if not port == "0":
                cloud.set_var("port", self.encode(self.check_data()))
            else:
                print("pass")
            time.sleep(1)

x = Main()
x._init__()
