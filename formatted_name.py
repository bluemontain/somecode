def get_formatted_name(first_name,last_name, midele_name=''):
    """返回整洁的姓名"""
    if midele_name:
    	full_name = f"{first_name} {midele_name} {last_name}"
    else:
    	full_name = f"{first_name}  {last_name}"
	
    return full_name.title()

musician = get_formatted_name('jimi','henrix')
print(musician)

musician = get_formatted_name('jimi','henrix','lee')
print(musician)