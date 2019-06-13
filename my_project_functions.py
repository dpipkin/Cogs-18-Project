#This is the drink dictionary with the inputs associated with each (caffeine, type (creamy or light), price)
drink_dict ={'latte':(1,'creamy',1),'decaf latte':(0,'creamy',1),'green tea':(0,'light',0),'black tea':(1, 'light',0),'coffee':(1, 'creamy',0), 'decaf coffee':(0, 'creamy',0),'matcha latte':(1, 'creamy',1), 'chai latte':(1, 'creamy',1)}

#Below is a function that takes the temperature given and outputs hot or iced if it is below a certain temp
def hot_or_iced(outside_temp):
    '''Recommends hot or iced based on input temp 

    Parameters
    ----------
    input: float
    Outside temp input by user  
    
    Returns
    -------
    hot or iced: string
        Depending on outside temp'''
    
    if outside_temp < 55:
        return 'hot'
    else: 
        return 'iced'
    
#Below is a function that takes what you want in a drink and checks which item(s) in the dictionary match            
def recommend_drinks (outside_temp, kind_want, caffeine_want, price_want):
    '''Recommends drink(s) based on inputs 

    Parameters
    ----------
    inputs: float, string, int, int
        Outside temp input 
        String for kind of drink wanted
        Int representing caffeine content wanted
        Int representing price wanted
    
    Returns
    -------
    drink from drink_dict: string
        Depending on inputs given'''
    recommend_temp = hot_or_iced (outside_temp)
    output = []
    for drink in drink_dict:
        (caffeine, kind, price)= drink_dict [drink]
        if caffeine == caffeine_want and kind== kind_want and price==price_want:
            output.append (recommend_temp + ' '+ drink)         
    return output 
#This is the restaurant dictionary with the inputs associated with each (flavor size, price, location)
restaurant_dict = {'lemongrass':('strong','big',1, 'PC'), 'panda express':('mild','small',0, 'PC'), 'sunshine market':('mild', 'small', 1, 'PC'), 'santorini':('strong','big',1, 'PC'),'tap ex':('mild','small',0, 'PC'), 'seed n sprout':('strong','big',1, 'PC'),'bombay coast':('strong','big',0, 'PC'),'taco villa':('mild','big',0,'not PC'),'roots':('strong','big',0,'not PC'),'blue pepper':('strong','small',1, 'not PC')}

#Below is a function that takes what you want from a meal and checks which item(s) in the dictionary match
def recommend_restaurant (flavor_want, size_want, price_want, area_want):
    '''Recommends restuarant(s) based on inputs 

    Parameters
    ----------
    inputs: string, string, int, string
        String for mild or strong flavor wanted
        String for portion size wanted
        Int representing price wanted
        String for in Price Center or not
    
    Returns
    -------
    place from restaurant_dict: string
        Depending on inputs given'''
    output =[]
    for place in restaurant_dict:
        (flavor, size, price, area)= restaurant_dict [place]
        if flavor == flavor_want and size==size_want and price==price_want and area==area_want:
            output.append (place)
    return output