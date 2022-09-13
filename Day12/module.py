import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
def random_user_id():
    str = ''
    for _ in range(6):
        str += random.choice(chars)
    return str

def user_id_gen_by_user():
    num = int(input('Enter the number of ID\'s'))
    limit = int(input('Enter the size of ID'))

    for _ in range(num):
        identity = ''.join([random.choice(chars) for _ in range(limit)])
        print(identity)

# user_id_gen_by_user()

def rgb_color_gen():

    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    print('rbg({},{},{})'.format(r,g,b))
rgb_color_gen()

def list_of_hexa_colors(many=0):
    if many == 0:
        many = random.randint(1, 10)
    hexas = "1,2,3,4,5,6,7,8,9,0,a,b,c,d,e,f".split(",")
    hexCodes = []
    for _ in range(many):
        hexCodes.append("#" + ''.join([random.choice(hexas) for _ in range(6)]))
    return hexCodes

def list_of_rgb_colors(many=0):
    if many == 0:
        many = random.randint(1, 10)
    rgbs = []
    for _ in range(many):
        rgbs.append(rgb_color_gen())
    return rgbs

def generate_colors(type_of_col, many):
    if type_of_col == 'hexa':
        return list_of_hexa_colors(many)
    elif type_of_col == 'rgb':
        return list_of_rgb_colors(many)
    else:
        return "Invalid Input"
