#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
#FONKSİYONLAR SİTEDE VERİLMİŞTİ GÖREV KARAKTER NEREDE DOĞARSA DOĞSUN ÇIKIŞA ULAŞTIRMAK

# yapabiliyorsa sağa dönmesini, sağa dönemezse 
 #dümdüz ilerlemesini veya son çare olarak sola 
# dönmesini sağlamaktır.
 
 #The functions move() and turn_left().
#Either the test front_is_clear() or wall_in_front(),
#right_is_clear() or wall_on_right(), and at_goal().
#How to use a while loop and if/elif/else statements.
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# YAPILMASININ NEDENİ SONSUZ WHILE ÖNLEMEK
while(front_is_clear()):
    move()
turn_left()

while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif(front_is_clear()):
            move()
        else:
            turn_left()        
"""