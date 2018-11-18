import json
import requests

with open('postal.txt', 'w') as file:
    for firstDigits in range(1, 83):
        strFirst = str(firstDigits)
        if (firstDigits < 10):
            strFirst = '0' + str(firstDigits)
        print(strFirst)

        for lastDigits in range(0, 10000):
            strLast = str(lastDigits)
            if(lastDigits < 10):
                strLast = '000' + str(lastDigits)
            elif(lastDigits < 100):
                strLast = '00' + str(lastDigits)
            elif(lastDigits < 1000):
                strLast = '0' + str(lastDigits)

            postal = strFirst + strLast

            url = (
                "https://developers.onemap.sg/commonapi/search?searchVal="
                + postal + "&returnGeom=N&getAddrDetails=N"
            )

            response = requests.get(url)
            content = response.content.decode("utf8")
            js = json.loads(content)

            if (js["found"] != 0):
                print(postal)
                file.write(postal + '\n')
