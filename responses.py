import random
import string
from random import *
from random import random
characters = string.ascii_letters + "1234567890"
def get_response(message: str,username, channel) -> str:
    premium_text_file = open("premium_list.txt", "r",encoding="utf8")
    premium_list = premium_text_file.read()
    owner = "siber_guvenlik"

    premium_text_file.close()
    p_message = message.lower()






    
    if p_message == 'siber help':
        return '`Bu bir generator botudur.Yani stok vardır ve stoğun içinden rastgele eşya vs. alırsınız.\nKomutlar : \nsiber stock -> stokları görürsünüz!\nStoklardan birşey almak için "siber gen [stock  isim].Seçtiğiniz stoktan rastgele eşya alır ve size dm\'den yollar.DM\'nizin açık olması lazım.`'


    if p_message == "ws all":
        return "İnşallah OwO çıkar."
    if p_message == "wcf all":
        return "İnşallah yazı çıkar."
    if p_message == "wcf t all":
        return "İnşallah tura çıkar."
    if p_message == "wbj all":
        return "İnşallah 21 çekersin."







    if p_message == "siber stock":
        return '`Bedava Stoklar : \nnitro[kontrol edilmemiş]\npassword[rastgele]\nnetflix[rastgele]\nminecraft[rastgele]\nrobux[rastgele]\nPremium Özel Stoklar : \nSteam[%20 Şansla Çalışır, Bol Oyunlu Çıkar]\nBlutv[Yüksek Çalışma Şansı]\nDisney[%50 Çalışma Şansı]\nStoklarda birine bakmak için : "siber gen [stok adı]"`'



    if "siber gen" in p_message:
        if channel != "gen":
            return "`Beni Burada Kullanamazsın.`"




    if p_message == "siber gen steam":
        if username in premium_list:

            f = open("steam.txt", "r")
            steam_list = f.read()
            steam_list = steam_list.split("\n")
            steam_account = steam_list[randint(1,530)]
            f.close()
            steam_account = steam_account.replace("- Games:", "- Oyunlar:")
            steam_account = steam_account.replace("- Balance:", "- Ne Kadar Para Var:")
            return f"`İşte Rastgele Premium Özel Steam Hesabın : \n{steam_account}`"
        else:
            return "`Bu Premium Özel Bir Stoktur.Lütfen Premium Satın Alın`"

        
    if p_message == "siber gen robux":
        if username in premium_list:
            characterss = string.ascii_uppercase + "1234567890"
            robux_code1 =  "".join(choice(characterss) for x in range(12))
            robux_code2 =  "".join(choice(characterss) for x in range(12))
            robux_code3 =  "".join(choice(characterss) for x in range(12))
            robux_code4 =  "".join(choice(characterss) for x in range(12))
            robux_code5 =  "".join(choice(characterss) for x in range(12))
            robux_code6 =  "".join(choice(characterss) for x in range(12))
            robux_code7 =  "".join(choice(characterss) for x in range(12))
            robux_code8 =  "".join(choice(characterss) for x in range(12))
            robux_code9 =  "".join(choice(characterss) for x in range(12))
            robux_code10 =  "".join(choice(characterss) for x in range(12))
            return f"`İşte Rastgele Oluşturulmuş Robux Kodların : \n{robux_code1}\n{robux_code2}\n{robux_code3}\n{robux_code4}\n{robux_code5}\n{robux_code6}\n{robux_code7}\n{robux_code8}\n{robux_code9}\n{robux_code10}`"


        characterss = string.ascii_uppercase + "1234567890"
        robux_code =  "".join(choice(characterss) for x in range(12))
        return f"`İşte Rastgele Oluşturulmuş Robux Kodun : {robux_code}`"

    if p_message == "siber gen nitro":
        if username in premium_list:
            lowercase = "abcdefghijklmnopqrstuvwxyz"
            uppercase = "ABCDEFGHIJKLMNOPQRSTUVWYYZ"
            numbers = "0123456789"

            upper, lower, nums = True, True, True
            all = ""

            if upper:
              all += uppercase
            if lower:
                all += lowercase
            if nums:
                all += numbers

            length = 16
            code1 = "".join(choice(characters) for x in range(length))
            code2 = "".join(choice(characters) for x in range(length))
            code3 = "".join(choice(characters) for x in range(length))
            code4 = "".join(choice(characters) for x in range(length))
            code5 = "".join(choice(characters) for x in range(length))
            code6 = "".join(choice(characters) for x in range(length))
            code7 = "".join(choice(characters) for x in range(length))
            code8 = "".join(choice(characters) for x in range(length))
            code9 = "".join(choice(characters) for x in range(length))
            code10 = "".join(choice(characters) for x in range(length))
            return(f"`İşte nitro kodların : \n{code1}\n{code2}\n{code3}\n{code4}\n{code5}\n{code6}\n{code7}\n{code8}\n{code9}\n{code10}\n[kontrol edilmemiş]\nİşte link halleri :` \nhttps://discord.com/gifts/{code1}\nhttps://discord.com/gifts/{code2}\nhttps://discord.com/gifts/{code3}\nhttps://discord.com/gifts/{code4}\nhttps://discord.com/gifts/{code5}\nhttps://discord.com/gifts/{code6}\nhttps://discord.com/gifts/{code7}\nhttps://discord.com/gifts/{code8}\nhttps://discord.com/gifts/{code9}\nhttps://discord.com/gifts/{code10}\n`[kontrol edilmemiş]`")
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWYYZ"
        numbers = "0123456789"

        upper, lower, nums = True, True, True
        all = ""

        if upper:
            all += uppercase
        if lower:
            all += lowercase
        if nums:
            all += numbers

            length = 16
        code = "".join(choice(characters) for x in range(length))
        return(f"`İşte nitro kodun : {code}  [kontrol edilmemiş]`  \nhttps://discord.com/gifts/{code}    `[Link Hali]`")
    


    if p_message == "siber gen minecraft":
        if username in premium_list:
            f = open("minecraft.txt", "r")
            minecraft = f.read()
            minecraft = minecraft.split("\n")
            minecraft1 = minecraft[randint(1,28)]
            minecraft2 = minecraft[randint(1,28)]
            minecraft3 = minecraft[randint(1,28)]
            minecraft4 = minecraft[randint(1,28)]
            minecraft5 = minecraft[randint(1,28)]
            minecraft6 = minecraft[randint(1,28)]
            minecraft7 = minecraft[randint(1,28)]
            minecraft8 = minecraft[randint(1,28)]
            minecraft9 = minecraft[randint(1,28)]
            minecraft10 = minecraft[randint(1,28)]
            return(f"`İşte rastgele minecraft hesapların : \n{minecraft1}\n{minecraft2}\n{minecraft3}\n{minecraft4}\n{minecraft5}\n{minecraft6}\n{minecraft7}\n{minecraft8}\n{minecraft9}\n{minecraft10}\n[kontrol edilmemiş]`")


        f = open("minecraft.txt", "r")
        minecraft = f.read()
        minecraft = minecraft.split("\n")
        minecraft = minecraft[randint(1,28)]
        return(f"`İşte rastgele minecraft hesabın : {minecraft} [kontrol edilmemiş]`")



    if p_message == "siber gen password":
        password =  "".join(choice(characters) for x in range(randint(8, 16)))
        return(f"` İşte oluşturulmuş şifren : {password}  [rastgele] `")
    

    if p_message == "siber gen disney":

        if username in premium_list:
            f = open("disney plus.txt", "r")
            disney_plus = f.read()
            disney_plus = disney_plus.split("\n")
            the_disney = disney_plus[randint(1,145)]
            the_disney = the_disney.removesuffix(" | 2FA")
            f.close()
            return(f"`İşte disney plus hesabın : {the_disney}`")
        else:
            return "`Premium'a Sahip Değilsin!`"



    if p_message == "siber gen blutv":
        if username in premium_list:
            f = open("blutv.txt", "r")
            blutv = f.read()
            blutv = blutv.split("\n")
            account = blutv[randint(1,45)]
            return f"`İşte BluTV Hesabın : {account}`"
        else:
            return "`Bu premium özel bir stoktur.Erişmek için premium gereklidir.`"








    if p_message == "siber gen netflix":
        if username in premium_list:
            f = open("netflix.txt", "r")
            netflix = f.read()
            netflix = netflix.split("\n")
            the_netflix1 = netflix[randint(1,80)]
            the_netflix1 = the_netflix1.replace("	Today","")
            the_netflix1 = the_netflix1.replace("	1 day ago","")
            the_netflix1 = the_netflix1.replace("	2 day ago","")
            the_netflix1 = the_netflix1.replace("	",":")
            the_netflix2 = netflix[randint(1,80)]
            the_netflix2 = the_netflix2.replace("	Today","")
            the_netflix2 = the_netflix2.replace("	1 day ago","")
            the_netflix2 = the_netflix2.replace("	2 day ago","")
            the_netflix2 = the_netflix2.replace("	",":")
            the_netflix3 = netflix[randint(1,80)]
            the_netflix3 = the_netflix3.replace("	Today","")
            the_netflix3 = the_netflix3.replace("	1 day ago","")
            the_netflix3 = the_netflix3.replace("	2 day ago","")
            the_netflix3 = the_netflix1.replace("	",":")
            the_netflix4 = netflix[randint(1,80)]
            the_netflix4 = the_netflix4.replace("	Today","")
            the_netflix4 = the_netflix4.replace("	1 day ago","")
            the_netflix4 = the_netflix4.replace("	2 day ago","")
            the_netflix4 = the_netflix4.replace("	",":")
            the_netflix5 = netflix[randint(1,80)]
            the_netflix5 = the_netflix5.replace("	Today","")
            the_netflix5 = the_netflix5.replace("	1 day ago","")
            the_netflix5 = the_netflix5.replace("	2 day ago","")
            the_netflix5 = the_netflix5.replace("	",":")
            the_netflix6 = netflix[randint(1,80)]
            the_netflix6 = the_netflix6.replace("	Today","")
            the_netflix6 = the_netflix6.replace("	1 day ago","")
            the_netflix6 = the_netflix6.replace("	2 day ago","")
            the_netflix6 = the_netflix6.replace("	",":")
            the_netflix7 = netflix[randint(1,80)]
            the_netflix7 = the_netflix7.replace("	Today","")
            the_netflix7 = the_netflix7.replace("	1 day ago","")
            the_netflix7 = the_netflix7.replace("	2 day ago","")
            the_netflix7 = the_netflix7.replace("	",":")
            the_netflix8 = netflix[randint(1,80)]
            the_netflix8 = the_netflix8.replace("	Today","")
            the_netflix8 = the_netflix8.replace("	1 day ago","")
            the_netflix8 = the_netflix8.replace("	2 day ago","")
            the_netflix8 = the_netflix8.replace("	",":")
            the_netflix9 = netflix[randint(1,80)]
            the_netflix9 = the_netflix9.replace("	Today","")
            the_netflix9 = the_netflix9.replace("	1 day ago","")
            the_netflix9 = the_netflix9.replace("	2 day ago","")
            the_netflix9 = the_netflix9.replace("	",":")
            the_netflix10 = netflix[randint(1,80)]
            the_netflix10 = the_netflix10.replace("	Today","")
            the_netflix10 = the_netflix10.replace("	1 day ago","")
            the_netflix10 = the_netflix10.replace("	2 day ago","")
            the_netflix10 = the_netflix10.replace("	",":")
            return(f"`İşte netflix hesapların : \n{the_netflix1}\n{the_netflix2}\n{the_netflix3}\n{the_netflix4}\n{the_netflix5}\n{the_netflix6}\n{the_netflix7}\n{the_netflix8}\n{the_netflix9}\n{the_netflix10}\n\n [rastgele]`")


        f = open("netflix.txt", "r")
        netflix = f.read()
        netflix = netflix.split("\n")

        the_netflix = netflix[randint(1,80)]
        account = the_netflix.replace("	Today","")
        account = account.replace("	1 day ago","")
        account = account.replace("	2 day ago","")
        account = account.replace("	",":")
        return(f"`İşte netflix hesabın : {the_netflix} [rastgele]`")

    if p_message == "siber premium":
        if username in premium_list:
            return("`Premium'un var!`")
        else:
            return("`Premium'un yok!`")
        



    
    if "siber premium add " in p_message:
        if username == owner:
            premium_text_file = open("premium_list.txt", "w")
            premium_add_name = message.removeprefix("siber premium add ")
            premium_text_file.write(premium_list + premium_add_name + "\n")
            premium_text_file.close()
            return f"`Premium listesine '{premium_add_name}' eklendi!`"
        else:


            return "`Owner değilsin!`"
    return



