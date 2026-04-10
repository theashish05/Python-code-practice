def write_log(message):
    with open(r"D:\py\Python-code-practice\app.log","a") as file:
        file.write(message+"\n")

write_log("App Started")
write_log("user logged in")
write_log("App stopped")