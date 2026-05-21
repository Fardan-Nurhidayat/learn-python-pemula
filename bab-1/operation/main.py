from itertools import count

variabel = [1 , 2 , 3 ,4 ,4 , 4 ,5 ,6]

print(variabel)
print(variabel.count(4))


string = "Fardan Nurhidayat"
is_fardan_in_string = "Fardan" in string
print(is_fardan_in_string)

school = ["SMPN 1 CINEAM" , "SMKN Manonjaya" , "Politeknik Negeri Cilacap"]
juniorHighSchool , highSchool , college = school
print(juniorHighSchool)
school.sort(key=str.lower)
print(school)

age = 17
print(type(age))

x = "Dicoding"
x[0] = "F"

print(x)
