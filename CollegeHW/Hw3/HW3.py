Asia_list = ['IBM','Google','Acer','Asus','Hitachi']
Euro_list = ['Philip','HP','Simens','IBM','Google']
America_list = ['HP','Microsoft','Google','IBM']

Asia_list_set = set(Asia_list)
Euro_list_set = set(Euro_list)
America_list_set = set(America_list)

Global = Asia_list + Euro_list + America_list
Global_set = set(Global)
Union = list(Global_set)

print("Global=",Union)