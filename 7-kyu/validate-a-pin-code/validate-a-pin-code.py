def validate_pin(pin):
    # return true or false
    
    if len(pin)!=4 and len(pin)!=6:
        return False
    for char in str(pin):
        if "0">char or char>"9":
            return False
    return True