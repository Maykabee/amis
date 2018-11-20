**TEST 1**
   _Code:`_`
      smth = [

    {
        "name": "Bob",
        "age":   20,
        "marks": {
                    "Math" : 98,
                    "Python" : 100
                 }
    },

    {
         "name": "Boba",
         "age":  19,
         "marks": {
                     "Physic" :98
                  }

    },

    {
         "name": "Boban",
         "age":   22,
         "marks": {
                  }

    }
         ]


def maxAge(smth,max=20):
    """ some magic and knowledge :) """


    if len(smth) == 0: #якщо ми перевірили уже всі елементи списку,то повертаємо результат
        return max
    if smth[0]['age'] > max: #якщо є число більше за максимальне за умовою,то це означає що саме це число тепер максимальне за умовою
        max = smth[0]['age']
    return maxAge(smth[1:], max) #перевіряємо наступний елемент списку

    return max

print(maxAge(smth))

   _Result:_
    ` 22`
    
 **TEST 2**
    _Code:`_
    smth = [

    {
        "name": "Bob",
        "age":   20,
        "marks": {
                    "Math" : 98,
                    "Python" : 100
                 }
    },

    {
         "name": "Boba",
         "age":  19,
         "marks": {
                     "Physic" :98
                  }

    },

    {
         "name": "Boban",
         "age":   22,
         "marks": {
                  }

    }
         ]
         
   def addMark(smth,name,disk,mark):
    """
     some magic and knowledge :)
     Повертає змінений список словників
      Args:
            smth: список словників
            name: ім'я студента
            disk: назва предмета
            mark: оцінка
        Returns:
           Список словників
        """

    for i in smth:
        if i["name"] == name:
            i["marks"][disk] = mark
    else:
        pass
    return smth
    
   _Result_:
   [{'name': 'Bob', 'age': 20, 'marks': {'Math': 98, 'Python': 100}}, {'name': 'Boba', 'age': 19, 'marks': {'Physic': 98, 'Math': 98}}, {'name': 'Boban', 'age': 22, 'marks': {}}]
   
   
  **TEST 3**
    _Code_
    smth = [

    {
        "name": "Bob",
        "age":   20,
        "marks": {
                    "Math" : 98,
                    "Python" : 100
                 }
    },

    {
         "name": "Boba",
         "age":  19,
         "marks": {
                     "Physic" :98
                  }

    },

    {
         "name": "Boban",
         "age":   22,
         "marks": {
                  }

    }
         ]
         
    def getNames(smth):
    """
     some magic and knowledge :)
    Повертає список імен студентів
    Args:
        smth: список словників
    Returns:
        Список імен студентів
    """
    names_list = [i_name['name'] for i_name in smth]
    return names_list
    
   _Result_:
    ['Bob', 'Boba', 'Boban']

 
