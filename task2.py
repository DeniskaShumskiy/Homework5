my_dict = {'first_one': 'we can do it'}

def biggest_dict(**kwargs):
    my_dict.update(**kwargs)

biggest_dict(name="Denis", age=30, weight=85, eyes_color="brown")
print(my_dict)