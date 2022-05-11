class RomanNumbers:
    '''Esta função transforma numeros romanos em inteiros, 
    caso seja necessário multiplicar o numero por mil esse deve ser seguido de um "*" '''
    @staticmethod
    def get_number_from_roman(n):
        n=str(n)

        #checando se todos os caracteres são válidos e se nao ha mais de 3 caracteres repetidos em sequencia 
        caract_in_seq = 0
        ultimo_caract = ''
        for caract in list(n): 
            if caract not in ("I","V","X","L","C","D","M","*"):
                return("entrada inválida")
            if caract == ultimo_caract:
                caract_in_seq += 1
                if caract_in_seq >=3:
                    return("entrada inválida")
            else:
                caract_in_seq = 0
            ultimo_caract = caract

        #traduzindo cada caracter recebido
        roman_numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, "*":"*"}
        translated_list = [*map(roman_numerals.get, list(n))]

        for i in range (len(translated_list)):
            if i+1 >= len(translated_list):
                pass
            else:
                if translated_list[i+1] == "*":
                    translated_list[i] = translated_list[i]*1000
        
        translated_list_mil = [i for i in translated_list if i != "*"]

        # if len(translated_list_mil)==1:
        #         return(translated_list_mil[0])

        sum=0
        for i in range (len(translated_list_mil)):
            num = translated_list_mil[i]
            if i+1 < len(translated_list_mil) and translated_list_mil[i+1] > num:
                sum -= num
            else: 
                sum += num
        return sum;
