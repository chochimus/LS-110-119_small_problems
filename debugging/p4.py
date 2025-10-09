def get_key_value(my_dict, key):
    if key in my_dict:
        return my_dict[key]
    else:
        return None

print(get_key_value({"a": 1}, "b"))

# In python accessing a non-existant key using bracket will raise a key-error, instead we should use the in 
# operator, we can further simplify this function using get method

def get_key_value2(my_dict, key):
    return my_dict.get(key, None)

print(get_key_value2({"a": 1}, "b"))