import streamlit as st
import random

#correcting the below Number Guess application
#
# - the random number needs to be stored in a session state
# - sidebar added 
# - cooloring text
# - showing an image
#

if 'number' in st.session_state:
    num = st.session_state['number']
else:
    num = random.randrange(1,10)
    st.session_state['number'] = num

col1,col2 = st.columns(2)

with col1:
    st.title('Welcome to ')

with col2:
 #   st.image('guess.jpg')
    st.subheader('#### Number Guess!')


# st.title("Welcome to Number Guess")
# st.write('### where you guess a number ')

# num = random.randrange(1,10)
st.write('### :blue[where you guess a number]')

txt_guess = int(st.text_input('Enter a number between 1 and 10: ', 1))

btn_start = st.button('Start Again')

if btn_start:
    num = random.randrange(1,10)
    st.write(num)
    st.session_state['number'] = num

btn_guess = st.button('Make a guess')

if btn_guess:
    if txt_guess == num:
        st.write("You win")
        st.balloons()
    else:
        st.write("Sorry. Wrong Number. Try again.")

btn_show = st.button('Show Number')

if btn_show:
    st.write("The number is ", num)

with st.expander("Help..."):
    st.write("Write a help doc here")

with st.sidebar:
    st.markdown('#### Copyright Acme Games')
    st.success('License Validated')
    st.slider('Rate this game:', 0,10)

