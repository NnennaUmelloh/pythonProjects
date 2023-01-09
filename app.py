import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title = "BookSmart", page_icon =":books:", layout = "wide")


def lottieURL(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def localCSS(fileName):
    with open(fileName) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)

localCSS("style/style.css")

# ASSETS

booksAnimation = lottieURL("https://assets6.lottiefiles.com/packages/lf20_yg29hewu.json")
blackWoman = Image.open(r"C:\Users\Nnenna\Downloads\Python Website Projects\images\thought-catalog-IcUbKfIuQ70-unsplash.jpg")
blackMan = Image.open(r"C:\Users\Nnenna\Downloads\Python Website Projects\images\blackmanreading.png")
friends = lottieURL("https://assets7.lottiefiles.com/packages/lf20_r10qhb8x.json")


# HEADER SECTION

with st.container():
    st.subheader("Hi! I am Nnenna - the Mastermind behind BookSmart :smile:")
    st.title("BookSmart: An enclove for booklovers")
    st.write("""
    
    I love a good book and the people who love good books!

    I am a nerd. Data Scientist. Poet. Professor.
    
    """)
    st.write("[Learn more about me >](https://professoroakland.carrd.co/)")

# Why BookSmart
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)

    with left_column:
        st.header("Why I created BookSmart")
        st.write("""
        While I was making my rounds on various dating apps, I tried - to no avail - to find folks
        who enjoyed reading books. I thought that even if we didn't go out on a date,
        at the very least we'd probably be friends.

        While my efforts ultimately ended in failure, I thought to myself, wouldn't it be nice
        to meet other people based on the books we loved? 

        Thus BookSmart was born!
        """)

    with right_column:
        st_lottie(booksAnimation, height = 300, key = "coding")

# Who is it for?
with st.container():
    st.write("---")
    st.header("Who is BookSmart for?")
    st.write("##")
    image1_column, text_column = st.columns(2)

    with image1_column:
        st.image(blackMan)
 

    with text_column:
        st.subheader("Book Lovers!")
        st.write("""
        BookSmart is for people who enjoy reading books 
        and would like to meet other people who share that interest.
        """)

# What I hope you gain from using BookSmart?
with st.container():
    st.write("---")
    st.header("What do you gain from using BookSmart?")
    st.write("##")
    friends_column, text1_column = st.columns(2)

    with friends_column:
        st_lottie(friends, height = 250, key = "coding1")


    with text1_column:
        st.subheader("At least a new friend...")
        st.write("""
        Even if you never make it to the frist date, this is a space made by a book lover for other
        book lovers. At the very least, you'll find a new friend to host spirited 
        debates about our favorite books.
        """)

# Contact Form

with st.container():
    st.write("---")
    #st.header("Any Questions? :mailbox:")
    st.write("##")

    contactForm = """
    
    <form action="https://formsubmit.co/nnenna.d.umelloh@gmail.com" method="POST">
    <input type = "hidden" name = "_captcha" value = "true">
     <input type="text" name=" First Name" placeholder = "First Name" required>
     <input type="email" name="Email" placeholder = "Your Email" required>
     <input type="hidden" name="_subject" value="BookSmart Questions from Landing Page">
     <input type="hidden" name="_autoresponse" value="Thank you so much for reaching out! I look forward to answering your questions. Expect a reply within 1-2 business days.">
     <input type="hidden" name="_template" value="box">
     <form action="https://formsubmit.co/your-random-string" method="POST" />
     <textarea name = "message" placeholder = "Your questions and comments." required></textarea>
     <button type="submit">Send</button>
</form>

    """

leftColumn, rightColumn = st.columns(2)

with leftColumn:
    st.empty()

with rightColumn:
    #st.empty()
    st.header("Any Questions? :mailbox:")
    st.markdown(contactForm, unsafe_allow_html= True)

