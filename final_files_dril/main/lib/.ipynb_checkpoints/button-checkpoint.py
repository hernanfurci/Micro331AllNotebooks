from IPython.display import Image
from IPython.display import display, Markdown, clear_output
global prev_step 
prev_step = 'reset'
def reset_button_clicked(button, outt, output):
    def reset_button(b):
        with outt:
            global prev_step 
            clear_output()
            prev_step = 'reset'
            display(Image(filename='si_wafer.JPG'))
    return reset_button
def on_butt_clicked(button, outt):
    def click_button(b):
        with outt:
            global prev_step
            if(button.value == 'oxydation' and prev_step == 'reset'):
                print('1. Oxydation \n')
                display(Image(filename='oxidation.JPG'))
                prev_step = 'oxydation'
            elif(button.value == 'spin coating (photoresist + lift-off resist)' and prev_step == 'oxydation'):
                print('2. Spin coating (photoresist + lift-off resist) \n')
                display(Image(filename='spin_coating.JPG'))
                prev_step = 'spin coating (photoresist + lift-off resist)'
            elif(button.value == 'exposure' and prev_step == 'spin coating (photoresist + lift-off resist)'):
                print('3. Exposure \n')
                display(Image(filename='photolitho.JPG'))     
                prev_step = 'exposure'
            elif(button.value == 'development' and prev_step == 'exposure'):
                print('4. Development \n')
                display(Image(filename='development.JPG')) 
                prev_step = 'development'
            elif(button.value == 'thin film deposition' and prev_step == 'development'):
                print('5. Thin film deposition \n')
                display(Image(filename='thin_film_depo.JPG'))   
                prev_step = 'thin film deposition'
            elif(button.value == 'lift off'  and prev_step == 'thin film deposition'):
                print('6. Lift off \n')
                display(Image(filename='lift_off.JPG')) 
                print('Process flow validated, well done !')
            else:
                clear_output()
                print('Error in your process flow, try again')
                prev_step = 'reset'
                display(Image(filename='si_wafer.JPG'))
    return click_button