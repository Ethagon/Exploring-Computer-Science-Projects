import simplegui
global y_wraith
global x_char_head
global x_char_body
global x_wraith
global x_char_head2
global y_tear
global x_moon
global y_head2
global y_tear2
global rain
global end
global arms

y_wraith = 200
x_char_head = 250
x_char_body = 235
polygon_exist = 0
x_wraith = 500
x_char_head2 = 100
y_tear = 200
x_moon = 30
y_head2 = 245
y_tear2 = 245
rain = 125
end = 10
arms = 350

def draw_handler(canvas):
    # Draw Here!
    global x_char_body
    global y_wraith
    global x_char_head
    global x_wraith
    global x_char_head2
    global y_tear
    global x_moon
    global y_head2
    global y_tear2
    global rain
    global end
    global arms
    
    #moon
    canvas.draw_circle((x_moon, 50), 30, 30, "white", "white")
    x_moon = x_moon + 0.5
    canvas.draw_polygon([(x_moon, 50), (x_moon+10, 50), (x_moon+10, 60)], 3, "black", "black")
    
    #clouds
    for c in range(200,350,50):
        canvas.draw_circle((c + 50, 70), 30, 30, "darkgray", "darkgray")
        
    #Head
    canvas.draw_circle((x_char_head2, 250), 40, 3, "Black", "Tan")
    
    if y_wraith<=0:
        x_char_head = x_char_head + 2
    canvas.draw_circle((x_char_head, 250), 40, 3, "Black", "Tan")
    canvas.draw_circle((x_char_head+20, 245), 5, 3, "Black", "Black")
    canvas.draw_circle((x_char_head - 15, 245), 5, 3, "Black", "Black")
    
    #Eyes
    canvas.draw_circle((x_char_head2 - 15, y_head2), 5, 3, "Black", "Black")
    canvas.draw_circle((x_char_head2 + 15, y_head2), 5, 3, "Black", "Black")
    
    #Body of People
    canvas.draw_polygon([(x_char_head2 - 15, 290), (x_char_head2 + 15, 290), (x_char_head2 + 15, 390), (x_char_head2 - 15, 390)], 3, "Black", "blue")
    
   
    if y_wraith <= 0:
        x_char_body = x_char_body + 2
    canvas.draw_polygon([(x_char_body, 290), (x_char_body+35, 290), (x_char_body+35, 390), (x_char_body, 390)], 3, "Black", "Pink")
    
    #Arms
    canvas.draw_line((x_char_head2 - 15, 290), (x_char_head2 - 50, arms), 3, "Black")
    canvas.draw_line((x_char_head2 + 15, 290), (x_char_head2 + 35, arms), 3, "Black")
    
    
    canvas.draw_line((x_char_body, 290), (x_char_body-20, 350), 3, "Black")
    canvas.draw_line((x_char_body+35, 290), (x_char_body+55, 350), 3, "Black")
    canvas.draw_line((x_char_body, 450), (x_char_body, 380), 3, "Black")
    canvas.draw_line((x_char_body+35, 450), (x_char_body+35, 380), 3, "Black")
    
    #Legs
    canvas.draw_line((x_char_head2 - 15, 450), (x_char_head2 - 15, 380), 3, "Black")
    canvas.draw_line((x_char_head2 + 15, 450), (x_char_head2 + 15, 380), 3, "Black")
    
    y_wraith = y_wraith - 2
    #wraith
    for i in range(200,350,50):
        canvas.draw_circle((x_wraith, i-y_wraith), 40, 3, "Black", "Black")
    
        #wraith eyes
    if y_wraith <= 0:
        canvas.draw_polygon([(x_wraith - 20, 180), (x_wraith - 10, 190), (x_wraith - 20, 190)], 1, "Red", "Red")
        canvas.draw_polygon([(x_wraith + 20, 190), (x_wraith +30, 180), (x_wraith + 30, 190)], 1, "Red", "Red")
    
    if y_wraith <= 0:
        y_wraith = 0
        
        if y_wraith == 0:
            canvas.draw_polygon([(300, 200), (430, 200), (430, 500), (300, 500)], 3, "gray", "gray")
            polygon_exist = 1
            
        if polygon_exist == 1 and x_char_head == 370:
            x_char_head = x_char_head - 2
            x_char_body = x_char_body - 2
            x_wraith = x_wraith + 2
            x_char_head2 = x_char_head2 + 1
            
        if x_wraith >= 600:
            x_char_head2 = x_char_head2 - 1
            canvas.draw_circle((170, y_tear + 55), 2, 8, "Lightblue", "Lightblue")
            canvas.draw_circle((135, y_tear + 55), 2, 8, "Lightblue", "Lightblue")
            y_tear = y_tear + 0.5
        
        if y_tear == 500:
            y_tear = y_tear - 0.5
            canvas.draw_circle((170, y_tear + 55), 2, 8, "gray", "gray")
            canvas.draw_circle((135, y_tear + 55), 2, 8, "gray", "gray")
            y_head2 = y_head2 -0.25
            
        if y_head2 == 235:
            y_head2 = y_head2 + 0.25
            canvas.draw_circle((170, y_tear2), 2, 8, "Lightblue", "Lightblue")
            canvas.draw_circle((135, y_tear2), 2, 8, "Lightblue", "Lightblue")
            y_tear2 = y_tear2 + 0.5
            arms = arms - 0.25
            
        if y_tear2 == 500:
            y_tear2 = y_tear2 - 0.5
            canvas.draw_circle((170, y_tear2), 2, 8, "gray", "gray")
            canvas.draw_circle((135, y_tear2), 2, 8, "gray", "gray")
            canvas.draw_circle((300, rain), 2, 8, "Lightblue", "Lightblue")
            canvas.draw_circle((250, rain), 2, 8, "Lightblue", "Lightblue")
            rain = rain + 2
            
        if rain >= 500:
            end = end + 3
            canvas.draw_circle((300, 300), end, 10, "Black", "Black")
            
frame = simplegui.create_frame('An Unforetold Night', 600, 600)
frame.set_canvas_background("gray")
frame.set_draw_handler(draw_handler)
frame.start()
