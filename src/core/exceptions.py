def message(type, message):
    if type == "warning":
        type = "\u001b[33;1mWarning:\u001b[0m"
    if type == "error":
        type = "\u001b[31;1mError:\u001b[0m"
    if type == "info":
        type = "\u001b[0;1mInfo:\u001b[0m"
    
    print(f"{type} {message}")