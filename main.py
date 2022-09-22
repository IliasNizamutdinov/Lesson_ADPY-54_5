from log_tools import track_log


name_file = 'logs/log_function.txt'

nested_list = ['Start',
	['a', 'b', 'c',['12','22',['33','44']]], 'Midle',
	['d', 'e', 'f', 'h', False, ['Что-то','Когда-нибудь'],[1,2,3,4]],
	[1, 2, None],'End'
]

@track_log(name_file)
def flat_generator(v_list):
    size = len(v_list)
    count = 1
    while count <= size:
        iter_val = v_list[count - 1]
        if not isinstance(iter_val,list):
            yield iter_val
        else:
            for it_ins in flat_generator(iter_val):
                yield (it_ins)
        count += 1


@track_log(name_file)
def sum(a, b):
    return a + b

@track_log(name_file)
def subt(a, b = 5):
    return a - b

def main():
   sum(10,12)
   subt(3,455)
   subt(a = 10, b = 5)
   for it in flat_generator(nested_list):
       print(it)

main()