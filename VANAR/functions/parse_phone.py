
# parse phone numbers from string:

# +373-022-123456

# to verify the numbers
# in/str -> out/bool

def validaetCountryCode(code):
    countryCodes = ['373',
                    '1242',
                    '1248']
    if code in countryCodes:
        return True
    else:
        return False



# in/str -> out/dict

# def parsePhoneNumber(input):
#     number = input[-6:]
#     output = {'number': number}
#     return output

def parsePhoneNumber(input):
    return{'country_code': input[-14: -11],
            'region_code': input[-10: -7],
            'number': input[-6:]}




#  def func validateRegionCode(code)
# validates regional code > list = [...]

# + create an algo : if/else->
# True country + region code validates

# make the parser more inteligent + enter nr sep -, /, " " or "" -> country code nu are separator -> None


p_str_1 = '+373-022-123456'
p_1 = parsePhoneNumber(p_str_1)
print(p_1)
print(validaetCountryCode(p_1['country_code']))