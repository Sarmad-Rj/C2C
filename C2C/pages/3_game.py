import streamlit as st
import random
import time

st.set_page_config(
    page_title="Game",
    page_icon="🎰", 
)

# --------------------------------------------0
def set_shade_only():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: linear-gradient(
                rgba(56, 234, 140, 1),
                rgba(255, 255, 255, 0.75)
            );
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_shade_only()


# --------------------------------------------1
col1, col2, col3 = st.columns([3, 10, 1]) 
with col1:
    pass

with col2:
    st.title(":rainbow[Guess The Number!] :sunglasses:" )

with col3:
    pass

# --------------------------------------------2
number = st.number_input("Enter a number from 1 to 15", min_value=1 , max_value=15)

# --------------------------------------------3
def wrong():
    st.toast('Try Again', icon = "😥")
    time.sleep(.5)

def right():
    st.toast('Congrats', icon = "🎉")
    time.sleep(1)

def guess_number(number):
    rn = random.randint(1, 15)
    if( number == rn ):
        st.success("## Congratulations You Guessed The Right Number!!")
        st.balloons()
        right()
    else: 
        st.warning("### ❌ You,ve Guessed the wrong number, Try again!")
        st.markdown(f"#### The number was: :green[{rn}]")
        wrong()
        

if st.button("Guess", type = "primary"):
    if number:
        guess_number(number)
        
    
    



















    