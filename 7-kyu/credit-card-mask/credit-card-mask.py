# return masked string
def maskify(cc):
    len_s=len(cc)
    if len_s<=4:
        return cc
    else:
        mask_head=(len_s-4)*"#"
        tail=cc[-4:]
        print(mask_head+tail)
        
    return mask_head+tail